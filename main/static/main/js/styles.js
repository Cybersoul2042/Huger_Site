let width;

width = window.innerWidth;
console.log(width)
if(width < 1024){
    document.querySelector('.sorry').style.display = "flex"
    document.getElementById('layout').style.display = "none";
}
else{
    document.querySelector('.sorry').style.display = "none"
    document.getElementById('layout').style.display = "grid";
}

