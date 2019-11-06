let Worker = require('tiny-worker');
let fs = require('fs');

gcodeLines = [];

settings = {"maxSpeed":[100,100,10,100],"maxPrintAcceleration":[1000,1000,100,10000],"maxTravelAcceleration":[1000,1000,100,10000],"maxJerk":[10,10,1,10],"absoluteExtrusion":false,"feedrateMultiplyer":100,"filamentDiameter":1.75,"firmwareRetractLength":2,"firmwareUnretractLength":2,"firmwareRetractSpeed":50,"firmwareUnretractSpeed":50,"firmwareRetractZhop":0,"timeScale":1.01}

let gcodeProcessorWorker = new Worker(__dirname + '/gcodeProcessor.js');
let progress = [];
let result = {};
const MIN_FILAMENT = 5;  // Don't record times for anything before the first 5mm of filament.
let filesize;
let totalFilamentUsed = Number.NEGATIVE_INFINITY;
gcodeProcessorWorker.onmessage = function (e) {
  if ("filePosition" in e.data) {
    progress.push(e.data);
    totalFilamentUsed = e.data["filamentUsage"];
  }
  if ("result" in e.data) {
    // progress is a list of objects, each with filePosition, printTime, and filamentUsage
    let totalPrintTime = progress[progress.length-1]["printTime"];
    result["estimatedPrintTime"] = totalPrintTime;

    // All the data is in progress now.
    result["progress"] = []
    result["progress"].push([0, result["estimatedPrintTime"]]);
    let last_printed_progress = Number.NEGATIVE_INFINITY;
    for (progress_entry of progress) {
      if (!('firstFilament' in result) && progress_entry["filamentUsage"] > 0) {
        // Output the file position where the first filament comes out, which is probably after the heatup time.
        result['firstFilament'] = progress_entry["filePosition"]/filesize;
        // Force writing progress.
        last_printed_progress = Number.NEGATIVE_INFINITY;
      }
      if (!('lastFilament' in result) && progress_entry["filamentUsage"] >= totalFilamentUsed) {
        // Output the file position where the last filament comes out, which is probably the start of cooldown.
        result['lastFilament'] = progress_entry["filePosition"]/filesize;
        // Force writing progress.
        last_printed_progress = Number.NEGATIVE_INFINITY;
      }
      let new_printed_progress = progress_entry["printTime"];
      if (last_printed_progress+60 < new_printed_progress) {
        result["progress"].push([progress_entry["filePosition"]/filesize, totalPrintTime - progress_entry["printTime"]]);
        last_printed_progress = new_printed_progress;
      }
    }
    result["progress"].push([progress[progress.length-1]["filePosition"]/filesize, totalPrintTime - progress[progress.length-1]["printTime"]]);
    result["progress"].push([1,0]);
    // All done.
    console.log(JSON.stringify(result));
    gcodeProcessorWorker.terminate();
  }
}
fs.readFile(process.argv[2], "utf8",
            function(err, data) {
              filesize = data.length;
              gcodeLines = data.split(/(?=[\r\n]+)/g);
              gcodeProcessorWorker.postMessage([gcodeLines, settings]);
            });
