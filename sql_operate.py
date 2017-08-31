import database
import datetime


class SqlOperate(object):
    @staticmethod
    def insert_pending(pending_data):
        cx = database.SqlConnect.conn()
