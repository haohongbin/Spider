#!/usr/bin/python
# encoding=utf-8


from tep.fixture import *


@pytest.fixture
def fixture_three():
    logger.info("fixture_three")
