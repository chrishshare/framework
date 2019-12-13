# -*- coding: UTF8 -*-
from utils.logUtil import InitLogging
from utils.yamlParser import YamlParser
import operator
import jaydebeapi as jdbc
from getrootdir import root_path
import os


class dbUtil:
    def __init__(self):
        """
        初始化连接串，并连接oracle
        """
        self._logger = InitLogging().init_logging()
        self._yaml = YamlParser().parser_common_conf(cf='projectConfig.yaml')
        self._dbinfo = self._yaml.get(self._yaml.get('project')).get('dbinfo')
        self._dbtype = self._dbinfo.get('type')
        self._username = self._yaml.get(self._dbtype).get('username')
        self._password = self._yaml.get(self._dbtype).get('password')
        # self._database = self._dbinfo.get('database')
        self._jdbcclass = self._yaml.get(self._dbtype).get('jdbcClass')
        self._jdbcurl = self._yaml.get(self._dbtype).get('jdbcurl')
        # self._dbfile = self._dbinfo.get('dbfile')
        # self._connstr = self._dbinfo.get('connectstr')
        # self._port = self._dbinfo.get('port')
        # jdbcClass: oracle.jdbc.driver.OracleDriver
        # jdbcurl: jdbc:oracle: thin:

    def connect_database(self):
        """
        连接数据库
        :return:
        """
        # jdbc驱动包路径
        lib_path = root_path + os.sep + 'libs' + os.sep
        conn = None
        cursor = None
        # 根据配置的不同数据库类型选择对应的驱动并初始化连接
        if operator.eq(self._dbtype, 'oralce'):
            conn = jdbc.connect(jclassname=self._jdbcclass, jars=lib_path + 'mysql-connector-java-8.0.16.jar',
                                url=self._jdbcurl, driver_args={'user': self._username, 'password': self._password})
            cursor = conn.cursor()
        if operator.eq(self._dbtype, 'mysql'):
            conn = jdbc.connect(jclassname=self._jdbcclass, url=self._jdbcurl,
                                driver_args={'user': self._username, 'password': self._password},
                                jars=lib_path + 'mysql-connector-java-8.0.16.jar')
            cursor = conn.cursor()
        if operator.eq(self._dbtype, 'sqlite'):
            conn = jdbc.connect(jclassname=self._jdbcclass, url=self._jdbcurl, jars=lib_path + 'sqlite-jdbc-3.28.0.jar')
            cursor = conn.cursor()
        if operator.eq(self._dbtype, 'hive'):
            pass
        if operator.eq(self._dbtype, 'gauss'):
            pass
        else:
            self._logger.error('暂不支持%s数据库类型' % self._dbtype)
        return {'conn': conn, 'cursor': cursor}

    def execute_single_sql(self, operate, sql, parameters=None):
        """
        执行单个SQL语句
        :param operate: SQL类型，DML、DDL
        :param sql:  SQL语句
        :param parameters:  SQL参数
        :return: 查询结果集
        """
        db_obj = self.connect_database()
        db_obj.get('cursor').execute(operation=sql, parameters=parameters)
        if operator.eq(operate, 'ddl'):
            db_obj.get('conn').commit()
        result = db_obj.get('cursor').fetchall()
        db_obj.get('cursor').close()
        db_obj.get('conn').close()
        return result


if __name__ == '__main__':
    sql = """select * from auth_user"""
    print(dbUtil().execute_single_sql(sql=sql, operate='dml'))
