 #! /usr/bin/env python
# coding:utf-8
import database
import send_mail

class SendMailPending(object):
    @staticmethod
    def send(p_data):
        cx = database.SqlConnect.conn()
        cur = cx.cursor()
        p_d = []
        for pd in p_data:
            p_d.append(str(pd))
        p_dstr = tuple(p_d)
        if len(p_data)==1:
            sql = """SELECT process_type, process_id, process_title, create_man, create_date, process_node 
FROM pending WHERE process_id IN (?)"""
        else:
            sql = """SELECT process_type, process_id, process_title, create_man, create_date, process_node 
FROM pending WHERE process_id IN (?{0})""".format(',?'*(len(p_data)-1))
        mail_datass = cur.execute(sql, p_dstr)
        mail_ds = mail_datass.fetchall()
        pending_len = len(mail_ds)
        title = "您当前有"+str(pending_len)+"条未处理的流程，请及时处理。"
        content = "<h1>您当前有"+str(pending_len)+"条未处理的流程，请及时处理。</h1>"+"""
        <table><thead><tr>
        <th>流程类型</th>
        <th>流程ID</th>
        <th>事物标题</th>
        <th>派单人员</th>
        <th>派单日期</th>
        <th>当前环节</th>
        </tr>
        </thead>
        <tbody>"""
        for mail_datas in mail_ds:
            content += "<tr>"
            for i, mail_data in enumerate(mail_datas):
                if i % 6 == 5:
                    content += "<td>"+str(mail_data)+"</td></tr>"
                else:
                    content += "<td>" + str(mail_data) + "</td>"
        content +="</tbody></table>"
        is_pending = 1
        send_mail.SendMail.send_mail(title, content, is_pending)
        cur.close()
        cx.close()


