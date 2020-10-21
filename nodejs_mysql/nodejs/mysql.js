var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '111111',
  database : 'coke',
  port : '3307'
});

//mysql 접속
connection.connect();

connection.query('select * from topic', function (error, results, fields) {
  if (error){
      console.log(error);
  }
  console.log(results);
});
 
connection.end();