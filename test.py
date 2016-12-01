#!/usr/bin/python
# -*- coding: UTF-8 -*-

from rigger_code.core import *

core.init("./data/default.ini")

#工具获取字段
fields =  core.utilFields("User")

#定义属于你自己的语法替换规则
fields_cond     = []
fields_cond_val = []

for field in fields:
    fields_cond.append('%s=?'%(field))
    fields_cond_val.append('$%s'%(field))

ure=['##update_cond_str','##update_val_str']
ustring=[",".join(fields_cond),",".join(fields_cond_val)]

#生成模版文件
core.runmodel(ure,ustring,"User")
