# -*- coding: utf-8 -*-
import DbHelper
import requests

key = "f0248792dea6aacac56146e3681f16f0"

url = "http://restapi.amap.com/v3/geocode/geo?"

db = DbHelper.DbHelper('192.168.0.128', 'root', 'root', 'python')
dicts = {
    'key': key
}

result = db.execute('select * from cms_areas2 limit 3600,200').select()


def getParams(dicts):
    if isinstance(dicts, dict):
        s = ''
        for k, v in dicts.items():
            if len(s) < 1:
                s += "%s=%s" % (k, v)
            else:
                s += "&%s=%s" % (k, v)
        return s
    else:
        return ''


def getLocation(dicts):
    geocodes = dicts['geocodes'][0]['location']
    longitude = geocodes.split(',')[0]
    latitude = geocodes.split(',')[1]
    return (longitude, latitude)


def getName(aid):
    aid = int(aid)
    sql = "select * from `cms_areas2` where `id` = %d" % (aid)
    resp = db.execute(sql).select()
    if resp:
        res = resp[0]
        return getName(res[3]) + res[1]
    else:
        return ''


def getResp(url):
    r0 = requests.get(url).json()
    if int(r0['status']) == 1:
        return getLocation(r0)
    else:
        return ''


for res in result:
    dicts['address'] = getName(res[0])
    params = getParams(dicts)
    urls = url + params
    location = getResp(urls)
    sql = "update `cms_areas2` set `longitude` = %s , `latitude` = %s where `id` = %d" % (
        location[0], location[1], int(res[0]))
    print(sql)
    db.execute(sql).update()
db.close()