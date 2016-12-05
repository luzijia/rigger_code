#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs
import db
import ConfigParser
import re
from jinja2 import Template

class core:
    db=''
    tpl_config=[]
    cf=''

    @staticmethod
    def init(filename):
        try:
            core.cf = ConfigParser.ConfigParser()

            core.cf.read(filename)

            for l in core.cf.sections():
                m = re.search(r'TPL::(.*)',l,re.I|re.MULTILINE)
                if m:
                    if m.group(1):
                        core.tpl_config.append(m.group(0))

            host=core.cf.get("MYSQL","host")
            user=core.cf.get("MYSQL","user")
            port=int(core.cf.get("MYSQL","port"))
            passwd=core.cf.get("MYSQL","passwd")
            dbname=core.cf.get("MYSQL","db")

            core.db = db.MyDb(host,port,user,passwd,dbname)
        except Exception,e:
            print e

    @staticmethod
    def run():
        for c in  core.tpl_config:
            tablename =  core.cf.get(c,"tablename")
            tpl       =  core.cf.get(c,"tpl")
            output_dir=  core.cf.get(c,"output_dir")
            core.gorun(tablename,tpl,output_dir)

    @staticmethod
    def gorun(tablename,tpl,output_dir):
        tpl_content = codecs.open(tpl).read()

        sql='show create table %s' %(tablename)
        struct=core.db.fetchone(sql)

        if(len(struct[1])==0):
            raise Exception("can't fetch table:%s"%(tablename))

        m = re.findall(r"PRIMARY KEY \(`(.*?)`\).*?", struct[1])
        if(len(m)==0):
            raise Exception("can't get PRIMARY_KEY of table:%s"%(tablename))

        pk = m[0]

        fields      =  core.utilFields(tablename)

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

        tpl_content = codecs.open(tpl).read()

        template    = Template(tpl_content)
        tpl_content=template.render(tablename=tablename,pk=pk,fields_cond=fields_cond,fields_bind=fields_bind,fields_cond_val=fields_cond_val)

        core.writeTplContent(tpl_content,tablename,output_dir)


    @staticmethod
    def utilFields(tablename):
        sql='SHOW FIELDS FROM %s' %(tablename)
        fields=core.db.fetchall(sql)
        fields_used = []
        for field in fields:
            if(field[3]!='PRI'):
                fields_used.append(field[0])

        return fields_used

    @staticmethod
    def writeTplContent(tpl_content,tablename,output):
        output_file = "%s/%s.php"%(output,tablename)

        output      = codecs.open(output_file,"w")
        output.write(tpl_content)

        print "file write into %s" %(output_file)


