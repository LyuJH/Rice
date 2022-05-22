#!/usr/bin/node
var express = require('express');
var multer = require('multer');

var exec = require('child_process').exec;
// eslint-disable-next-line no-unused-vars
var fs = require("fs"); //引入fs，fs 是node中一个文件操作模块，包括文件创建，删除，查询，读取，写入。
// eslint-disable-next-line no-unused-vars
const { stdout } = require('process');

var app = express();
app.use(express.static('public'));
// eslint-disable-next-line no-undef
// MODEL_NAME='ssd_mobilenet_v1'
// eslint-disable-next-line no-undef
// MODEL_TYPE='\'1 # 1 combined paddle fluid model\''
// eslint-disable-next-line no-undef
// LABEL_NAME='labels/pascalvoc_label_list'
// eslint-disable-next-line no-undef
// IMAGE_NAME='steel_images/47.jpg'
// eslint-disable-next-line no-undef
// OUTPUT_IMAGE='47_result.jpg'



app.get('/', function (req, res) {
    res.send('Hello World');
})
app.get("/clean", function (req, res) {
    exec("rm -rf ./output/*",()=>{})
    exec("rm -rf ./upload/*",()=>{})
    res.send("Success!")
})
app.post("/detect", uploadFile, (req, res) => {
    //这里的req.body是经过uploadFile中间件进行处理后的,包含了表单中所有的提交内容
    console.log(req.body);
    // eslint-disable-next-line no-undef
    IMAGE_NAME=`./upload/${req.body.photo}`
    // eslint-disable-next-line no-undef
    OUTPUT_IMAGE=`./output/${req.body.photo}`
    // var libpath="export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/plite/lib &&"
    // eslint-disable-next-line no-unused-vars
    var libpath="";
    // var shellcmd=libpath+`./ssd_detection ${MODEL_NAME} ${MODEL_TYPE} ${LABEL_NAME} ${IMAGE_NAME} ${OUTPUT_IMAGE}`;
    // eslint-disable-next-line no-undef
    var shellcmd=`./test ./model ${IMAGE_NAME}`//开始推理
    // var shellcmd=`/opt/DetectionServer/yolov3_detection yolov3_mobilenet_v1_opt.nb ${IMAGE_NAME}`
    //获取推理完后的结果
    console.log(shellcmd)
    exec(shellcmd, function(error, stdout, stderr) {
        if (error) {
            console.error('error: ' + error);
            res.send(error);
            return;
        }
        console.log('stdout: ' + stdout+'stderr:'+stderr);
        // eslint-disable-next-line no-undef
        res.send({url:OUTPUT_IMAGE,info:stdout});
    });
})



//自定义中间件
function uploadFile(req, res, next) {
    let upload = multer({ dest: "upload/" }).single("image");
    upload(req, res, (err) => {
        if (err) {
            res.send("err:" + err);
        } else {
            req.body.photo = req.file.filename;
            next();
        }
    })
}



var server = app.listen(8081, function () {

    var host = server.address().address
    var port = server.address().port

    console.log("应用实例，访问地址为 http://%s:%s", host, port)

})
