 #! /usr/bin/env python
# coding:utf-8
import login
import html_parser
import sql_operate


class OaMain(object):
    def __init__(self):
        self.login_main = login.LoginObj()

    def mian(self):
        html,htmllist = self.login_main.response_oa()
        main_data = html_parser.HtmlParser(html).main_parse()
        sql_operate.SqlOperate.insert_pending(main_data)
        # list_data = html_parser.HtmlParser(htmllist).list_parse()

        print(main_data)


if __name__ == '__main__':
    OM = OaMain()
    OM.mian()
