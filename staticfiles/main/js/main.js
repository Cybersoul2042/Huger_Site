
var loader = document.getElementById("preloader");
if(window.location.href == "http://127.0.0.1:8000/"){
    loader.style.display = "none"
    window.onload = setTimeout(load, 2000);
}
else{
    loader.style.display = "none"
}
function load(){
    loader.style.display = "none";
}

document.addEventListener("DOMContentLoaded", () => {
    let mybutton = document.querySelector(".scroll-up");
    mybutton.addEventListener("click", () => topFunction())

    
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
        mybutton.style.opacity = "0.7";
    } else {
        mybutton.style.opacity = "0";
        mybutton.style.display = "none";
    }
    }

    
    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    } 
    if(document.querySelector('#login') != null){
        document.querySelector("#buttons").style.gridTemplateAreas = `road road video video home home
                                                                      about about contact contact home home
                                                                      footer footer footer footer footer footer`;
    }
    document.querySelector(".fa-bars").addEventListener("click", () => {
        let navbar = document.querySelector(".navbar-modal")
        if(navbar.style.height == "0px"){
            navbar.style.transform = "scaleY(1)"
            navbar.style.height = "200px"
        }
        else{
            navbar.style.transform = "scaleY(0)"
            navbar.style.height = "0px"
        }
        
    })
    document.querySelector('.about-huger').addEventListener('click', () => ShowModal());

    function ShowModal(){
        let modal = document.querySelector(".modal");

        if(modal.style.visibility == "visible"){
            document.querySelector('.fa-angle-up').style.rotate = "0deg";
            modal.style.opacity = "0";
            setTimeout(() => {
                modal.style.visibility = "hidden";
            }, 600);
            
        }
        else{
            document.querySelector('.fa-angle-up').style.rotate = "180deg";
            modal.style.visibility = "visible";
            modal.style.opacity = "100%";
        }
    }

    const slider = document.querySelector('.videos');
    const slides = document.querySelectorAll('.video');
    let slideWidth = 830; 
    window.onresize = window.onload = function() {
        if(window.innerWidth < 1024){
            slideWidth = 420;
        }
        else{
            slideWidth = 830;
            
        }
    }
    console.log(slideWidth)
    
    let currentIndex = 0;
    
    document.querySelector('#left')?.addEventListener("click", () => scrollPrev());
    document.querySelector('#right')?.addEventListener("click", () => scrollNext());

   
    function updateSlides() {
        slides.forEach((slide, index) => {
            if (index === currentIndex) {
                slide.style.transform = 'scale(1)'; 
                slide.style.opacity = 1;
            } else {
                slide.style.transform = 'scale(0.8)';
                slide.style.opacity = 0.5;
            }
        });
    }

   
    function scrollNext() {
        currentIndex = Math.min(currentIndex + 1, slides.length - 1);
        slider.scrollLeft = currentIndex * slideWidth;
        updateSlides();
    }

   
    function scrollPrev() {
        currentIndex = Math.max(currentIndex - 1, 0);
        slider.scrollLeft = currentIndex * slideWidth;
        updateSlides();
    }

  
    slider?.addEventListener('scroll', () => {
        currentIndex = Math.round(slider.scrollLeft / slideWidth);
        updateSlides();
    });

    updateSlides();

    document.querySelector("#contact").addEventListener("click", () => ScrollToView(".contact"))
    document.querySelector("#about").addEventListener("click", () => ScrollToView(".about"))
    document.querySelector("#road").addEventListener("click", () => ScrollToView(".road"))
    document.querySelector("#video").addEventListener("click", () => ScrollToView(".video"))

    function ScrollToView(element){
        if(window.location.href != "http://127.0.0.1:8000/"){
            window.location.assign("http://127.0.0.1:8000/")
            let scrollElement = document.querySelector(`${element}-section`)
            scrollElement.scrollIntoView({
                inline: "center",
                behavior: 'smooth'
            })
        }
        else{
            let scrollElement = document.querySelector(`${element}-section`)
            scrollElement.scrollIntoView({
                block: "center",
                behavior: 'smooth'
            })
        }
    }

})




