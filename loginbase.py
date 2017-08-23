#! /usr/bin/env python
# coding:utf-8
import urllib.request


class LoginBase(object):
    @staticmethod
    def res_obj(url, post_data):
        p_data = urllib.parse.urlencode(post_data).encode('utf-8') # 对data进行url编码
        req = urllib.request.Request(url, p_data)
        return req
