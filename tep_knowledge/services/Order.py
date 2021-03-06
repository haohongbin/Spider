from tep.client import BaseRequest


class Order(BaseRequest):

    def post(self):
        response = self.request(
            "post",
            url=self.case_vars.get("domain") + "/order",
            headers={"token": self.case_vars.get("token")},
            json={"skuId": self.case_vars.get("skuId"), "price": self.case_vars.get("skuPrice"),
                  "skuNum": self.case_vars.get("skuNum"), "totalPrice": self.case_vars.get("totalPrice")}
        )
        self.case_vars.put("orderId", response.jmespath("orderId"))
        assert response.status_code < 400
