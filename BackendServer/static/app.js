document.addEventListener('DOMContentLoaded', () => {
    constraints = { video: { facingMode: "environment" }, audio: false };
// Define constants
const cameraView = document.querySelector("#camera--view"),
        cameraOutput = document.querySelector("#camera--output"),
        cameraSensor = document.querySelector("#camera--sensor"),
        cameraTrigger = document.querySelector("#camera--trigger")
// Access the device camera and stream to cameraView
function cameraStart() {
        navigator.mediaDevices
            .getUserMedia(constraints)
            .then(function(stream) {
                        track = stream.getTracks()[0];
                        cameraView.srcObject = stream;
                    })
        .catch(function(error) {
                    console.error("Oops. Something is broken.", error);
                });
}
let modal_waiting = document.querySelector("#waiting");
let modal = document.querySelector("#art_info");
let closeBtn = document.querySelector(".close-btn");
// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() {
        cameraSensor.width = cameraView.videoWidth;
        cameraSensor.height = cameraView.videoHeight;
        cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
        cameraOutput.src = cameraSensor.toDataURL("image/webp");
        $.post( "/postmethod", {
            javascript_data:  cameraOutput.src
        }).done(function(response) { 
            console.log(response);
            data = JSON.parse(response);

            modal_waiting.style.display = "none";
            content = document.createElement("div");
            //content.innerHTML = data.artworkName;
            
            content.innerHTML =
                  `<p><span class='info-label'>Title:</span><span class='info-text'>${data.artworkName}</span></p>`
                + `<p><span class='info-label'>Artist:</span><span class='info-text'>${data.artistName}</span></p>`
                + `<p><span class='info-label'>Date:</span><span class='info-text'>${data.artworkDate}</span></p>`
                + `<p><a class='info-label' href=${data.artistWebsite}>Website</a></p>`

            $("#art_info .modal-content").append(content);
            modal.style.display = "block";
        } );
        cameraOutput.classList.add("taken");
        modal_waiting.style.display = "block";
};

closeBtn.onclick = function(){
    $("#art_info.modal-content").children().remove();
    modal.style.display = "none";
}
// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
})
