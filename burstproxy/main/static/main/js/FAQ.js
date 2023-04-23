let arrow1 = document.querySelector('#arrow1');
let arrow2 = document.querySelector('#arrow2');
let arrow3 = document.querySelector('#arrow3');
let arrow4 = document.querySelector('#arrow4');
let arrow5 = document.querySelector('#arrow5');
let arrow6 = document.querySelector('#arrow6');
let arrow7 = document.querySelector('#arrow7');
let arrow8 = document.querySelector('#arrow8');
//***********************************************
let quest1 = document.querySelector('#quest1');
let quest2 = document.querySelector('#quest2');
let quest3 = document.querySelector('#quest3');
let quest4 = document.querySelector('#quest4');
let quest5 = document.querySelector('#quest5');
let quest6 = document.querySelector('#quest6');
let quest7 = document.querySelector('#quest7');
let quest8 = document.querySelector('#quest8');
//***********************************************
let answer1 = document.querySelector('#answer1');
let answer2 = document.querySelector('#answer2');
let answer3 = document.querySelector('#answer3');
let answer4 = document.querySelector('#answer4');
let answer5 = document.querySelector('#answer5');
let answer6 = document.querySelector('#answer6');
let answer7 = document.querySelector('#answer7');
let answer8 = document.querySelector('#answer8');
//***********************************************
let activequest = null;
let activeansver = null;
let activearrow = null;
let id = null;
let id1 = 0, id2 = 0, id3 = 0, id4 = 0, id5 = 0, id6 = 0, id7 = 0, id8 = 0;
//***********************************************
function quest1click(){
    activequest = quest1;
    activeansver = answer1;
    activearrow = arrow1;
    id = id1;
    questclick();
    id1 = id;
}
function quest2click(){
    activequest = quest2;
    activeansver = answer2;
    activearrow = arrow2;
    id = id2;
    questclick();
    id2 = id;
}
function quest3click(){
    activequest = quest3;
    activeansver = answer3;
    activearrow = arrow3;
    id = id3;
    questclick();
    id3 = id
}
function quest4click(){
    activequest = quest4;
    activeansver = answer4;
    activearrow = arrow4;
    id = id4;
    questclick();
    id4 = id;
}
function quest5click(){
    activequest = quest5;
    activeansver = answer5;
    activearrow = arrow5;
    id = id5;
    questclick();
    id5 = id;
}
function quest6click(){
    activequest = quest6;
    activeansver = answer6;
    activearrow = arrow6;
    id = id6;
    questclick();
    id6 = id;
}
function quest7click(){
    activequest = quest7;
    activeansver = answer7;
    activearrow = arrow7;
    id = id7;
    questclick();
    id7 = id;
}
function quest8click(){
    activequest = quest8;
    activeansver = answer8;
    activearrow = arrow8;
    id = id8;
    questclick();
    id8 = id;
}
//***********************************************
function questclick(){
    if (id == 0){
        activeansver.classList.remove('none');
        activearrow.classList.add('rotate180');
        id = 1;
    }else{
        activeansver.classList.add('none');
        activearrow.classList.remove('rotate180');
        id = 0;
    }
    return id;
}