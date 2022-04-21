环境准备: python3.8,pipenv,docker,docker-compose

编辑器 vscode或者pycharm,vscode可以安装rest client插件

第一个项目为最简单的单文件api项目

第二个项目为使用flask蓝图实现多模块拆分

## 本地启动项目

```
//安装依赖
pipenv insstall

//启动项目
python run.py 
```

## 部署项目

可以使用docker-compose直接启动项目

docker-compose up 

## 测试接口

每个项目都附带了test.http文件,pycharm打开可以直接请求接口实例,vscode需要安装插件

