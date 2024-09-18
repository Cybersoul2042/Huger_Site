document.querySelector('#left').addEventListener("click", () => scrollPrev())
document.querySelector('#right').addEventListener("click", () => scrollNext())

const slider = document.querySelector('.videos');
const slides = document.querySelectorAll('.video');
const slideWidth = 660; // Width of the slide (400px) + margin (10px * 2)
let currentIndex = 0;

// Update the scale of the slides
function updateSlides() {
    slides.forEach((slide, index) => {
        if (index === currentIndex) {
            slide.style.transform = 'scale(1)'; // Enlarge the current slide
            slide.style.opacity = 1;
        } else {
            slide.style.transform = 'scale(0.8)'; // Reset the scale of other slides
            slide.style.opacity = 0.5;
        }
    });
}

// Scroll to the next slide
function scrollNext() {
    currentIndex = Math.min(currentIndex + 1, slides.length - 1);
    slider.scrollLeft = currentIndex * slideWidth;
    updateSlides();
}

// Scroll to the previous slide
function scrollPrev() {
    currentIndex = Math.max(currentIndex - 1, 0);
    slider.scrollLeft = currentIndex * slideWidth;
    updateSlides();
}

// Handle snapping and resizing
slider.addEventListener('scroll', () => {
    // Calculate the closest slide index
    currentIndex = Math.round(slider.scrollLeft / slideWidth);
    updateSlides();
});

updateSlides();


