const express = require("express"); //express framework to have a higher level of methods
const app = express()
var http = require("http");
const WebSocket = require("ws");
const server = http.createServer(app);
const fs = require('fs')
// const s = new WebSocket.Server({ server });
const s = new WebSocket.WebSocketServer({port:3000,path:'/ws'})
require("dns").lookup(require("os").hostname(), function (err, add, fam) {
    console.log("addr: " + add + "fam: " + fam);
  });

  app.get("/", function (req, res) {
    res.end("");
  });

  s.on("connection", function (ws, req) {
    console.log("client connected");
    ws.on("message", function (message) {
      let data = JSON.parse(message)
      let buff=fs.readFileSync('BufferData.csv').toString()
      buff=buff.split('\n')
      console.log(buff)
      let head = buff[0]
      buff.shift()
      console.log(buff)
      if(buff.length>100){
        buff.shift()
        let p = [data['Ammonia'],data['Benzene'],data['CO2'],data['Nitrox'],data['Alcohol']]
        buff.push(p.join(','))
  
        buff=buff.join('\n');
        head = head+'\n'+buff;
        fs.writeFileSync('BufferData.csv',head)
      } else {
        let p = [data['Ammonia'],data['Benzene'],data['CO2'],data['Nitrox'],data['Alcohol']]
        buff.push(p.join(','))
  
        buff=buff.join('\n');
        head = head+'\n'+buff;
        fs.writeFileSync('BufferData.csv',head)
      }
      console.log(message);
    });
    ws.on("close", function () {
      console.log("client lost");
    });
  });

  app.listen(9000)