from httprunner import HttpRunner, Config, Step, RunRequest

"""
测试登录到下单流程，需要先运行utils/flask_mock_api.py
"""


class TestLoginPay(HttpRunner):
    config = (
        Config("登录到下单流程")
            .variables(
            **{
                "skuNum": "3"
            }
        )
            .base_url("http://127.0.0.1:5000")
    )

    teststeps = [
        Step(
            RunRequest("登录")
                .post("/login")
                .with_headers(**{"Content-Type": "application/json"})
                .with_json({"username": "dongfanger", "password": "123456"})
                .extract()
                .with_jmespath("body.token", "token")
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("搜索商品")
                .get("searchSku?skuName=电子书")
                .with_headers(**{"token": "$token"})
                .extract()
                .with_jmespath("body.skuId", "skuId")
                .with_jmespath("body.price", "skuPrice")
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("添加购物车")
                .post("/addCart")
                .with_headers(**{"Content-Type": "application/json",
                                 "token": "$token"})
                .with_json({"skuId": "$skuId", "skuNum": "$skuNum"})
                .extract()
                .with_jmespath("body.totalPrice", "totalPrice")
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("下单")
                .post("/order")
                .with_headers(**{"Content-Type": "application/json",
                                 "token": "$token"})
                .with_json({"skuId": "$skuId", "price": "$skuPrice", "skuNum": "$skuNum", "totalPrice": "$totalPrice"})
                .extract()
                .with_jmespath("body.orderId", "orderId")
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("支付")
                .post("/pay")
                .with_headers(**{"Content-Type": "application/json",
                                 "token": "$token"})
                .with_json({"orderId": "$orderId", "payAmount": "6.9"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.success", "true")
        ),
    ]
