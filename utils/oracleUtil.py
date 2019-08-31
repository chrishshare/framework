# -*- coding: UTF8 -*-
import cx_Oracle
from utils.configUtil import GetConfig
from utils.logUtil import InitLogging


class OralceUtil:
    def __init__(self):
        """
        初始化连接串，并连接oracle
        """
        self.logger = InitLogging().init_logging()
        self._username = GetConfig(section='oracle', option='username').get_section_value()
        self._password = GetConfig(section='oracle', option='password').get_section_value()
        self._connstr = GetConfig(section='oracle', option='connstr').get_section_value()
        self._conn = cx_Oracle.connect(self._username, self._password, self._connstr)
        self._cursor = self._conn.cursor()

    def query_sql_with_sql(self, sql):
        """
        执行不带参数的sql
        :param sql:
        :return:
        """
        result = self._cursor.execute(sql)
        self._close_connect()
        return result.fetchall()

    def query_sql_with_param(self, sql, param):
        """
        执行带参数的sql
        :param sql:
        :param param:
        :return:
        """
        result = self._cursor.execute(sql, param)
        self._close_connect()
        return result.fetchall()

    def update_and_insert_sql_with_sql(self, sql):
        """
        执行带参数的sql
        :param sql:
        :param param:
        :return:
        """
        try:
            self._cursor.execute(sql)
            self._conn.commit()
            self._close_connect()
        except Exception as e:
            self.logger.error(e)

    def update_and_insert_sql_with_param(self, sql, param):
        """
        执行带参数的sql
        :param sql:
        :param param:
        :return:
        """
        try:
            self._cursor.execute(sql, param)
            self._conn.commit()
            self._close_connect()
        except Exception as e:
            self.logger.error(e)

    def _close_connect(self):
        """
        关闭连接，查询时需要，插入、更新不需要
        :return:
        """
        self._cursor.close()
        self._conn.close()

if __name__ == '__main__':
    sql = """select * from user$"""
    print(OralceUtil().query_sql_with_sql(sql=sql))





