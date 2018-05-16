# -*- coding: utf-8 -*-
import DbHelper
import pinyin

db = DbHelper.DbHelper('192.168.0.128', 'root', 'root', 'python')


def initialStr(val):
    if isinstance(val, str):
        if val == 'None':
            return ''
        else:
            return pinyin.get(val)
    else:
        return "类型不对"


def city(res):
    return res[1]


sql = "select * from cms_areas2"
result = db.execute(sql).select()

for val in result:
    cityName = city(val)
    print(cityName)
    initial = initialStr(cityName)[0:1]
    print(val[0])
    sql = "update `cms_areas2` set `initial` = '%s' where `id` = %d" % (initial, val[0])
    db.execute(sql).update()
db.close()
