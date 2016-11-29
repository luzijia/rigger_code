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

    '''
    制造Model
    '''
    @staticmethod
    def runmodel(table_name):
        try:
            model_tpl=myConfigParser.myConfigParser.get("TPL","model")
            print "runmodel:%s"%(table_name)
            tpl_content = codecs.open(model_tpl).read()
            sql='show create table %s' %(table_name)
            struct=core.db.fetchone(sql)

            if(len(struct[1])==0):
                raise Exception("can't fetch table:%s"%(table_name))

            m = re.findall(r"PRIMARY KEY \(`(.*?)`\).*?", struct[1])
            if(len(m)==0):
                raise Exception("can't get PRIMARY_KEY of table:%s"%(table_name))

            pk = m[0]

            #update字符匹配
            sql='SHOW FIELDS FROM %s' %(table_name)
            fields=core.db.fetchall(sql)
            fields_used     = []
            fields_used_val =  []
            for field in fields:
                if(field[3]!='PRI'):
                    field_msg = '%s=?'%(field[0])
                    fields_used.append(field_msg)
                    field_msg = '$%s'%(field[0])
                    fields_used_val.append(field_msg)

            tpl_content =  re.sub(r'##tablename', table_name, tpl_content)
            tpl_content =  re.sub(r'##pk',pk,tpl_content)
            tpl_content =  re.sub(r'##update_cond_str',",".join(fields_used),tpl_content)
            tpl_content =  re.sub(r'##update_val_str',",".join(fields_used_val),tpl_content)

            output      = model_tpl=myConfigParser.myConfigParser.get("TPL","output_model")
            output      = re.sub(r'model',table_name,output)
            core.writeTplContent(tpl_content,output)
        except Exception,e:
            print e

    @staticmethod
    def writeTplContent(tpl_content,output_file):
        output = codecs.open(output_file,"w")
        output.write(tpl_content)
        print "file write into %s" %(output_file)



