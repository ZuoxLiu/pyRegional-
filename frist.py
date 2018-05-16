# -*- coding: utf-8 -*-
import requests
import DbHelper
import logging

cityData = requests.get("http://res.42du.cn/static/json/region/prov-town.json")

logger = logging.getLogger('baseSpider')
logger.setLevel(logging.INFO)
db = DbHelper.DbHelper('192.168.0.128', 'root', 'root', 'python')
try:
    cityJson = cityData.json()
except:
    print('ValueError:', "没有json数据")


def stringToList(str):
    return str.split(":")


for city in cityJson:
    lCity = stringToList(city)
    cityNum = lCity[0]
    cityStr = lCity[1]
    if len(cityNum) == 2:
        sql = '''
                 insert into `cms_areas2`(`id`,`name`,`pid`,`depth`) values (%d,'%s',%d,%d)
              ''' % (int(cityNum), cityStr, 0, 1)
        db.execute(sql).save()
    elif len(cityNum) == 4:
        pid = cityNum[0:2]
        print(pid)
        sql = '''
                insert into `cms_areas2`(`id`,`name`,`pid`,`depth`) values (%d,'%s',%d,%d)
              ''' % (int(cityNum), cityStr, int(pid), 2)
        db.execute(sql).save()
    elif len(cityNum) == 6:
        pid = cityNum[0:4]
        print(pid)
        sql = '''
            insert into `cms_areas2`(`id`,`name`,`pid`,`depth`) values (%d,'%s',%d,%d)
        ''' % (int(cityNum), cityStr, int(pid), 3)
        db.execute(sql).save()
db.close()

print('success')
