//View arrow move
const SLEEP_TIME = 500;
let viewCat = document.querySelectorAll(".cat-item-block");

// Add mouseenter and mouseleave to each view cat
for (var i = 0; i < viewCat.length; i++) {
    viewCat[i].addEventListener("mouseenter", viewArrowMove);
    viewCat[i].addEventListener("mouseleave", viewArrowStop);
}

// Start moving when mouseenter
async function viewArrowMove(e) {
    let arrow = e.target.querySelector(".view-arrow");
    arrow.dataset.hover = "true"
    await sleep(SLEEP_TIME); // starts after css animation
    if (arrow.classList.contains("view-arrow-right")) {
        moveLeft(arrow);
    } else {
        moveRight(arrow);
    }
}

async function moveLeft(arrow) {
    if (arrow.dataset.hover) {
        arrow.classList.add("view-arrow-left");
        arrow.classList.remove("view-arrow-right");
        await sleep(SLEEP_TIME);
        moveRight(arrow);
    }
}

async function moveRight(arrow) {
    if (arrow.dataset.hover) {
        arrow.classList.add("view-arrow-right");
        arrow.classList.remove("view-arrow-left");
        await sleep(SLEEP_TIME);
        moveLeft(arrow);
    }
}

// Stop when mouseleave
function viewArrowStop(e) {
    let arrow = e.target.querySelector(".view-arrow");
    arrow.dataset.hover = "";
    // Remove className view-arrow-left if contained
    if (arrow.classList.contains("view-arrow-left")) {
        arrow.classList.remove("view-arrow-left"); 
    }
    // Add className view-arrow-right if not contained
    if (!arrow.classList.contains("view-arrow-right")) {
        arrow.classList.add("view-arrow-right");
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
