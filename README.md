环境准备: python3.8,pipenv,docker,docker-compose

编辑器: vscode或者pycharm,vscode可以安装rest client插件

技术栈: flask,uwsgi/gunicorn,nginx,docker

第一个项目为最简单的单文件api项目

第二个项目为使用flask蓝图实现多模块拆分

## restful介绍 

> RESTFUL是一种网络应用程序的设计风格和开发方式，基于HTTP，可以使用 XML 格式定义或 JSON 格式定义。最常用的数据格式是JSON。由于JSON能直接被JavaScript读取，所以，使用JSON格式的REST风格的API具有简单、易读、易用的特点


### 请求方式 

| GET（SELECT）  | 从服务器取出资源（一项或多项） |
|--------------|-----------------|
| POST（CREATE） | 在服务器新建一个资源  |
| PUT（UPDATE）  | 在服务器更新资源（更新完整资源） |
| PATCH（UPDATE） | 在服务器更新资源， PATCH更新个别属性 |
| DELETE（DELETE） | 从服务器删除资源      |


### 和传统模式对比 

| 方法 | 传统                                           | rest                                             |
|----|----------------------------------------------|--------------------------------------------------|
| 查询所有 | get <http://localhost:8080/employee/list>      | get <http://localhost:8080/employees>            |
| 查询单个 | get <http://localhost:8080/employee/list?id=1> | get <http://localhost:8080/employees/1>          |
| 添加 | post <http://localhost:8080/employee/add>      | post <http://localhost:8080/employees>           |
| 修改 | post <http://localhost:8080/employee/update>   | put <http://localhost:8080/employees>            |
| 删除 | post <http://localhost:8080/employee/delete>   | delete <http://localhost:8080//employees/%7Bid>} |


## 环境相关介绍 

pipenv: python虚拟环境管理工具

> pipenv主要有以下特性：
>
> pipenv集成了pip，virtualenv两者的功能，且完善了两者的一些缺陷
>
> 过去用virtualenv管理requirements.txt文件可能会有问题，Pipenv使用Pipfile和Pipfile.lock，后者存放将包的依赖关系，查看依赖关系是十分方便
>
> 各个地方使用了哈希校验，无论安装还是卸载包都十分安全，且会自动公开安全漏洞
>
> 支持Python2 和 Python3，在各个平台的命令都是一样的。

docker: Docker 是一个基于LXC技术构建的容器引擎

> 主要有如下优点
>
>部署方便
>
>隔离性
>
>快速回滚
>
>成本低

docker-cmpose: docker编排工具

> 优点通过文本的方式，把要处理的容器按照顺序执行，如果是多容器也就是通过一条命令就可以部署成功

uwsgi: uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议

nginx: 一个高性能的HTTP和反向代理web服务器

flask: python web开发框架

## 本地启动项目

```
//安装依赖
pipenv install

//启动项目
python run.py 
```

## 部署项目

可以使用docker-compose直接启动项目

```
docker-compose up 
```

## 测试接口

每个项目都附带了test.http文件,pycharm打开可以直接请求接口实例,vscode需要安装插件

