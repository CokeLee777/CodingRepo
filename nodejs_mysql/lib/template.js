module.exports = {
  HTML:function(title, list, body, control){
    return `
    <!doctype html>
    <html>
    <head>
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
  },list:function(topics){
    var list = '<ul>';
    var i = 0;
    while(i < topics.length){
      list = list + `<li><a href="/?id=${topics[i].id}">${topics[i].title}</a></li>`;
      i = i + 1;
    }
    list = list+'</ul>';
    return list;
  },authorSelect:function(authors, author_id){
    let tag = '';
    for(let i = 0;i < authors.length; i++){
      let selected = '';
      //현재의 id 와 루프안의 id 가 같다면
      //update 버튼을 눌렀을 때 원래있던 옵션으로 기본값으로 설정
      if(authors[i].id === author_id){
        selected = 'selected';
      }
      tag += `<option value="${authors[i].id}"${selected}>${authors[i].name}</option>`
    }
    return `
    <select name="author">
      <option>${tag}</option>
    </select>
    `
  }
}
