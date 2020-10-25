module.exports = {
    HTML:function(title,menu){
        return `
        <!DOCTYPE html>
        <html>
        <head>
            <title>${title}</title>
            <meta charset='utf-8'>
        </head>
        <body>
            <h1><a href="/">Home</a></h1>
            ${menu}
        </body>
        </html>
        `
    },menu:function(topics){
        list = '<ul>';
        for(let i = 0; i < topics.length; i++){
            list +=  `<li><a href="/?id=${topics[i].id}">${topics[i].title}</a></li>`;
        }
        list += '</ul>';
        return list
    }
}