 #! /usr/bin/env python
# coding:utf-8
import login
import html_parser
import sql_operate
import send_mail_pending
import notice_filter
import send_mail_notice
import urllib.request
from http.cookiejar import CookieJar
import loginbase
import datetime
import time


class OaMain(object):
    def __init__(self):
        cj = CookieJar()  # 创建cookie对象
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  # 创建cookie处理程序、创建opener

    def mian(self):
        # 登录获取网页的代码
        html,htmllist = login.LoginObj.response_oa(self.opener)

        # 爬取需要的数据
        main_list = html_parser.HtmlParser(html).main_parse()

        # 将数据写入的数据库，并将过期的数据删除
        pending_lists = sql_operate.SqlOperate.insert_pending(main_list)

        # 判断是否有需要发邮件的数据，如果有的话将发送邮件
        if len(pending_lists) != 0:
            send_mail_pending.SendMailPending.send(pending_lists)

        # BS提取出网页的数据
        list_data = html_parser.HtmlParser(htmllist).list_parse()

        # RE将需要的数据筛选出来
        will_send_notice = notice_filter.NoticeFilter.filter(list_data)

        # 将数据插入数据库，这样就可以判断这条通知之前是否已经发过邮件
        notice_list = sql_operate.SqlOperate.insert_notice(will_send_notice)

        # 判断是否有需要发邮件的数据，如果有的话将发送邮件
        if len(will_send_notice) != 0:
            send_mail_notice.SendMailNotice.send(self.opener, notice_list)


if __name__ == '__main__':
    time1 = datetime.datetime.now()
    runTimes = time.strptime(str(time1), "%Y-%m-%d %H:%M:%S.%f")
    i = 0
    gTime = None
    for runTime in runTimes:
        if i == 3:
            gTime = runTime
            break
        i += 1

    if 8 <= gTime <= 21:
        OM = OaMain()
        OM.mian()
