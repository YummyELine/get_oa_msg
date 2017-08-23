#! /usr/bin/env python
# coding:utf-8


import urllib.request
from http.cookiejar import CookieJar


class LoginObj(object):
    def __init__(self):
        data = {"STAFFID": "002122", "PWD": "Liqy2122", "v_code": ""}  # 用户名密码
        self.post_data = urllib.parse.urlencode(data).encode('utf-8')  # 对data进行url编码
        list_data = {"pageSize": "20",
                     "pageNum:": "1",
                     "notify_type_id": "0",
                     "search_his": "0",
                     "author": "",
                     "title	": "",
                     "begin_time": "",
                     "end_time	": ""}
        self.post_list = urllib.parse.urlencode(list_data).encode('utf-8')

    def response_oa(self):
        cj = CookieJar()  # 创建cookie对象
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  # 创建cookie处理程序、创建opener
        req = urllib.request.Request("http://192.168.1.9:8081/oa/LoginCheck", self.post_data)  # 这是提交表单URL
        content = opener.open(req)
        html = content
        req_list = urllib.request.Request("http://192.168.1.9:8081/oa/announcement/announcement_list_qry.jsp", self.post_list)
        content_list = opener.open(req_list)
        html_list = content_list
        # print(html_list.decode('utf-8'))
        return html, html_list


