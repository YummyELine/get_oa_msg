 #! /usr/bin/env python
# coding:utf-8
import database
import send_mail

class SendMailPending(object):
    @staticmethod
    def send(p_data):
        cx = database.SqlConnect.conn()
        cur = cx.cursor()
        mail_datas = cur.execute("""select process_type, process_id, process_title, create_man, create_date, process_node from pending where process_id in (?)""", p_data)
        pending_len = len(mail_datas.fetchall())
        for i, mail_data in enumerate(mail_datas):


