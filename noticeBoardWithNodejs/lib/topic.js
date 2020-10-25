const template = require('./template.js');
const db = require('./db.js');
const url = require('url');

exports.home = function(request,response){
    db.query('select * from board', function(error,topics){
        if (error) throw error;

        const title = 'Welcome to Blog';
        const Menu = template.menu(topics);
        const html = template.HTML(title,Menu);
        response.writeHead(200);
        response.end(html);
    });
}

exports.page = function(request,response){
    const _url = request.url;
    const queryData = url.parse(_url,true).query;
    db.query('select * from board', function(error,topics){
        db.query('select * from board where id=?',[queryData.id], function(error,topic){
            if (error) throw error;

            const title = topic[0].title;
            const Menu = template.menu(topics);
            const html = template.HTML(title,Menu);
            response.writeHead(200);
            response.end(html);
        });
    });  
}