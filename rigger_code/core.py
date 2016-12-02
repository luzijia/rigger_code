#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs
import myConfigParser
import db
import re
from jinja2 import Template

class core:
    db=''

    @staticmethod
    def init(filename):
        try:
            myConfigParser.myConfigParser.load(filename)

            host=myConfigParser.myConfigParser.get("MYSQL","host")
            user=myConfigParser.myConfigParser.get("MYSQL","user")
            port=int(myConfigParser.myConfigParser.get("MYSQL","port"))
            passwd=myConfigParser.myConfigParser.get("MYSQL","passwd")
            dbname=myConfigParser.myConfigParser.get("MYSQL","db")

            core.db = db.MyDb(host,port,user,passwd,dbname)
        except Exception,e:
            print e

    @staticmethod
    def runmodel(table_name):
        model_tpl=myConfigParser.myConfigParser.get("TPL","model")

        tpl_content = codecs.open(model_tpl).read()
        sql='show create table %s' %(table_name)
        struct=core.db.fetchone(sql)

        if(len(struct[1])==0):
            raise Exception("can't fetch table:%s"%(table_name))

        m = re.findall(r"PRIMARY KEY \(`(.*?)`\).*?", struct[1])
        if(len(m)==0):
            raise Exception("can't get PRIMARY_KEY of table:%s"%(table_name))

        pk = m[0]

        fields      =  core.utilFields(table_name)

        #预先生成好需要替换的格式
        #fields_bind mysql bind 模式: field1=?,field2=?
        #fields_cond mysql bind 模式的条件:array($field1,$field2)
        #fields_cond_val: field1=$field1,field2=$field2
        fields_bind     = []
        fields_cond     = []
        fields_cond_val = []

        for field in fields:
            fields_bind.append('%s=?'%(field))
            fields_cond.append('$%s'%(field))
            fields_cond_val.append('%s=$%s'%(field,field))

        tpl_content = codecs.open(model_tpl).read()

        template    = Template(tpl_content)
        tpl_content=template.render(tablename=table_name,pk=pk,fields_cond=fields_cond,fields_bind=fields_bind,fields_cond_val=fields_cond_val)

        core.writeTplContent(tpl_content,table_name)

    @staticmethod
    def utilFields(table_name):
        print "fetch %s Fidlds"%(table_name)
        sql='SHOW FIELDS FROM %s' %(table_name)
        fields=core.db.fetchall(sql)
        fields_used = []
        for field in fields:
            if(field[3]!='PRI'):
                fields_used.append(field[0])

        return fields_used

    @staticmethod
    def writeTplContent(tpl_content,table_name):
        output_file = re.sub(r'model',table_name,myConfigParser.myConfigParser.get("TPL","output_model"))
        output      = codecs.open(output_file,"w")
        output.write(tpl_content)
        print "file write into %s" %(output_file)

