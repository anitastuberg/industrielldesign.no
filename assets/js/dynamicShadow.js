$(document).ready(function () {
    let shadowProject = $('.dynamic-shadow-project');
    let shadowEvent = $('.dynamic-shadow-event');


    function changeShadow(e, item, sl, spred) {
        let mouseX = e.pageX;
        let mouseY = e.pageY;
        item.each(function () {
            let self = $(this);
            let offset = self.offset();
            let mouse = [mouseX, mouseY];
            let box = [offset.left + self.width() / 2, offset.top + self.height() / 2];
            let l = Math.sqrt(Math.pow((mouse[0] - box[0]), 2) + Math.pow((mouse[1] - box[1]), 2));
            let vf = [-(mouse[0] - box[0]) / l, -(mouse[1] - box[1]) / l];
            let shadowLength = Math.min(l, sl);
            let shadow = vf[0] * shadowLength + 'px ' + vf[1] * shadowLength + 'px ' + spred + 'px rgba(52,79,87,0.3)';
            self.css('box-shadow', shadow);
        })
    }

    if (window.matchMedia("(max-width: 1000px)")) {

        document.onmousemove = function (e) {

            if (shadowProject.length > 0) {
                changeShadow(e, shadowProject, 200, 200);
            }
            if (shadowProject.length > 0) {
                changeShadow(e, shadowEvent, 70, 100);
            }
        };
    }
});
