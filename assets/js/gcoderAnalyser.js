var gcodeProcessorWorker = new Worker('js/gcodeProcessor.js?1801221');
var gcodeLines = undefined;
var selectedSettings = 0;
var results = Array(4);
var resultFieldIds = [];
var currentCalculationSetting = 0;
//var dropzone = document.getElementById('dropzone');
var histogram = Array(4);
//dropzone.style.cursor = 'pointer';
//dropzone.onmouseover = function () {
//  this.style.border = '3px dashed #909090';
//};
//dropzone.onmouseout = function () {
//  this.style.border = '3px dashed #cccccc';
//};
//makeDroppable(document.getElementById("importSettingsButton"), readSettings);

//$(document).ready(function () {
//  $('#viewerHelp').popover({
//    content: "&#8226 Make sure <b>Extrusion Mode</b> is selected correctly <br /> &#8226 <b>Filament Diameter</b> will affect line width",
//    html: true
//  });
//});
//
//makeDroppable(dropzone, readFile);

//function makeDroppable(element, callback) {
//
//  var input = document.createElement('input');
//  input.setAttribute('type', 'file');
//  input.setAttribute('multiple', false);
//  input.style.display = 'none';
//
//  input.addEventListener('change', triggerCallback);
//  element.appendChild(input);
//
//  element.addEventListener('dragover', function (e) {
//    e.preventDefault();
//    e.stopPropagation();
//    element.classList.add('dragover');
//  });
//
//  element.addEventListener('dragleave', function (e) {
//    e.preventDefault();
//    e.stopPropagation();
//    element.classList.remove('dragover');
//  });
//
//  element.addEventListener('drop', function (e) {
//    e.preventDefault();
//    e.stopPropagation();
//    element.classList.remove('dragover');
//    triggerCallback(e);
//  });
//
//  element.addEventListener('click', function () {
//    input.value = null;
//    input.click();
//  });
//
//  function triggerCallback(e) {
//    var files;
//    if (e.dataTransfer) {
//      files = e.dataTransfer.files;
//    } else if (e.target) {
//      files = e.target.files;
//    }
//    callback.call(null, files);
//  }
//}

//$(function () {
//  $("#canvasVerticalSlider").slider({
//    orientation: "vertical",
//    min: 1,
//    max: 2,
//    step: 1,
//    values: 1,
//  });
//  $("#canvasVerticalSlider").height($("#renderCanvas").height() - 96);
//  $("#canvasVerticalSlider").on("slide", function (event, ui) { setRender(ui.value) });
//});

gcodeProcessorWorker.onmessage = function (e) {
  if ("resultFormat" in e.data) {
    addResultTableEntries(e.data.resultFormat);
  } else if ("progress" in e.data) {
    setProgressBarPercent(e.data.progress);
  } else if ("complete" in e.data) {
    document.getElementById("progress").style = "display:none;";
    document.getElementById("calculateButton").style = "margin-bottom: 20px; display:true;";
    setProgressBarPercent(0);
  } else if ("result" in e.data) {
    results[currentCalculationSetting] = e.data.result;
    $("#layerNumber").text("(Generating...)");
    displayResult();
    generateView();
  } else if ("layers" in e.data) {
    gcodeProcessorWorker.postMessage("cleanup");
    initRender(e.data.layers, settingSets[currentCalculationSetting].filamentDiameter.value[0]);
  } else if ("histogram" in e.data) {
    histogram[currentCalculationSetting] = e.data.histogram;
    drawHistogram();
  }
}

//function displayResult() {
//  for (var i = 0; i < resultFieldIds.length; i++) {
//    var key = resultFieldIds[i];
//    if (results[selectedSettings] != undefined && results[selectedSettings][key] != undefined) {
//      document.getElementById(key).innerHTML = results[selectedSettings][key];
//    } else {
//      document.getElementById(key).innerHTML = "";
//    }
//  }
//}

//function setProgressBarPercent(percent) {
//  var progressBar = document.getElementById("progressBar");
//  progressBar.style = "-webkit-transition: none; transition: none;width: " + percent + "%;";
//  progressBar.setAttribute("aria-valuenow", percent);
//  progressBar.innerHTML = percent + "%";
//}

//function displayProgressBar() {
//  setProgressBarPercent(0);
//  document.getElementById("progress").style = "margin-bottom: 14px; display:true;";
//  document.getElementById("calculateButton").style = "display:none;";
//}

//function refreshStatistics() {
//  if (gcodeLines != undefined) {
//    displayProgressBar();
//    gcodeProcessorWorker.postMessage([gcodeLines, simpleSettingsDict(selectedSettings)]);
//    currentCalculationSetting = selectedSettings;
//  }
//}

//function readSettings(evt) {
//  var f = evt[0];
//  if (f) {
//    var r = new FileReader();
//    r.onload = function (e) {
//      importSettings(e.target.result);
//    }
//    r.readAsText(f);
//  }
//}

//function readFile(evt) {
//  var f = evt[0];
//  if (f) {
//    var size;
//    if (f.size / 1024 / 1024 < 1) {
//      size = (f.size / 1024).toFixed(1) + "KB";
//    } else {
//      size = (f.size / 1024 / 1024).toFixed(1) + "MB";
//    }
//    dropzone.innerHTML = f.name + " - " + size;
//    var r = new FileReader();
//    r.onload = function (e) {
//      gcodeLines = e.target.result.split(/\s*[\r\n]+\s*/g);
//      refreshStatistics();
//    }
//    r.readAsText(f);
//    displayProgressBar();
//  }
//}
