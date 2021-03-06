from tep.client import BaseRequest


class Pay(BaseRequest):

    def post(self):
        response = self.request(
            "post",
            url=self.case_vars.get("domain") + "/pay",
            headers={"token": self.case_vars.get("token")},
            json={"orderId": self.case_vars.get("orderId"), "payAmount": "6.9"}
        )
        assert response.status_code < 400
        assert response.jmespath("success") == "true"
