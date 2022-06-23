#!/usr/bin/python
# encoding=utf-8

from tep.dao import mysql_engine
from tep.fixture import *


@pytest.fixture(scope="session")
def env_vars(config):
    class Clazz(TepVars):
        env = config["env"]

        """变量定义开始"""
        # 环境变量
        mapping = {
            "qa": {
                "domain": "http://127.0.0.1:5000",
                "mysql_engine": mysql_engine("rm-2zef25889658j8c6w.mysql.rds.aliyuncs.com",  # host
                                             "3306",  # port
                                             "kpl_notify",  # username
                                             "Vw7L6E10430OiXkQ",  # password
                                             "kpl_notify"),  # db_name
            },
            "release": {
                "domain": "https://release.com",
                "mysql_engine": mysql_engine("127.0.0.1",
                                             "2306",
                                             "root",
                                             "123456",
                                             "release"),
            }
            # 继续添加
        }
        # 定义类属性，敲代码时会有智能提示
        domain = mapping[env]["domain"]
        mysql_engine = mapping[env]["mysql_engine"]
        """变量定义结束"""

    return Clazz()
