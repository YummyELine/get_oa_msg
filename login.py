#! /usr/bin/env python
# coding:utf-8


import urllib.request
from http.cookiejar import CookieJar
import loginbase


class LoginObj(object):

    @staticmethod
    def response_oa(opener):
        data = {"STAFFID": "002122", "PWD": "Liqy2122", "v_code": ""}  # 用户名密码
        url = "http://192.168.1.9:8081/oa/LoginCheck"
        req = loginbase.LoginBase.res_obj(url, data)
        opener.open(req).read().decode('gbk')


        main_url = "http://192.168.1.9:8081/oa/PersonalFlowIndex"
        main_req = loginbase.LoginBase.res_obj(main_url)
        html = opener.open(main_req).read().decode('gbk')

        list_data = {"pageSize": "50",
                     "pageNum:": "1",
                     "notify_type_id": "0",
                     "search_his": "0",
                     "author": "",
                     "title	": "",
                     "begin_time": "",
                     "end_time	": ""}
        list_url = "http://192.168.1.9:8081/oa/announcement/announcement_list_qry.jsp"
        req_list = loginbase.LoginBase.res_obj(list_url, list_data)
        html_list = opener.open(req_list).read().decode('utf-8')
        return html, html_list



