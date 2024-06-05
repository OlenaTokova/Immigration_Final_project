document.addEventListener("DOMContentLoaded", function() {
    const recordButton = document.getElementById("recordButton");

    recordButton.addEventListener("click", () => {
        navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            const audioChunks = [];
            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks);
                const formData = new FormData();
                formData.append("audio", audioBlob, "voice.wav");

                fetch("/transcribe", {
                    method: "POST",
                    body: formData
                }).then(response => response.json()).then(data => {
                    document.getElementById("transcriptionResult").innerText = data.transcription;
                });
            });

            setTimeout(() => {
                mediaRecorder.stop();
            }, 5000);
        });
    });
});
