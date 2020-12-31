# -*- coding: UTF8 -*-
import jaydebeapi as jdbc
from pythonlog.utils.logUtil import init_logging
from framework.utils import YamlParser
import operator
from framework.getrootdir import root_path
import os


class dbUtil:
    def __init__(self):
        """
        初始化连接串，并连接oracle
        """
        self._logger = init_logging()
        self._yaml = YamlParser().parser_common_conf(cf='projectConfig.yaml')
        self._dbinfo = self._yaml.get(self._yaml.get('project')).get('dbinfo')
        self._dbtype = self._dbinfo.get('type')
        self._username = self._yaml.get(self._dbtype).get('username')
        self._password = self._yaml.get(self._dbtype).get('password')
        self._jdbcclass = self._yaml.get(self._dbtype).get('jdbcClass')
        self._jdbcurl = self._yaml.get(self._dbtype).get('jdbcurl')

    def connect_database(self):
        """
        连接数据库
        """
        lib_path = root_path + os.sep + 'libs' + os.sep

        if operator.eq(self._dbtype, 'oralce'):
            conn = jdbc.connect(jclassname=self._jdbcclass, jars=lib_path + 'ojdbc8.jar',
                                url=self._jdbcurl, driver_args={'user': self._username, 'password': self._password})
            cursor = conn.cursor()
        elif operator.eq(self._dbtype, 'mysql'):
            conn = jdbc.connect(jclassname=self._jdbcclass, url=self._jdbcurl,
                                driver_args={'user': self._username, 'password': self._password},
                                jars=lib_path + 'mysql-connector-java-8.0.16.jar')
            cursor = conn.cursor()
        elif operator.eq(self._dbtype, 'sqlite3'):
            conn = jdbc.connect(jclassname=self._jdbcclass, url=self._jdbcurl, jars=lib_path + 'sqlite-jdbc-3.28.0.jar')
            cursor = conn.cursor()
        else:
            self._logger.error('暂不支持%s数据库类型' % self._dbtype)
            raise
        return {'conn': conn, 'cursor': cursor}

    def execute_sql(self, operate, sql, parameters=None):
        """
        执行单个ＳＱＬ
        :param operate: 　操作类型，ddl／dml
        :param sql: sql语句，使用参数的方式时，sql必须使用　：variable的方式绑定变量
        :param parameters: sql参数，传入字典族
        :return:　查询结果集
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
    print(dbUtil().execute_sql(sql=sql, operate='dml'))
