function checkboxFilter(e) {
    const VALUE = e.getAttribute("value");
    var recipeWrappers = document.querySelectorAll('.recipe-wrapper');
    for(var i = 0; i < recipeWrappers.length; i++) {
        // if the checkbox is checked
        if(!recipeWrappers[i].classList.contains(VALUE)) {
            if(e.checked) {
                // set display as 'none' for all recipes that don't have the class
                recipeWrappers[i].style.display = "none";
            } else {
                // set display as 'flex' for all recipes that don't have the class
                recipeWrappers[i].style.display = "flex";
            } 
        }
    }
}