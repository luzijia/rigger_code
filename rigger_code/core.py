#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs
import myConfigParser
import db
import re

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
    def runmodel(ures,ureplaces,table_name):
        print "runmodel:%s"%(table_name)
        tpl_content = core.modelinit(table_name)
        i=0;
        l=len(ures)
        while i < l:
            tpl_content = re.sub(ures[i],ureplaces[i],tpl_content)
            i+=1
        core.writeTplContent(tpl_content,table_name)

    #工具
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

    #model初始化操作：生成pk和table_name
    #返回替换后的模版文件
    @staticmethod
    def modelinit(table_name):
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

            tpl_content =  re.sub(r'##tablename', table_name, tpl_content)
            tpl_content =  re.sub(r'##pk',pk,tpl_content)

            return tpl_content

    @staticmethod
    def writeTplContent(tpl_content,table_name):
        output_file = re.sub(r'model',table_name,myConfigParser.myConfigParser.get("TPL","output_model"))
        output      = codecs.open(output_file,"w")
        output.write(tpl_content)
        print "file write into %s" %(output_file)



