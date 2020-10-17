//모듈들 가져오기
const http = require('http');
const fs = require('fs');
const url = require('url');
const qs = require('querystring');
const path = require('path');

const CRUD = {
    CRUD_btn:
    function(action,title)
    {
        if (action === '/create')
        {
            return `
            <a href=${action}>create</a>
            `
        }
        else if (action === '/update')
        {
            return `
            <a href=${action}?id=${title}>update</a>
            `
        }
        else if (action === '/delete')
        {
            return `
            <form action=${action} method="post">
                <input type="hidden" name="id" value="${title}">
                <input type="submit" value="delete">
            </form>
            `
        }
        
    },
    CU_create:
    function(action)
    {
        return `
        <form action=${action} method="post">
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
        `
    },
    CU_update:
    function(action, title, description)
    {
        return `
        <form action=${action} method="post">
            <input type="hidden" name="id" value="${title}">
            <p>
                <input type="text" name="title" value="${title}" placeholder="title">
            </p>
            <p>
                <textarea name="description" placeholder="description">${description}</textarea>
            </p>
            <p>
                <input type="submit" value="submit">
            </p>
        </form>
        `
    }
}


const template = {
    HTML:
    function(title, list, description, create, update, del)
    {
        return`
        <!doctype html>
        <html>
            <head>
                <title>WEB1 - ${title}</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1><a href="/">WEB</a></h1>
                ${list}
                ${create} ${update} ${del}
                <h2>
                ${title}
                </h2>  
                ${description} 
            </body>
        </html>
        `
    },
    list:
    function(filelist)
    {
        let list = '<ul>';
        for (let i = 0; i < filelist.length; i++)
        {
            list += `<li><a href='/?id=${filelist[i]}'>${filelist[i]}</a></li>`;
        }
        list += '</ul>';
        return list
    }
}


const app = http.createServer(function(request,response)
{
    const _url = request.url;
    const queryData = url.parse(_url, true).query;
    const pathname = url.parse(_url, true).pathname;
    //query string 값이 없는 곳으로 접속했을 때
    if (pathname === '/')
    {
        //홈으로 접속했을 때
        if (queryData.id === undefined)
        {
            fs.readdir('./data', function(err,filelist)
            {
                let title = 'Welcome';
                let description = 'Hello Node js';
                let list = template.list(filelist);
                let HTML = template.HTML(title, list, description,CRUD.CRUD_btn('/create',title),``,``);
                response.writeHead(200);
                response.end(HTML);
            });
        }
        //홈이아닌곳으로 접속했을 때
        else
        {
            fs.readdir('./data', function(err,filelist)
            {
                fs.readFile(`./data/${queryData.id}`,'utf-8',function(err,description)
                {
                    let title = queryData.id;
                    let list = template.list(filelist);
                    let HTML = template.HTML(title, list, description,CRUD.CRUD_btn('/create',title), CRUD.CRUD_btn('/update',title), CRUD.CRUD_btn('/delete',title));
                    response.writeHead(200);
                    response.end(HTML);
                });
                
            });
        }
            
    }
    //생성 버튼을 눌렀을 때
    else if (pathname === '/create')
    {
        fs.readdir('./data', function(err,filelist)
        {
            let title = `Create Page`;
            let list = template.list(filelist);
            let HTML = template.HTML(title, list, ``,CRUD.CU_create('/create_process'),``,``);
            response.writeHead(200);
            response.end(HTML);   
        });
    }
    //생성했을 때
    else if (pathname === '/create_process')
    {
        let body = '';
        //웹 서버로 보낸 데이터 받아오기
        request.on('data', function(data)
        {
            body += data;
            //데이터가 너무 많으면
            if (body.length > 1e6) request.connection.destroy();
        });
        //데이터 받아오는 작업이 끝났을 때 수행
        request.on('end', function()
        {
            let post = qs.parse(body);
            let title = post.title;
            let description = post.description;
            //파일 쓰기
            fs.writeFile(`./data/${title}`,`${description}` ,'utf-8', function(err)
            {
                //사용자가 쓴 title 페이지로 이동하는 리다이렉션 수행
                response.writeHead(302, {Location: `/?id=${title}`});
                response.end();
            })
            console.log(post);
            
        });
        
    }
    //업데이트 버튼을 눌렀을 때
    else if (pathname === '/update')
    {
        fs.readdir('./data', function(err,filelist)
        {
            fs.readFile(`./data/${queryData.id}`,'utf-8',function(err,description)
            {
                
                let title = queryData.id;
                let list = template.list(filelist);
                let HTML = template.HTML(title, list, ``,``,CRUD.CU_update('/update_process',title,description),``);
                response.writeHead(200);
                response.end(HTML);
            }); 
        });
    }
    else if (pathname === '/update_process')
    {
        let body = '';
        //웹 서버로 보낸 데이터 받아오기
        request.on('data', function(data)
        {
            body += data;
            //데이터가 너무 많으면
            if (body.length > 1e6) request.connection.destroy();
        });
        //데이터 받아오는 작업이 끝났을 때 수행
        request.on('end', function()
        {
            let post = qs.parse(body);
            let id = post.id;
            let title = post.title;
            let description = post.description;
            console.log(body);
            console.log(post);
            fs.rename(`./data/${id}`, `./data/${title}`, function(err)
            {
                //파일 쓰기
                fs.writeFile(`./data/${title}`,description ,'utf-8', function(err)
                {
                    //사용자가 쓴 title 페이지로 이동하는 리다이렉션 수행
                    response.writeHead(302, {Location: `/?id=${title}`});
                    response.end();
                })
            });
            
        });
    }
    else if (pathname === '/delete')
    {
        let body= '';
        request.on('data', function(data)
        {
            body += data;
            if (body.length > 1e6) request.connection.destroy();
        });
        request.on('end', function()
        {
            let post = qs.parse(body);
            let id = post.id;
            fs.unlink(`./data/${id}`,function(err)
            {
                response.writeHead(302, {Location: `/`});
                response.end();
            });
        });
    }
    else
    {
        response.writeHead(404);
        response.end('Not found');
    }
});

app.listen(3000);