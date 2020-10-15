module.exports = {
    //본문의 내용(HTML) 함수
    HTML:
    function(title, list, body, control){
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
        ${control}
        ${body}
      </body>
      </html> 
      `;
    },
    //리스트 목록들을 불러오는 함수
    list:
    function(filelist){
      // 리스트 목록들을 불러옴
      let list = '<ul>';
      for (let i = 0; i < filelist.length; i++){
        list += `<li><a href='/?id=${filelist[i]}'>${filelist[i]}</a></li>`;
      }
      list += '</ul>';
  
      return list
    }
}