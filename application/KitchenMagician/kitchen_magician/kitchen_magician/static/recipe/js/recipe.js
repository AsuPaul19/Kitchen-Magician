const favoriteBtn = document.querySelector("#favorite-block");
favoriteBtn.onclick = function() {
    console.log("clicked");
    if(favoriteBtn.style.value == "unsaved") {
        favoriteBtn.src = "../../static/recipe/images/favorite_heart_saved.png";
        favoriteBtn.style.value = "saved";
    } else {
        favoriteBtn.src = "../../static/recipe/images/favorite_heart_unsaved.png";
        favoriteBtn.style.value = "unsaved";
    }
}