#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DOMAIN = 'http://test.airpost.in'
mysql_host = '127.0.0.1'
mysql_database = 'basement'
mysql_username = 'root'
mysql_password = ''
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s?charset=utf8' % (
	mysql_username, mysql_password, mysql_host, mysql_database)
SECRET_KEY = '\xb9\xed|\xad<\x9fbx\x93\xf7^l\xee\xf6@M\xa1k\x86\x12\x18\xf3>\x0e'
CSRF_ENABLED = True
DEBUG = True
UPLOADS_DEFAULT_DEST = os.path.join(os.getcwd(), 'basement/static/uploads')
UPLOADS_DEFAULT_URL = DOMAIN + '/uploads/'

UPLOADED_AVATARS_ALLOW = set(['jpg', 'gif', 'jpeg', 'png'])

CITIES = {
u'香港':150,
u'安康':151,
u'阿克苏':152,
u'安庆':153,
u'安阳':154,
u'包头':155,
u'北海':156,
u'昌都':157,
u'保山':158,
u'广州':159,
u'常德':160,
u'郑州':161,
u'长春':162,
u'朝阳':163,
u'酒泉':164,
u'赤峰':165,
u'长治':166,
u'重庆':167,
u'长海':168,
u'长沙':169,
u'成都':170,
u'常州':171,
u'大同':172,
u'达州':173,
u'丹东':174,
u'香格里拉':175,
u'大连':176,
u'大理':177,
u'敦煌':178,
u'东营':179,
u'张家界':180,
u'恩施':181,
u'延安':182,
u'阜阳':183,
u'福州':184,
u'富蕴':185,
u'广汉':186,
u'格尔木':187,
u'海口':188,
u'黑河':189,
u'呼和浩特':190,
u'合肥':191,
u'杭州':192,
u'怀化':193,
u'淮安':194,
u'海拉尔':195,
u'乌兰浩特':196,
u'哈密':197,
u'衡阳':198,
u'哈尔滨':199,
u'舟山':200,
u'和田':201,
u'黄岩':202,
u'汉中':203,
u'银川':204,
u'且末':205,
u'庆阳':206,
u'景德镇':207,
u'嘉峪关':208,
u'井冈山':209,
u'西双版纳':210,
u'吉林':211,
u'九江':212,
u'泉州':213,
u'佳木斯':214,
u'锦州':215,
u'衢州':216,
u'九寨沟':217,
u'库车':218,
u'喀什':219,
u'南昌':220,
u'昆明':221,
u'赣州':222,
u'库尔勒':223,
u'克拉玛依':224,
u'贵阳':225,
u'桂林':226,
u'连城':227,
u'兰州':228,
u'丽江':229,
u'临沧':230,
u'潞西':231,
u'拉萨':232,
u'洛阳':233,
u'连云港':234,
u'临沂':235,
u'柳州':236,
u'泸州':237,
u'牡丹江':238,
u'绵阳':239,
u'梅州':240,
u'南充':241,
u'北京':242,
u'齐齐哈尔':243,
u'宁波':244,
u'南京':245,
u'南宁':246,
u'南阳':247,
u'南通':248,
u'北京':249,
u'上海':250,
u'攀枝花':251,
u'巴彦淖尔':252,
u'上海':253,
u'沈阳':254,
u'山海关':255,
u'荆州':256,
u'石家庄':257,
u'汕头':258,
u'思茅':259,
u'三亚':260,
u'深圳':261,
u'青岛':262,
u'塔城':263,
u'铜仁':264,
u'通辽':265,
u'济南':266,
u'通化':267,
u'天津':268,
u'黄山':269,
u'太原':270,
u'乌鲁木齐':271,
u'榆林':272,
u'潍坊':273,
u'威海':274,
u'温州':275,
u'乌海':276,
u'武汉':277,
u'武夷山':278,
u'无锡':279,
u'梧州':280,
u'万县':281,
u'襄樊':282,
u'西昌':283,
u'锡林浩特':284,
u'西安':285,
u'厦门':286,
u'西宁':287,
u'徐州':288,
u'宜宾':289,
u'盐城':290,
u'宜昌':291,
u'伊宁':292,
u'义乌':293,
u'延吉':294,
u'烟台':295,
u'昭通':296,
u'湛江':297,
u'珠海':298,
u'遵义':299,
}
