#! /usr/bin/env python
# coding:utf-8
import login


class OaMain(object):
    def __init__(self):
        self.login_main = login.LoginObj()

    def mian(self):
        html,htmllist = self.login_main.response_oa()
        print(html.read())
        print(htmllist.read().decode('utf-8'))


if __name__ == '__main__':
    OM = OaMain()
    OM.mian()
