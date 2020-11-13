function showPreview(event) {
    if(event.target.files.length > 0) {
        var src = URL.createObjectURL(event.target.files[0]);
        var preview = document.querySelector("#image-preview");
        preview.src = src;
        preview.style.display = "block";

    }
}

const btnSubmit = document.querySelector(".recipe-submit-btn");
btnSubmit.addEventListener("click", imageAlert);
function imageAlert() {
    var preview = document.querySelector("#image-preview");
    var uploaded = preview.style.display;
    if(!uploaded) {
        alert("Please upload an image for your recipe, thank you!")

    }
}