from tep.client import BaseRequest


class AddCart(BaseRequest):

    def post(self):
        response = self.request(
            "post",
            url=self.case_vars.get("domain") + "/addCart",
            headers={"token": self.case_vars.get("token")},
            json={"skuId": self.case_vars.get("skuId"), "skuNum": self.case_vars.get("skuNum")}
        )
        self.case_vars.put("totalPrice", response.jmespath("totalPrice"))
        assert response.status_code < 400
