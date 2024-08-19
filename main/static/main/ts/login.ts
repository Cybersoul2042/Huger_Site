document.addEventListener("DOMContentLoaded", function(){
    var changeButtons = document.getElementsByClassName('change-button');

    for (var i = 0; i < changeButtons.length; i++) {
        changeButtons[i].addEventListener("click", () => ChangeRegistry(`button${i}`));
    }
})

function ChangeRegistry(button:string)
{
    let sliderPosition = document.querySelector<HTMLElement>('.slider')!.style;
    let signinPosition = document.querySelector<HTMLElement>('.sign-in')!.style;
    let registerPosition = document.querySelector<HTMLElement>('.register')!.style;

    if(sliderPosition.transform == "translate(0%)"){
        sliderPosition.transform = "translate(100%)";
        signinPosition.transform = "translate(-100%)";
        registerPosition.transform = "translate(0%)";
        console.log('register')
    }
    else{
        sliderPosition.transform = "translate(0%)";
        signinPosition.transform = "translate(0%)";
        registerPosition.transform = "translate(100%)";
        console.log('sign-in')
    }
}