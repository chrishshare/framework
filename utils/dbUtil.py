# -*- coding: UTF8 -*-
import cx_Oracle
from utils.logUtil import InitLogging
from utils.yamlParser import YamlParser
import MySQLdb
import sqlite3


class dbUtil:
    def __init__(self):
        """
        初始化连接串，并连接oracle
        """
        self._logger = InitLogging().init_logging()
        self._yaml = YamlParser().parser_common_conf(cf='projectConfig.yaml')
        self._dbinfo = self._yaml.get(self._yaml.get('project')).get('dbinfo')
        self._dbtype = self._dbinfo.get('type')
        self._username = self._dbinfo.get('username')
        self._password = self._dbinfo.get('password')
        self._database = self._dbinfo.get('database')
        self._dbfile = self._dbinfo.get('dbfile')
        self._connstr = self._dbinfo.get('connectstr')
        self._port = self._dbinfo.get('port')

    def connect_database(self):
        """
        连接数据库
        :return:
        """
        conn = ''
        if 'oracle' == self._dbtype:
            conn = cx_Oracle.connect(self._username, self._password, self._connstr)
        elif 'mysql' == self._dbtype:
            conn = MySQLdb.connect(self._connstr, self._username, self._password, self._database)
        elif 'sqlite3' == self._dbtype:
            conn = sqlite3.connect(database=self._dbfile)
        elif 'hive' == self._dbtype:
            # 暂时没有实现
            self._logger.error('暂时没有实现')
            # db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8')
            # cursor = conn.cursor()
        else:
            self._logger.error('暂不支持该数据库类型')
        cursor = conn.cursor()
        return {'cursor': cursor, 'conn': conn}

    def query_sql_with_sql(self, sql):
        """
        执行不带参数的sql
        :param sql:
        :return:
        """
        result = self.connect_database().get('cursor').execute(sql)
        self._close_connect()
        return result.fetchall()

    def query_sql_with_param(self, sql, param):
        """
        执行带参数的sql
        :param sql:
        :param param:
        :return:
        """
        result = self.connect_database().get('cursor').execute(sql, param)
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
            self.connect_database().get('cursor').execute(sql)
            self.connect_database().get('conn').commit()
            self._close_connect()
        except Exception as e:
            self._logger.error(e)

    def update_and_insert_sql_with_param(self, sql, param):
        """
        执行带参数的sql
        :param sql:
        :param param:
        :return:
        """
        try:
            self.connect_database().get('cursor').execute(sql, param)
            self.connect_database().get('conn').commit()
            self._close_connect()
        except Exception as e:
            self._logger.error(e)

    def _close_connect(self):
        """
        关闭连接，查询时需要，插入、更新不需要
        :return:
        """
        self.connect_database().get('cursor').close()
        self.connect_database().get('conn').close()


if __name__ == '__main__':
    sql = """select * from auth_user"""
    print(dbUtil().query_sql_with_sql(sql=sql))





