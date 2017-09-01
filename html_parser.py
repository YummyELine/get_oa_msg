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

        main_data = self._get_main_data(soup)
        list_data = self._get_his_data(soup)
        return list_data

