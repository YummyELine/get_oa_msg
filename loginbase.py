#! /usr/bin/env python
# coding:utf-8
import urllib.request


class LoginBase(object):
    @staticmethod
    def res_obj(*args):
        if len(args) == 2:
            p_data = urllib.parse.urlencode(args[1]).encode('utf-8')  # 对data进行url编码
            req = urllib.request.Request(args[0], p_data)
        elif len(args) == 1:
            req = urllib.request.Request(args[0])
        else:
            req = None
        return req



