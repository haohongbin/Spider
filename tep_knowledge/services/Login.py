from tep.client import BaseRequest


class Login(BaseRequest):

    def post(self):
        response = self.request(
            "post",
            url=self.case_vars.get("domain") + "/login",
            headers={"Content-Type": "application/json"},
            json={
                "username": "dongfanger",
                "password": "123456",
            }
        )
        assert response.status_code < 400
        self.case_vars.put("token", response.jmespath("token"))
