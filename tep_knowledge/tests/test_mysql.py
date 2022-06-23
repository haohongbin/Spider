from loguru import logger
from tep.dao import print_db_table


def test_mysql(pd, env_vars):
    data = pd.read_sql("select * from mobile_verify_codes_new where mobile = 16312345678", env_vars.mysql_engine)
    logger.info(print_db_table(data))
