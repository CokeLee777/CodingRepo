//http 모듈을 http 서버를 만들기 위하여 불러온다.
let http = require('http');
let fs = require('fs');
//url 이라는 모듈을 사용하기위해 불러온다.
let url = require('url');
let qs = require('querystring');
let template = require('./lib/template.js');
let path = require('path');

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
          let list = template.list(filelist);

          // template변수에 함수 적용
          let HTML = template.HTML(title, list,
            `<h2>${title}</h2>${description}`,
            `<a href="/create">create</a>`);

          //200이라는 숫자를 서버가 브라우저에게 주면 파일전송을 성공했다는 뜻
          response.writeHead(200);
          response.end(HTML);
        });

      //query string id 값이 있는 경우
      } else {

        fs.readdir('./data', function(error, filelist){
          //입력 정보에 대한 보안
          let filteredId = path.parse(queryData.id).base;

          //본문 내용 query string 값에 따라서 파일 읽어 오기
          fs.readFile(`data/${filteredId}`, 'utf-8', function(err, description){

            let title = queryData.id;
            
            //리스트 목록 불러오는 함수 호출
            let list = template.list(filelist);

            let HTML = template.HTML(title, list,
              `<h2>${title}</h2>${description}`,
              `<a href="/create">create</a>
               <a href="/update?id=${title}">update</a> 
               <form action="delete_process" method="post">
                <input type="hidden" name="id" value="${title}">
                <input type="submit" value="delete">
               </form>`);

          //200이라는 숫자를 서버가 브라우저에게 주면 파일전송을 성공했다는 뜻
          response.writeHead(200);
          response.end(HTML);
          });

        });

      }
      //사용자가 create 버튼을 클릭했을 때
    } else if (pathname === '/create'){

      fs.readdir('./data', function(error, filelist){

        //default 페이지 이기 때문에 title 과 세부내용을 변경
        let title = 'WEB - create';
        
        //리스트 목록 불러오는 함수 호출
        let list = template.list(filelist);

        // create 버튼을 누르면 텍스트 상자와 제출 버튼이 뜬다.
        let HTML = template.HTML(title, list, `
        <form action="/create_process" method="post">
          <p>
            <input type="text" name="title" placeholder="title">
          </p>
          <p>
            <textarea name="description" placeholder="description"></textarea>
          </p>
          <p>
            <input type="submit" value="submit">
          </p>
        </form>
        `, '');

        //200이라는 숫자를 서버가 브라우저에게 주면 파일전송을 성공했다는 뜻
        response.writeHead(200);
        response.end(HTML);
      });

      //사용자가 create 버튼을 누르고 submit 버튼을 눌렀을 때
    } else if (pathname === '/create_process'){
      let body = '';
      //request.on : 웹서버가 데이터를 받았을 때 callback 함수를 호출
      request.on('data', function(data){
        //웹서버가 받은 데이터를 body 에 추가
        body += data;
        //데이터가 너무 많으면
        if (body.length > 1e6) request.connection.destroy();

      });
      //데이터를 다 수신하고 더이상 받을 게 없다면
      request.on('end', function(){
        let post = qs.parse(body);
        let title = post.title;
        let description = post.description;
        fs.writeFile(`data/${title}`, description, 'utf-8', function(err){
          //302 코드는 페이지를 리다이렉션하는 뜻
          //사용자가 제출한 title의 description을 보여주는 페이지로 이동
          response.writeHead(302, {Location: `/?id=${title}`});
          response.end();
        });
      });
      
      //사용자가 update 버튼을 눌렀을 때
    } else if (pathname === '/update'){
      fs.readdir('./data', function(error, filelist){
        //입력 정보에 대한 보안
        let filteredId = path.parse(queryData.id).base;

        //본문 내용 query string 값에 따라서 파일 읽어 오기
        fs.readFile(`data/${filteredId}`, 'utf-8', function(err, description){

          let title = queryData.id;
          
          //리스트 목록 불러오는 함수 호출
          let list = template.list(filelist);

          let HTML = template.HTML(title, list, `
          <form action="/update_process" method="post">
            <input type="hidden" name="id" value="${title}">
            <p>
              <input type="text" name="title" placeholder="title" value="${title}">
            </p>
            <p>
              <textarea name="description" placeholder="description">${description}</textarea>
            </p>
            <p>
              <input type="submit" value="submit">
            </p>
          </form>
          `, `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`);

        //200이라는 숫자를 서버가 브라우저에게 주면 파일전송을 성공했다는 뜻
        response.writeHead(200);
        response.end(HTML);
        });

      });
    } else if (pathname === '/update_process'){
      let body = '';
      //request.on : 웹서버가 데이터를 받았을 때 callback 함수를 호출
      request.on('data', function(data){
        //웹서버가 받은 데이터를 body 에 추가
        body += data;
        //데이터가 너무 많으면
        if (body.length > 1e6) request.connection.destroy();

      });
      //데이터를 다 수신하고 더이상 받을 게 없다면
      request.on('end', function(){

        let post = qs.parse(body);
        let id = post.id;
        let title = post.title;
        let description = post.description;
        //바뀐 title 정보를 바탕으로 파일 저장
        fs.rename(`data/${id}`, `data/${title}`, function(err){
          //내용 저장
          fs.writeFile(`data/${title}`, description, 'utf-8', function(err){
            //302 코드는 페이지를 리다이렉션하는 뜻
            //사용자가 제출한 title의 description을 보여주는 페이지로 이동
            response.writeHead(302, {Location: `/?id=${title}`});
            response.end();
          });
        });

      });
      //사용자가 delete 버튼을 클릭했을 때
    } else if (pathname === '/delete_process'){
      let body = '';
      //request.on : 웹서버가 데이터를 받았을 때 callback 함수를 호출
      request.on('data', function(data){
        //웹서버가 받은 데이터를 body 에 추가
        body += data;
        //데이터가 너무 많으면
        if (body.length > 1e6) request.connection.destroy();

      });
      //데이터를 다 수신하고 더이상 받을 게 없다면
      request.on('end', function(){

        let post = qs.parse(body);
        let id = post.id;
        //입력 정보에 대한 보안
        let filteredId = path.parse(id).base;
        
        fs.unlink(`data/${filteredId}`, function(err){
          response.writeHead(302, {Location: `/`});
          response.end();
        });

      });

    } else {

      //그 외에 경로에는 에러 표시 (404라는 약속 된 번호)
      response.writeHead(404);
      response.end('Not found');
    }

 
});

app.listen(3000);