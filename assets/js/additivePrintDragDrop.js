function textLinesFromFile(file, complete) {
    var reader = new FileReader();
    reader.onload = function(progressEvent){
        var lines = this.result.split('\n');
        complete(lines);
    };
  reader.readAsText(file);
};


//var gcodeProcessorWorker = new Worker('gcodeProcessor.js');
//gcodeProcessorWorker.postMessage("getResultFormat");

//https://github.com/eyal0/GCodeAnalyser/blob/master/js/gcodeAnalyser.js


window.addEventListener("drop", function(e) {
        e.preventDefault();
        document.getElementsByTagName("HTML")[0].style.opacity = 1;
        var gcodeNotification = document.getElementById("GCodeReservation");

        var lastFile = e.dataTransfer.files[0];
        var fileName = lastFile.name;
        var nameElements = fileName.split(".");
        var fileTypeName = nameElements[nameElements.length-1].toLowerCase();

        if (fileTypeName == "gcode") {
            gcodeNotification.classList.add("Visible");
            textLinesFromFile(lastFile, function (lines) {
            console.log("textlines created");

//            gcodeProcessorWorker.postMessage([lines, simpleSettingsDict(selectedSettings)]);

            });

            document.getElementById("GCodeTitle").innerHTML = fileName;

            var cancelButton = document.getElementById("cancelButton");
            cancelButton.addEventListener("click", function () {
                //remove file and close
                gcodeNotification.classList.remove("Visible");
            });
        }
        else {
            console.log("not gcode file");
        }

});


window.addEventListener("dragover", function(e) {
    e.preventDefault();
});

var lastTarget = null;

window.addEventListener("dragenter", function(e)
{
    lastTarget = e.target;
    document.getElementsByTagName("HTML")[0].style.opacity = 0.8;
});

window.addEventListener("dragleave", function(e) {
    if(e.target === lastTarget || e.target === document)
    {
        document.getElementsByTagName("HTML")[0].style.opacity = 1;
    }
});

