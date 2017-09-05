 #! /usr/bin/env python
# coding:utf-8
import database
import send_mail
import urllib.request
from http.cookiejar import CookieJar
import loginbase
from bs4 import BeautifulSoup
import re

class SendMailNotice(object):
    @staticmethod
    def send(opener, p_datas):
        for p_data in p_datas:
            if p_data['key_word'] == '施冬荣' or p_data['key_word'] == '吴艳':
                header_t = 'OA关注人员动向'
            elif p_data['key_word'] == '早会':
                header_t = 'OA早会提醒'
            elif p_data['key_word'] == '放假':
                header_t = 'OA放假通知'
            else:
                header_t = 'OA通知相关'
            title = '标题：'+str(p_data['title'])+'；发布人：'+str(p_data['send_man'])+';发布时间：'+str(p_data['send_time'])+';是否置顶：'+str(p_data['if_top'])
            content_req = loginbase.LoginBase.res_obj(p_data['html'])
            content = opener.open(content_req).read().decode('gbk')
            soup = BeautifulSoup(content, 'html.parser')
            a_labels = soup.find_all('a')
            annexs_htmls =[]
            for a_label in a_labels:
                annexs_k = {}
                a_h = re.search(r'doc_id=',a_label.get('href'))
                if a_h is not None:
                    a_html='http://192.168.1.9:8081'+a_label.get('href')
                    annexs_k['html'] = a_html
                    annexs_k['filename'] = a_label.get_text()
                    annexs_htmls.append(annexs_k)
            annexs = []
            for annexs_html in annexs_htmls:
                annex_rt = {}
                annex_req = loginbase.LoginBase.res_obj(annexs_html['html'])
                annex_rt['annex'] = opener.open(annex_req).read()
                annex_rt['filename'] = annexs_html['filename']
                annexs.append(annex_rt)
            is_pending = 0
            send_mail.SendMail.send_mail(title, content, is_pending, header_t, annexs)


