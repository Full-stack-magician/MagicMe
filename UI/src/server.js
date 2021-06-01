//1.引入express

const { request, response } = require('express');
const express = require('express');
//2。创建应用对象
const app=express();
//3.创建路由规则
//request 是对请求报文的封装
//resonse 是对响应报文的封装
app.all('/server',(request,response)=>{
    //设置响应头，设置允许跨域
    response.setHeader('Access-Control-Allow-Origin','*');
    //设置响应体
    response.send('Hello Ajax');

});

app.all('/json-server',(request,response)=>{
    //设置响应头，设置允许跨域
    response.setHeader('Access-Control-Allow-Origin','*');
    
    //响应一个数据
    const data={
        name:'atguigu'
    };
    //对对象进行字符串转换
    let str=JSON.stringify(data);
    //设置响应体
    response.send(str);

});
//延时响应
app.all('/delay',(request,response)=>{
    //设置响应头，设置允许跨域
    response.setHeader('Access-Control-Allow-Origin','*');
    
    setTimeout(()=>{
    //设置响应体
        response.send("超时");
    },3000)
});
//4.监听端口启动服务
app.listen(8000,()=>{
console.log("服务已启动，8000 端口监听中...")
});
app.all('/axios-server',(request,response)=>{
    response.setHeader('Access-Control-Allow-Origin','*');
    
    response.setHeader('Access-Control-Allow-Headers','*');
    console.log(request.query.account);
    if (request.query.account == 123 && request.query.password == 456) {
        
        response.send("1");
      } else {
        
        response.send("0");
      }
});
