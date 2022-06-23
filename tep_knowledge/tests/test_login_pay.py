import jmespath
from tep.client import request

"""
测试登录到下单流程，需要先运行utils/flask_mock_api.py
"""


def test(env_vars, login):
    # 搜索商品
    response = request(
        "get",
        url=env_vars.domain + "/searchSku",
        headers={"token": login.token},
        params={"skuName": "电子书"}
    )
    sku_id = jmespath.search("skuId", response.json())
    sku_price = jmespath.search("price", response.json())
    assert response.status_code < 400

    # 添加购物车
    sku_num = 3
    response = request(
        "post",
        url=env_vars.domain + "/addCart",
        headers={"token": login.token},
        json={"skuId": sku_id, "skuNum": str(sku_num)}
    )
    total_price = jmespath.search("totalPrice", response.json())
    assert response.status_code < 400

    # 下单
    response = request(
        "post",
        url=env_vars.domain + "/order",
        headers={"token": login.token},
        json={"skuId": sku_id, "price": sku_price, "skuNum": str(sku_num), "totalPrice": total_price}
    )
    order_id = jmespath.search("orderId", response.json())
    assert response.status_code < 400

    # 支付
    response = request(
        "post",
        url=env_vars.domain + "/pay",
        headers={"token": login.token},
        json={"orderId": order_id, "payAmount": "6.9"}
    )
    assert response.status_code < 400
    assert response.json()["success"] == "true"
