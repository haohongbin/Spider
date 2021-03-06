from tep.client import BaseRequest


class SearchSku(BaseRequest):

    def get(self):
        response = self.request(
            "get",
            url=self.case_vars.get("domain") + "/searchSku",
            headers={"token": self.case_vars.get("token")},
            params={"skuName": "电子书"}
        )
        self.case_vars.put("skuId", response.jmespath("skuId"))
        self.case_vars.put("skuPrice", response.jmespath("price"))
        assert response.status_code < 400
