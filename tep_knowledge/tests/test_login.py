from loguru import logger


def test_login(login):
    logger.info(login.token)
