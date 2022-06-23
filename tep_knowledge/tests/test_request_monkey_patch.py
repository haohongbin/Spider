from utils.http_client import request


def test_login(env_vars):
    response = request(
        "post",
        url=env_vars.domain + "/login",
        desc="登录",
        headers={"Content-Type": "application/json"},
        json={
            "username": "dongfanger",
            "password": "123456",
        }
    )
    assert response.status_code < 400
