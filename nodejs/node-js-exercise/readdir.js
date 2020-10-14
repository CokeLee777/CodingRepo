const testFolder = './data';
const fs = require('fs');

//node.js 는 특정 디렉토리의 파일 목록을 배열로 돌려준다.
fs.readdir(testFolder, function(error, filelist){
    console.log(filelist);
});