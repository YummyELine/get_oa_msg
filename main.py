 #! /usr/bin/env python
# coding:utf-8
import login
import html_parser
import sql_operate
import send_mail_pending


class OaMain(object):
    def __init__(self):
        self.login_main = login.LoginObj()

    def mian(self):
        html,htmllist = self.login_main.response_oa()
        main_list = html_parser.HtmlParser(html).main_parse()
        pending_lists = sql_operate.SqlOperate.insert_pending(main_list)
        if len(pending_lists) != 0:
            send_mail_pending.SendMailPending.send(pending_lists)

        # list_data = html_parser.HtmlParser(htmllist).list_parse()




if __name__ == '__main__':
    OM = OaMain()
    OM.mian()
