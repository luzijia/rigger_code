#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

class MyDb:
    def __init__(self,host,port,user,passwd,db):
        try:
            self.db     = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db)
            self.cursor = self.db.cursor()
        except Exception,e:
            print e

    def fetchall(self,sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception,e:
            print e

    def fetchone(self,sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception,e:
            print e

    def execute(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit();
        except Exception,e:
            print e
    def __del__(self):
        self.close()

    def close(self):
        try:
            self.db.close()
            self.cursor.close()
        except Exception,e:
            print e
