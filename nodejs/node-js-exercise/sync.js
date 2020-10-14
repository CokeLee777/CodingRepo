let fs = require('fs');
/*
//readFileSync (동기)
console.log('A');
let result = fs.readFileSync('node-js-exercise/sample1.txt', 'utf-8');
console.log(result);
console.log('C');
*/

//readFile (비동기)
console.log('A');
//readfile 은 리턴값이 없다.
fs.readFile('node-js-exercise/sample1.txt', 'utf-8', function(err,result){
    console.log(result);
});
console.log('C');