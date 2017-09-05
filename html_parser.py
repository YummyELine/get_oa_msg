 #!/usr/bin/env python
# coding:utf-8
import datetime
import time
from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def __init__(self, html_code):
        if html_code is None:
            return
        self.soup = BeautifulSoup(html_code, 'html.parser')

    def main_parse(self):
        main_list = []
        tos = self.soup.find_all('tr', class_='odd')
        for to in tos:
            main_data = {}
            bes = to.find_all('td')
            for i, be in enumerate(bes):
                if (i + 1) % 6 == 1:
                    main_data['process_type'] = be.get_text()
                elif (i + 1) % 6 == 2:
                    main_data['process_id'] = be.get_text()
                elif (i + 1) % 6 == 3:
                    main_data['process_title'] = be.get_text()
                elif (i + 1) % 6 == 4:
                    main_data['create_man'] = be.get_text()
                elif (i + 1) % 6 == 5:
                    main_data['create_date'] = be.get_text()
                elif (i + 1) % 6 == 0:
                    main_data['process_node'] = be.get_text()
            main_list.append(main_data)
        return main_list

    def list_parse(self):
        trs = self.soup.find_all('tr')
        list_tr = []
        list_td = []
        rt_data = []
        for i, tr in enumerate(trs):
            if i > 1:
                notice = {}
                result = re.search(r'''id=\d+''', str(tr)).group()
                html_address = 'http://192.168.1.9:8081/oa/NotifyContent?notify_'+result
                notice["id"] = result
                notice["html"] = html_address
                list_tr.append(notice)
        tds = self.soup.find_all('td')
        for i, td in enumerate(tds):
            if i % 6 == 0:
                notice_data = {}
            if i % 6 == 1:
                notice_data["type"] = td.get_text()
            if i % 6 == 2:
                notice_data["send_time"] = td.get_text()
            if i % 6 == 3:
                notice_data["send_man"] = td.get_text()
            if i % 6 == 4:
                notice_data["title"] = td.get_text()
            if i % 6 == 5:
                notice_data["if_top"] = td.get_text()
                list_td.append(notice_data)
        loop_time = len(list_tr)
        for i in range(loop_time):
            title_html = {}
            title_html["type"] = list_td[i]['type']
            title_html["send_time"] = list_td[i]['send_time']
            title_html["send_man"] = list_td[i]['send_man']
            title_html["if_top"] = list_td[i]['if_top']
            title_html["title"] = list_td[i]["title"]
            title_html["html"] = list_tr[i]["html"]
            title_html["html_id"] = list_tr[i]["id"]
            rt_data.append(title_html)
        return rt_data


