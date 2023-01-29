
function settime() {
    var video = document.getElementById("home-video");
    video.currentTime = 0;
    video.play();
    console.log(video.currentTime);
    setInterval(function () {
        if (video.currentTime > 15) {
            video.pause();
        }
    }, 1000);
}