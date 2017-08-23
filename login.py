#! /usr/bin/env python
# coding:utf-8


import urllib.request
from http.cookiejar import CookieJar
import loginbase


class LoginObj(object):
    def __init__(self):
        cj = CookieJar()  # 创建cookie对象
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  # 创建cookie处理程序、创建opener

    def response_oa(self):
        data = {"STAFFID": "002122", "PWD": "Liqy2122", "v_code": ""}  # 用户名密码
        url = "http://192.168.1.9:8081/oa/LoginCheck"
        req = loginbase.LoginBase.res_obj(url, data)
        html = self.opener.open(req).read().decode('gbk')

        list_data = {"pageSize": "20",
                     "pageNum:": "1",
                     "notify_type_id": "0",
                     "search_his": "0",
                     "author": "",
                     "title	": "",
                     "begin_time": "",
                     "end_time	": ""}
        list_url = "http://192.168.1.9:8081/oa/announcement/announcement_list_qry.jsp"
        req_list =  loginbase.LoginBase.res_obj(list_url, list_data)
        html_list = self.opener.open(req_list).read().decode('utf-8')
        return html, html_list



