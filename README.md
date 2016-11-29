## 简介
RIGGER CODE 轻量级代码脚手架 程序员开发代码的加速器

## 模版说明
```python
    class ##tablename extends Table
    {
       public function __construct
       {
           parent::__construct("##tablename", "##pk");
       }
    }
    ##tablename 表名
    ##pk        主键
```
## 安装
```python
$ python setup.py install
```

## 使用
```python

    CREATE TABLE `User` (
            `uid` int(11) NOT NULL AUTO_INCREMENT,
            `nickname` varchar(255) COLLATE utf8_bin NOT NULL,
            `addtime` datetime NOT NULL,
            PRIMARY KEY (`uid`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8


    from rigger_code.core import *
    core.init("./data/default.ini")
    core.runmodel("User")
```
## 商业友好的开源协议
RIGGER CODE遵循MIT开源协议发布。MIT是和BSD一样宽范的许可协议,作者只想保留版权,而无任何其他了限制.也就是说,你必须在你的发行版里包含原许可协议的声明,无论你是以二进制发布的还是以源代码发布的.
