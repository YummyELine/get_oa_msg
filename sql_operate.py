import database
import datetime


class SqlOperate(object):
    @staticmethod
    def insert_pending(pending_lists):
        tuple_lists = []
        for pending_list in pending_lists:
            cx = database.SqlConnect.conn()
            cur = cx.cursor()
            if_inserts = cur.execute("""select process_id from pending where process_id = ?""", (pending_list['process_id'],))
            if len(if_inserts.fetchall()) == 0:
                cx.execute("""insert into pending(process_type, process_id, process_title, create_man, create_date, process_node) 
                values (?, ?, ?, ?, ?, ?) """, (
                pending_list['process_type'], pending_list['process_id'], pending_list['process_title'],
                pending_list['create_man'], pending_list['create_date'], pending_list['process_node']))
                cx.commit()
                tuple_lists.append(pending_list['process_id'])
            cur.close()
            cx.close()
        tuple_lists = tuple(tuple_lists)
        return tuple_lists
