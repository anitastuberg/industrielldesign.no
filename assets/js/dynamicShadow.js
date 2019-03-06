$(document).ready(function () {
    let shadowBox = $('.dynamic-shadow');

    function changeShadow(e) {
        let mouseX = e.pageX;
        let mouseY = e.pageY;
        shadowBox.each(function () {
            let self = $(this);
            let offset = self.offset();
            let mouse = [mouseX, mouseY];
            let box = [offset.left + self.width() / 2, offset.top + self.height() / 2];
            let l = Math.sqrt(Math.pow((mouse[0] - box[0]), 2) + Math.pow((mouse[1] - box[1]), 2));
            let vf = [-(mouse[0] - box[0]) / l, -(mouse[1] - box[1]) / l];
            let shadowLength = Math.min(l, 40);
            let shadow = vf[0] * shadowLength + 'px ' + vf[1] * shadowLength + 'px 70px rgba(0,0,0,0.2)';
            self.css('box-shadow', shadow);
        })
    }

    document.onmousemove = function (e) {
        changeShadow(e);
    };
});
