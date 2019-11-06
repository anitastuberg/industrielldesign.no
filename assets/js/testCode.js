onmessage = function (e) {
    if (e.data == "getResultFormat") {
        this.setTimeout(4000);
        console.log("getResultFormat");
        //postMessage({ "resultFormat": gcodeProcessor.results });
    } else {
        console.log("else part of function");
    }
};
