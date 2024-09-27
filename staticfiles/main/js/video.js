// Select the HTML5 video
document.addEventListener("DOMContentLoaded", () => {
    let playBtn = document.getElementsByClassName('play')
    let rewindBtn = document.getElementsByClassName('rewind')
    let forwardBtn = document.getElementsByClassName('forward')
    let fullscreenBtn = document.getElementsByClassName('fullscreen')
    let downloadBtn = document.getElementsByClassName('download')

    Array.prototype.forEach.call(playBtn, function(element) {
        element.addEventListener('click', function(event){
            let videoCon = event.target.parentElement.parentElement;
            
            if(video.nodeName == "li"){
                console.log(video.id);
                video = videoCon.querySelector('#vid')
                if(video.paused){
                    video.play()
                }
                else{
                    video.pause()
                }
            }
            else{
                videoCon = videoCon.parentElement;
                video = videoCon.querySelector('#vid')
                if(video.paused){
                    video.play()
                }
                else{
                    video.pause()
                }
            }
            
        });
    });
    Array.prototype.forEach.call(rewindBtn, function(element) {
        element.addEventListener('click', function(event){
            let videoCon = event.target.parentElement.parentElement;
            if(video.nodeName == "li"){
                video = videoCon.querySelector('#vid')
                video.currentTime = video.currentTime - ((video.duration/100) * 5)
            }
            else{
                videoCon = videoCon.parentElement;
                video = videoCon.querySelector('#vid')
                video.currentTime = video.currentTime - ((video.duration/100) * 5)
            }
            
        });
    });
    Array.prototype.forEach.call(forwardBtn, function(element) {
        element.addEventListener('click', function(event){
            let videoCon = event.target.parentElement.parentElement;
            if(video.nodeName == "li"){
                video = videoCon.querySelector('#vid')
                video.currentTime = video.currentTime + ((video.duration/100) * 5)
            }
            else{
                videoCon = videoCon.parentElement;
                video = videoCon.querySelector('#vid')
                video.currentTime = video.currentTime + ((video.duration/100) * 5)
            }
            
        });
    });
    Array.prototype.forEach.call(fullscreenBtn, function(element) {
        element.addEventListener('click', function(event){
            let videoCon = event.target.parentElement.parentElement;
            event.preventDefault()
            if(video.nodeName == "li"){
                console.log(video.id);
                video = videoCon.querySelector('#vid')
                video.requestFullscreen()
            }
            else{
                videoCon = videoCon.parentElement;
                video = videoCon.querySelector('#vid')
                video.requestFullscreen()
            }
            
        });
    });
    Array.prototype.forEach.call(downloadBtn, function(element) {
        element.addEventListener('click', function(event){
            let videoCon = event.target.parentElement.parentElement;
            event.preventDefault()
            if(video.nodeName == "li"){
                video = videoCon.querySelector('#vid')
                let a = document.createElement('a')
                a.href = video.src 
                a.target = "_blank"
                a.download = ""
                document.body.appendChild(a)
                a.click()
                document.body.removeChild(a)
            }
            else{
                videoCon = videoCon.parentElement;
                video = videoCon.querySelector('#vid')
                let a = document.createElement('a')
                a.href = video.src 
                a.target = "_blank"
                a.download = ""
                document.body.appendChild(a)
                a.click()
                document.body.removeChild(a)
            }
            
        });
    });

    let videos = document.getElementsByClassName("video")
    console.log(videos)
    Array.prototype.forEach.call(videos, function(videocon){
        let video = videocon.querySelector('#vid')
        video.addEventListener("timeupdate", (event) => {
            let video = event.target
            let curr = (video.currentTime / video.duration) * 100;
            if(video.ended){
                video.parentElement.querySelector(".fa-play").style.display = "block";
                video.parentElement.querySelector(".fa-pause").style.display = "none";
            }
            video.parentElement.querySelector('.inner').style.width = `${curr}%`;
        });
    });

})
    

