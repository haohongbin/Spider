
from sp.db_operation.mysql_db import MySQLDB
from sp.fixture import *


@pytest.fixture(scope="session")
def env_vars(config):
    class Clazz(SpVars):
        env = config["env"]

        """变量定义开始"""
        # 环境变量
        mapping = {
            "qa": {
                "domain": "http://127.0.0.1:5000",
                "mysql_engine": MySQLDB("127.0.0.1",  # host
                                             "2306",  # port
                                             "root",  # username
                                             "123456",  # password
                                             "qa"),  # db_name
            },
            "release": {
                "domain": "https://release.com",
                "mysql_engine": MySQLDB("127.0.0.1",
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
