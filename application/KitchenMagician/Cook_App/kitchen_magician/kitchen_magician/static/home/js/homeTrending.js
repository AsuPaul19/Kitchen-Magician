const sliderTrending = document.querySelector('.slider');
const buttonsTrending = document.querySelectorAll('.btn');
const optionsTrending = document.querySelectorAll('.option');
const slidesTrending = document.querySelectorAll('.slider-img');

var index = 1;
var op_index = 0;
var size = slidesTrending[index].clientWidth;

updateTrending();

function updateTrending() {
    sliderTrending.style.transform = "translateX(" + (-size * index) + "px)";

    optionsTrending.forEach(option => option.classList.remove('colored'));
    optionsTrending[op_index].classList.add('colored');
}

function slideTrending() {
    sliderTrending.style.transition = "transform .5s ease-in-out";
    updateTrending();
}

function btnCheckTrending() {
    if (this.id === "prev") {
        index--;

        if(op_index == 0){
            op_index = 3;
        }
        else{
            op_index--;
        }
    }

    else if (this.id === "next") {
        index++;

        if(op_index == 3){
            op_index = 0;
        }
        else{
            op_index++;
        }
    }
    console.log(`Turning to index: ${index}`);
    console.log(`Turning to option: ${op_index}`);
    slideTrending();
}

function optionFuncTrending(){
    let i = Number(this.getAttribute('option-index'));
    index = i + 1;
    op_index = i;
    slideTrending();
}

sliderTrending.addEventListener('transitionend', () => {
    console.log("triggered slider event");
    if (slidesTrending[index].id === "first") {
        sliderTrending.style.transition = "none";
        index = slidesTrending.length - 2;
        sliderTrending.style.transform = "translateX(" + (-size * index) + "px)";
    }
    else if (slidesTrending[index].id === "last") {
        sliderTrending.style.transition = "none";
        index = 1;
        sliderTrending.style.transform = "translateX(" + (-size * index) + "px)";
    }
})

buttonsTrending.forEach(btn => btn.addEventListener('click', btnCheckTrending));
optionsTrending.forEach(option => option.addEventListener('click', optionFuncTrending));
