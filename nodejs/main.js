//http 모듈을 http 서버를 만들기 위하여 불러온다.
let http = require('http');
let fs = require('fs');
//url 이라는 모듈을 사용하기위해 불러온다.
let url = require('url');

//본문의 내용(HTML) 함수
function templateHTML(title, list, body){
  return `
  <!doctype html>
  <html>
  <head>
  <!--query string 의 id 값으로 title 을 준다.-->
    <title>WEB1 - ${title}</title>
    <meta charset="utf-8">
  </head>
  <body>

    <h1><a href="/">WEB</a></h1>
    ${list}
    ${body}
  </body>
  </html> 
  `;
}

//리스트 목록들을 불러오는 함수
function templateList(filelist){

  // 리스트 목록들을 불러옴
  let list = '<ul>';
  for (let i = 0; i < filelist.length; i++){
    list += `<li><a href='/?id=${filelist[i]}'>${filelist[i]}</a></li>`;
  }
  list += '</ul>';

  return list
}

let app = http.createServer(function(request,response){

    let _url = request.url;
    let queryData = url.parse(_url, true).query;
    //query string 을 제외한 path 는 pathname 에 담겨있다.
    let pathname = url.parse(_url, true).pathname;

    // path 가 없는 경로(query string 을 제외한 경로)로 접속 했다면 
    if (pathname ==='/'){

      //query string 이 없는 값, 즉 홈으로(WEB 링크 클릭시) 로 접속 할 경우
      if (queryData.id === undefined){

        fs.readdir('./data', function(error, filelist){

          //default 페이지 이기 때문에 title 과 세부내용을 변경
          let title = 'Welcome';
          description = 'Hello, Node.js';
          
          //리스트 목록 불러오는 함수 호출
          let list = templateList(filelist);

          // template변수에 함수 적용
          let template = templateHTML(title, list, `<h2>${title}</h2>${description}`);

          //200이라는 숫자를 서버가 브라우저에게 주면 파일전송을 성공했다는 뜻
          response.writeHead(200);
          response.end(template);
        });

      //query string id 값이 있는 경우
      } else {

        fs.readdir('./data', function(error, filelist){

          //본문 내용 query string 값에 따라서 파일 읽어 오기
          fs.readFile(`data/${queryData.id}`, 'utf-8', function(err, description){

            let title = queryData.id;
            
            //리스트 목록 불러오는 함수 호출
            let list = templateList(filelist);

            let template = templateHTML(title, list, `<h2>${title}</h2>${description}`);

          //200이라는 숫자를 서버가 브라우저에게 주면 파일전송을 성공했다는 뜻
          response.writeHead(200);
          response.end(template);
          });

        });

      }
      
    } else {

      //그 외에 경로에는 에러 표시 (404라는 약속 된 번호)
      response.writeHead(404);
      response.end('Not found');
    }

 
});

app.listen(3000);