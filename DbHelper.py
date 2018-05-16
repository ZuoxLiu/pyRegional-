# -*- coding: utf-8 -*-
import pymysql

'db module'
__author__ = 'liuzuoxian'


class DbHelper(object):
    def __init__(self, host='127.0.0.1', user='root', password="",
                 database=None, port=3306):
        self.database = database
        self.port = port
        self.host = host
        self.user = user
        self.password = password
        self.conn = None
        self.cur = None
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database, self.port, charset="utf8")
        self.cur = self.conn.cursor()
        return self

    def execute(self, sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            raise e
        return self

    def save(self):
        try:
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()

    def update(self):
        self.save()

    def select(self):
        try:
            result = self.cur.fetchall()
        except Exception as e:
            raise e
        finally:
            self.conn.close()
        return result

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = DbHelper('192.168.0.128', 'root', 'root', 'python')
    db.execute("select * from cms_areas").select()
