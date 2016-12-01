### 简介
RIGGER CODE 轻量级代码脚手架 程序员开发代码的加速器

## 优点
无需懂Python代码
通过简单正则打造属于自己的模版
支持自定义语法规则
从枯燥的增删改查中解放出来

### 模版语法
```
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
### 安装
```
$ git clone https://github.com/luzijia/rigger_code
$ python setup.py install
```

### 使用
```python
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
    from rigger_code.core import *

    core.init("./data/default.ini")

    fields =  core.utilFields("User")

    fields_cond     = []
    fields_cond_val = []

    for field in fields:
        fields_cond.append('%s=?'%(field))
        fields_cond_val.append('$%s'%(field))

    #自定义语法规则
    ure=['##update_cond_str','##update_val_str']
    ustring=[",".join(fields_cond),",".join(fields_cond_val)]

    core.runmodel(ure,ustring,"User")

```
## 输出的模版
```
<?php
class User extends Table
{
    public function __construct()
    {
        parent::__construct("User", "uid");
    }

    public function add($info)
    {
        $this->addRecord($info);
    }

    public function getUserInfo($uid)
    {
        return $this->getRecord($uid);
    }

    public function delUser($uid)
    {
        $sql = "delete from {$this->getTableName()} where uid=?";
        return $this->Execute($sql, array($uid));
    }

    public function update($uid,$nickname,$addtime)
    {
        $sql = "update {$this->getTableName()} set nickname=?,addtime=? where uid=?";
        return $this->Execute($sql, array($nickname,$addtime,$uid));
    }
}

```

### 商业友好的开源协议
RIGGER CODE遵循MIT开源协议发布。MIT是和BSD一样宽范的许可协议,作者只想保留版权,而无任何其他了限制.也就是说,你必须在你的发行版里包含原许可协议的声明,无论你是以二进制发布的还是以源代码发布的.
