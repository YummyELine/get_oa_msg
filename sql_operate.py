import database
import datetime


class SqlOperate(object):
    @staticmethod
    def insert_pending(pending_lists):
        insert_time = datetime.datetime.now()
        cx = database.SqlConnect.conn()
        cx.execute("""delete from pending where (julianday(?)-julianday(insert_time))*24*60 >= 60""",(insert_time,))
        cx.commit()
        cx.close()
        tuple_lists = []
        for pending_list in pending_lists:
            cx = database.SqlConnect.conn()
            cur = cx.cursor()
            if_inserts = cur.execute("""select process_id from pending where process_id = ?""", (pending_list['process_id'],))
            if len(if_inserts.fetchall()) == 0:
                cx.execute("""insert into pending(process_type, process_id, process_title, create_man, create_date, process_node, insert_time) 
                values (?, ?, ?, ?, ?, ?, ?) """, (
                pending_list['process_type'], pending_list['process_id'], pending_list['process_title'],
                pending_list['create_man'], pending_list['create_date'], pending_list['process_node'], insert_time))
                cx.commit()
                tuple_lists.append(pending_list['process_id'])
            cur.close()
            cx.close()
        tuple_lists = tuple(tuple_lists)
        return tuple_lists

    @staticmethod
    def insert_notice(list_datas):
        rt_lists = []
        for list_data in list_datas:
            cx = database.SqlConnect.conn()
            cur = cx.cursor()
            if_inserts = cur.execute("""select html_id from notice where html_id = ?""",
                                     (list_data['html_id'],))
            if len(if_inserts.fetchall()) == 0:
                cx.execute("""insert into notice(title, html, html_id, key_word) 
                                values (?, ?, ?, ?) """, (
                    list_data['title'], list_data['html'], list_data['html_id'],
                    list_data['key_word']))
                cx.commit()
                rt_lists.append(list_data)
            cur.close()
            cx.close()
        sql = "delete from notice where html_id not in ("
        for i, ss in enumerate(list_datas):
            if i == 0:
                sql += "'"+ss['html_id']+"'"
            else:
                sql += ", '"+ ss['html_id']+"'"
        sql += ')'
        cx = database.SqlConnect.conn()
        cx.execute(sql)
        cx.commit()
        cx.close()
        # 返回将要发邮件的数据
        return rt_lists
        # print(list_data)
