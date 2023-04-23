let sel6 = document.querySelector('#s4__s6');
let sel6opt1 = document.querySelector('#s4__s6i3o1');
let sel6opt2 = document.querySelector('#s4__s6i3o2');
let sel6opt3 = document.querySelector('#s4__s6i3o3');
let sel6opt4 = document.querySelector('#s4__s6i3o4');
let sel6opt5 = document.querySelector('#s4__s6i3o5');
//************************************************** */\
let active = null;
let actar = null;
let actind = null;
let i1;
let s6 = 0;
let active6 = sel6opt1;
let s6ar = [sel6opt1, sel6opt2, sel6opt3, sel6opt4, sel6opt5];
function end(){
    actind = 0;
    while (actind != actar.length){
        actar[actind].classList.add('none');
        actind++;
    }
    active6.classList.remove('none');
    active2.classList.remove('none');
    active.classList.remove('resize5');
    s6 = 0;
    s2 = 0;
}
//************************************************** */\
function s6click(){
    if (s6 == 0){
        sel6.classList.add('resize5');
        sel6opt1.classList.remove('none'); sel6opt2.classList.remove('none'); sel6opt3.classList.remove('none');
        sel6opt4.classList.remove('none'); sel6opt5.classList.remove('none');
        s6 = 1;
        if ((active != sel6)&(active != null)){
            end();
            s6 = 1;
        }
        active = sel6;
        actar = s6ar;
    }
    else{
        end();
    }
}
function s6i3o1click(){
    active6 = sel6opt1; 
}
function s6i3o2click(){
    active6 = sel6opt2;
}
function s6i3o3click(){
    active6 = sel6opt3;
}
function s6i3o4click(){
    active6 = sel6opt4;
}
function s6i3o5click(){
    active6 = sel6opt5;
}
//************************************************************************************************************************************/\
let sel2 = document.querySelector('#s4__s2');
let sel2opt1 = document.querySelector('#s4__s2i3o1');
let sel2opt2 = document.querySelector('#s4__s2i3o2');
let sel2opt3 = document.querySelector('#s4__s2i3o3');
let sel2opt4 = document.querySelector('#s4__s2i3o4');
let sel2opt5 = document.querySelector('#s4__s2i3o5');
//************************************************** */\
let i2;
let s2 = 0;
let active2 = sel2opt1;
let s2ar = [sel2opt1, sel2opt2, sel2opt3, sel2opt4, sel2opt5];
function s2click(){
    if (s2 == 0){
        sel2.classList.add('resize5');
        sel2opt1.classList.remove('none'); sel2opt2.classList.remove('none'); sel2opt3.classList.remove('none');
        sel2opt4.classList.remove('none'); sel2opt5.classList.remove('none');
        s2 = 1;
        if ((active != sel2)&(active != null)){
            end();
            s2 = 1;
        }
        active = sel2;
        actar = s2ar;
    }
    else{
        end();
    }
}
function s2i3o1click(){
    active2 = sel2opt1;
}
function s2i3o2click(){
    active2 = sel2opt2;
}
function s2i3o3click(){
    active2 = sel2opt3;
}
function s2i3o4click(){
    active2 = sel2opt4;
}
function s2i3o5click(){
    active2 = sel2opt5;
}