由于文件较大，便将所用的文件存放在阿里云盘下
文件链接https://www.aliyundrive.com/s/6eWz5MRXz9u

#opt
存放的是AIGO_C5MB开发板上/opt目录的文件，使用时先加载驱动insmod fpgadrv.ko，然后在/opt/deploy/目录下解压node-v16.14.2-linux-armv7l，之后输入node index.js即可，或者在/opt/deploy/目录下输入./test ./model ./images/*.jpg，推理结果存放在output文件夹下

#rice
存放的是paddlpaddle环境下的源码，使用方法见文件夹下的Rice文件
