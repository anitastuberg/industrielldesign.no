
function leftLightOn() {
    if (window.innerWidth > 760) {
        document.getElementById("footer_top").style.backgroundImage = "url(../img/footer/background_left_cropped.png)";
    }
}

function rightLightOn() {
    if (window.innerWidth > 760) {
        document.getElementById("footer_top").style.backgroundImage = "url(../img/footer/background_right_cropped.png";
        }
    }

function lightOff() {
    if (window.innerWidth > 760) {
        document.getElementById("footer_top").style.backgroundImage = "url(../img/footer/background_cropped.png)";
    }
    else {
        document.getElementById("footer_top").style.backgroundImage = "";
    }
    }

function variant() {
    if (window.innerWidth > 760) {
        document.getElementById("variant").src = "img/variant_blaa.svg";
        document.getElementById("footer_top").style.backgroundImage = "url(../img/footer/background_right_cropped.png)";
        }
    }

function variantOut() {
    if (window.innerWidth > 760) {
        document.getElementById("variant").src = "img/variant_hvit.svg";
        document.getElementById("footer_top").style.backgroundImage = url('{% static "img/footer/background_cropped.png" %}');
        }
    }

function slack() {
    if (window.innerWidth > 760) {
        document.getElementById("slack").src = "img/slack_farge.png";
        document.getElementById("footer_top").style.backgroundImage = "url(../img/footer/background_left_cropped.png)";
        }
    }

function slackOut() {
    if (window.innerWidth > 760) {
        document.getElementById("slack").src = "img/slack_blaa.svg";
        document.getElementById("footer_top").style.backgroundImage = url('{% static "img/footer/background_cropped.png" %}');
        }
    }


window.onresize = lightOff;