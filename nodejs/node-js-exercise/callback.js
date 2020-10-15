/*
function a(){
    console.log('A');
}
*/
//익명함수 - javascript 에서는 함수가 값이다.
let a = function(){ 
    console.log('A');
}

function slowfunc(callback){
    callback();
}

slowfunc(a);