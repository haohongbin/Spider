from tep.fixture import TepVars

from services.AddCart import AddCart
from services.Login import Login
from services.Order import Order
from services.Pay import Pay
from services.SearchSku import SearchSku

"""
测试登录到下单流程，需要先运行utils / flask_mock_api.py
"""


class Test:
    case_vars = TepVars()
    case_vars.vars_ = {
        "domain": "http://127.0.0.1:5000",
        "skuNum": "3"
    }

    def test(self):
        # 登录
        Login(Test).post()
        # 搜索商品
        SearchSku(Test).get()
        # 添加购物车
        AddCart(Test).post()
        # 下单
        Order(Test).post()
        # 支付
        Pay(Test).post()
