 #! /usr/bin/env python
# coding:utf-8
import re


class NoticeFilter(object):
    @staticmethod
    def filter(notice_datas):
        filter_datas = ['通知', '公告', '早会', '吴艳', '施冬荣', '放假', '培训', '活动', '规范', '招聘', '通告']
        filter_rules = ''
        for i, filter_data in enumerate(filter_datas):
            if i == 0:
                filter_rules = filter_data
            else:
                filter_rules += "|" + filter_data
        rt_notice = []
        for notice_data in notice_datas:
            re_notices = re.search(filter_rules,notice_data['title'])
            if re_notices is not None:
                re_notice = re_notices.group()
                key_filter = {}
                key_filter['type'] = notice_data['type']
                key_filter['send_time'] = notice_data['send_time']
                key_filter['send_man'] = notice_data['send_man']
                key_filter['if_top'] = notice_data['if_top']
                key_filter['title'] = notice_data['title']
                key_filter['html'] = notice_data['html']
                key_filter['html_id'] = notice_data['html_id']
                key_filter['key_word'] = re_notice
                rt_notice.append(key_filter)
        return rt_notice
