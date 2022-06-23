import seldom
from seldom import data

class LoginCodeTest(seldom.TestCase):
    """用户发送验证码"""

    def start(self):
        self.url = "/coach-provider/coach/login/code"

    def test_login(self):
        payload = {
            "secret": "pf5j2783c7jnGEgfMyJ08em9UABY1OGwHw8IKuY1/7+JJWBrDC3xa6ZKVwmcyUvp+LcbsgJElqTq1SXlBq57LYSQ0oc617a2U6nN66DcN5c10MYr/Eb17N61jy2TmmUlv3B30w/nuVgakFPP0Nxrc2kAlWRu3pQ8GyX9u6OOxY="
        }
        self.post(self.url, json=payload)
        self.assertStatusCode(200)
        except_json = {"status":"true","data":"OK","code":100000,"msg":"OK","ts":1645782243,"version":"v2","success":"true"}

        self.assertJSON(except_json)

if __name__ == '__main__':
    seldom.main(base_url="https://test.coachapi.yundiketang.cn", debug=True)
