### 简介
RIGGER CODE 轻量级代码脚手架 程序员开发代码的加速器

## 优点
无需了解Python代码即可使用
安装后自动生成可执行文件
通过加载配置文件完成操作
预先生成语法格式模版中使用
从枯燥增删改查中解放出来
模版引擎使用了jinja2 为以后扩充打下基础


### 模版语法
```
    class {{tablename}} extends Table
    {
       public function __construct
       {
           parent::__construct("{{tablename}}", "{{pk}}");
       }
    }

    tablename 表名
    pk        主键

    fields_bind
        mysql bind 模式: field1=?,field2=?
    fields_cond
        mysql bind 模式的条件:array($field1,$field2)
    fields_cond_val: field1=$field1,field2=$field2

    $sql = "update {$this->getTableName()} set {{ fields_bind }}  where {{pk}}=?";
    会生成SQL：
    $sql = "update {$this->getTableName()} set nickname=?,addtime=?  where uid=?";

    $sql = "update {$this->getTableName()} set {{ fields_cond_val }}  where {{pk}}=?";
    会生成SQL：
    $sql = "update {$this->getTableName()} set nickname=$nickname,addtime=$addtime  where uid=?";

    这里还可以生成更多的模式

    ```
### 安装,需要sudo权限
```
$ git clone https://github.com/luzijia/rigger_code
$ chmod u+x setup.sh
$ ./setup.sh
```

### 使用
安装后会在dist目录生成rgc命令

```
$ rgc -h

Usage: rgc [options]

Options:
    --version           show program's version number and exit
    -h, --help          show this help message and exit
    -f FILE, --filename=FILE

rgc -f data/default.ini
file write into /tmp/User.php
file write into /tmp/Live.php
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


## 未来
rigger code 是我利用空闲时间开发，最初的灵感来源于要从枯燥的增删改查中解放出来。目前的rgc已完成对model层的自动化操作，未来可以把控制器层和模版层甚至js代码都做进去，但由于时间有限未来重点不在放到rgc中了，有兴趣继续完善的朋友可以fork且pull request给我。



