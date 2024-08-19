document.addEventListener("DOMContentLoaded", function () {
    var changeButtons = document.getElementsByClassName('change-button');
    for (var i = 0; i < changeButtons.length; i++) {
        changeButtons[i].addEventListener("click", function () { return ChangeRegistry("button".concat(i)); });
    }
});
function ChangeRegistry(button) {
    var sliderPosition = document.querySelector('.slider').style;
    var signinPosition = document.querySelector('.sign-in').style;
    var registerPosition = document.querySelector('.register').style;
    if (sliderPosition.transform == "translate(0%)") {
        sliderPosition.transform = "translate(100%)";
        signinPosition.transform = "translate(-100%)";
        registerPosition.transform = "translate(0%)";
        console.log('register');
    }
    else {
        sliderPosition.transform = "translate(0%)";
        signinPosition.transform = "translate(0%)";
        registerPosition.transform = "translate(100%)";
        console.log('sign-in');
    }
}
//# sourceMappingURL=login.js.map