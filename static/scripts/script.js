const imgInput = document.getElementById("img_input");

imgInput.addEventListener("change", (event) => {
    const image = event.target.files[0];
    const formData = new FormData();
    formData.append('file', image);

    fetch("/vehicle_segment", {
            method: 'POST',
            body: formData
        }
    )
    .then(response => response.json())
    .then(data => {
        const textData = data.predicted;
        const imageData = data.image;
        
        const imgOutput = document.getElementById("img_output");
        imgOutput.src = 'data:image/png;base64,' + imageData;

        const textOutput = document.getElementById("text_output");
        textOutput.textContent = JSON.stringify(textData, undefined, 2);
    })
    .catch(error => console.error('Error:', error));
});
