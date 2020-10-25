const mysql = require('mysql');
//mysql에 접속하기위한 정보 입력
const db = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : '111111',
    database : 'coke',
    port : '3307'
});
//mysql 접속
db.connect();

module.exports = db;