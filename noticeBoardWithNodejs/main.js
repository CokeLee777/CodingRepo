const http = require('http');
const url = require('url');
const template = require('./lib/template.js');
const db = require('./lib/db.js');
const topic = require('./lib/topic.js');

const app = http.createServer(function(request,response){
    const _url = request.url;
    const queryData = url.parse(_url,true).query;
    const pathname = url.parse(_url,true).pathname;
    
    if(pathname === '/'){
        if(queryData.id === undefined){
            topic.home(request,response);
        }else{
            topic.page(request,response);   
        }
    }else{
        response.writeHead(404);
        response.end('Not found');
    }

    
});

app.listen(3000);