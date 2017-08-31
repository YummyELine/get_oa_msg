import sqlite3


class SqlConnect(object):
    @staticmethod
    def conn():
        return sqlite3.connect("oa.sqlite3")