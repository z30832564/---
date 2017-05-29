# -*- coding: utf-8 -*-
from weibo import APIClient
import webbrowser
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
import io
import json
import csv
import exceptions
import numpy as np
import urllib2

APP_KEY = '3742916737'
APP_SECRET = 'ac696deb0ed0ddba7d311adcb0842ecf'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
# 利用官方SDK
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
# 得到授权页面的url，用webbrowser打开
url = client.get_authorize_url()
print url
webbrowser.open_new(url)

print '输入url中code后面的内容后按回车键：'
code = raw_input()
# code = your.web.framework.request.get('code')
# client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
r = client.request_access_token(code)
access_token = r.access_token  #  新浪返回的token，类似abc123xyz456  
expires_in = r.expires_in

client.set_access_token(access_token, expires_in)


'''
key = [ '机场', '站', '港', '站', '站', '站', '站',
       '发', '洗', '银行', '银行', '油', '气', '气', '车',
      '医院', '宾馆', '站', '药店', '区', '楼', '区', '院', '局',
       '政府', '所', '校', '学', '店', '店', '馆', '园', '公司']
cate = ['19,21', '19,22', '19,34', '19,35', '19,36', '19,37', '19,38',
        '19,148', '19,149', '19,150', '19,152', '19,153', '19,154', '19,155', '19',
        '19', '19', '19,267', '19,669', '44,45', '44,46', '44,47', '44,608', '44,609',
        '44,617', '44', '51', '51', '64', '115', '169', '194', '258']

for q in range(31, len(key)-1):
    print q
    print key[q]
    print cate[q]
    '''
fout_poi = io.open('test2', 'wb')
res_poi = client.place.pois.search.get(keyword='集团', category='258', page=10, count=50)
a = json.dumps(res_poi, ensure_ascii=False, indent=2)
fout_poi.write(a)

# 从test中解析出poiids和类别放到poiis.csv中

file = open("test2", 'r')
json_string = file.read()

json_dict = json.loads(json_string)

poi = []
category = []
lat = []
lon = []

json_dict = json.loads(json_string)
for i in json_dict.get("pois"):
    category.append(i.get("category_name"))
    poi.append(i.get("poiid"))
    lat.append(i.get("lat"))
    lon.append(i.get("lon"))
print poi
print category
print lat
print lon

# 打开存放结果的文件    file_clear_result
file_clear_result = open('result5.csv', 'a')


# 开始循环
for i in range(0, len(poi) - 1, 1):

    res_poi = client.place.pois.users.get(poiid=poi[i], count=50)
    file_weibo = io.open('weibo', 'w', encoding='utf-8')
    print res_poi
    print type(res_poi),len(res_poi)

    a = json.dumps(res_poi, ensure_ascii=False, indent=2)
    try:
        file_weibo.write(a)

        #file_weibo.close()
        print type(res_poi)
        print res_poi
        print i
        print category[i]
        json_clear = open('weibo')
        #res_poi = json_clear.read()
        try:
            json_dict_clear = json.load(json_clear)
        except ValueError:
            pass
        print type(json_dict_clear)
        for p in json_dict_clear.get('users'):
            file_clear_result.write(str(p.get('id')) + ','
                                    + str(p.get('checkin_at')) + ','
                                    + str(p.get('city')) + ','
                                    + str(p.get('gender')) + ','
                                    + str(p.get('bi_followers_count')) + ','
                                    + str(p.get('friends_count')) + ','
                                    + str(p.get('star')) + ','
                                    + str(p.get('online_status')) + ','
                                    + str(p.get('block_word')) + ','
                                    + str(p.get('statuses_count')) + ','
                                    + str(p.get('verified')) + ','
                                    + str(p.get('block_app')) + ','
                                    + str(p.get('followers_count')) + ','
                                    + str(p.get('avatargj_id')) + ','
                                    + str(p.get('source_type')) + ','
                                    + str(p.get('allow_all_comment')) + ','
                                    + str(p.get('geo_enabled')) + ','
                                    + str(p.get('class')) + ','
                                    + str(p.get('remark')) + ','
                                    + str(p.get('favourites_count')) + ','
                                    + str(p.get('province')) + ','
                                    + str(p.get('created_at')) + ','
                                    + str(p.get('user_ability')) + ','
                                    + str(p.get('verified_type')) + ','
                                    + str(p.get('pagefriends_count')) + ','
                                    + str(p.get('urank')) + ','
                                    + str(p.get('status').get('in_reply_to_status_id')) + ','
                                    + str(p.get('status').get('in_reply_to_screen_name')) + ','
                                    + str(p.get('status').get('in_reply_to_user_id')) + ','
                                    + str(p.get('status').get('source_allowclick')) + ','
                                    + str(p.get('status').get('isLongText')) + ','
                                    + str(p.get('status').get('created_at')) + ','
                                    + str(p.get('status').get('comments_count')) + ','
                                    + str(category[i].encode('utf-8')) + '\n')
    except TypeError:
        pass
    except AttributeError:
        pass

