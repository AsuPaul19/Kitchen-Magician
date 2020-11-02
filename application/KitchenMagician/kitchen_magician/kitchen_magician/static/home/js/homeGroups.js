const sliderGroups = document.querySelector('.groups');
const buttonsGroups = document.querySelectorAll('.groups-btn');
const optionsGroups = document.querySelectorAll('.groups-option');
const slidesGroups = document.querySelectorAll('.groups-img');

var index = 1;
var op_index = 0;
var size = slidesGroups[index].clientWidth;

updateGroups();

function updateGroups() {
    sliderGroups.style.transform = "translateX(" + (-size * index) + "px)";

    optionsGroups.forEach(optionGroups => optionGroups.classList.remove('colored'));
    optionsGroups[op_index].classList.add('colored');
}

function slideGroups() {
    sliderGroups.style.transition = "transform .5s ease-in-out";
    updateGroups();
}

function btnGroupsCheck() {
    if (this.id === "prev") {
        index--;

        if(op_index == 0){
            op_index = 7;
        }
        else{
            op_index--;
        }
    }

    else if (this.id === "next") {
        index++;

        if(op_index == 7){
            op_index = 0;
        }
        else{
            op_index++;
        }
    }
    console.log(`Turning to index: ${index}`);
    console.log(`Turning to option: ${op_index}`);
    slideGroups();
}

function optionGroupsFunc(){
    let i = Number(this.getAttribute('option-index'));
    index = i + 1;
    op_index = i;
    slideGroups();
}

sliderGroups.addEventListener('transitionend', () => {
    console.log("triggered slider event");
    if (slidesGroups[index].id === "first") {
        sliderGroups.style.transition = "none";
        index = slidesGroups.length - 2;
        sliderGroups.style.transform = "translateX(" + (-size * index) + "px)";
    }
    else if (slidesGroups[index].id === "last") {
        sliderGroups.style.transition = "none";
        index = 1;
        sliderGroups.style.transform = "translateX(" + (-size * index) + "px)";
    }
})

buttonsGroups.forEach(btn => btn.addEventListener('click', btnGroupsCheck));
optionsGroups.forEach(option => option.addEventListener('click', optionGroupsFunc));
