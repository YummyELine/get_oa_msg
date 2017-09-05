import sqlite3


class SqlConnect(object):
    @staticmethod
    def conn():
        return sqlite3.connect("D:\\PY\\untitled1_OA\\oa.sqlite3")