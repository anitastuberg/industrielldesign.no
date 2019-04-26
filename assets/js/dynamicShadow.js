$(document).ready(function () {
    let shadowLarge = $('.dynamic-shadow-large');
    let shadowSmall = $('.dynamic-shadow-small');


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

    function createShadowEvent(e) {
        if (shadowLarge.length > 0) {
                changeShadow(e, shadowLarge, 200, 200);
            }
            if (shadowSmall.length > 0) {
                changeShadow(e, shadowSmall, 70, 100);
            }
    }

    if (window.matchMedia("(max-width: 1000px)")) {

        document.onmousemove = function (e) {
            createShadowEvent(e);
        };
        $(window).scroll(function(e) {

            createShadowEvent(e);
        })
    }
});
