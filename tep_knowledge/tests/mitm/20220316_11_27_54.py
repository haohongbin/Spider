from tep.client import request


def test():

    # 接口描述
    # 数据
    # 请求
    response = request(
        "post",
        url="https://userapi.yundiketang.com/student-provider/contract/list",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'Content-Length': '12', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': '6jlFX0tRtn80Rm8F7c96zy0q6I0b', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740135530610021637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        json={"status":2}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "post",
        url="https://userapi.yundiketang.com/student-provider/open/klass/calendar",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'Content-Length': '67', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': '6jlFX0tRtn80Rm8F7c96zy0q6I0b', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740135531810031637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        json={"startDate":"2022-03-16 00:00:00","endDate":"2022-03-16 23:00:00"}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': '6jlFX0tRtn80Rm8F7c96zy0q6I0b', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740135528610011637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/signList?status=1",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740135603010081637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/coach/recommend/for/student",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740135628910121637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740135819210141637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "post",
        url="https://userapi.yundiketang.com/student-provider/open/coach/list/for/student",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'Content-Length': '135', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740135820010151637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        json={"pageSize":10,"pageNum":1,"subject":1,"level":"","minPrice":0,"maxPrice":10000,"labelIds":[],"coachSex":0,"startTime":"","endTime":""}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "post",
        url="https://userapi.yundiketang.com/student-provider/open/klass/calendar",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'Content-Length': '67', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740141770910201637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        json={"startDate":"2022-03-16 00:00:00","endDate":"2022-03-31 23:00:00"}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "post",
        url="https://userapi.yundiketang.com/student-provider/open/klass/list",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'Content-Length': '94', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740141769110191637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        json={"startDate":"2022-03-16 00:00:00","endDate":"2022-03-16 23:00:00","pageSize":100,"pageNum":1}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/klass/cancelNumber",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740141772210211637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "post",
        url="https://userapi.yundiketang.com/student-provider/contract/list",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'Content-Length': '12', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740141792110251637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        json={"status":2}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "post",
        url="https://userapi.yundiketang.com/student-provider/open/coach/list/for/student",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'Content-Length': '36', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740141803610271637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        json={"pageSize":5,"pageNum":1,"index":1}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740141980410301637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/signList?status=2",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740142162410331637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740142383310361637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/activeCode/list",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740142649110381637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740142703010401637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/details",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740142795910431637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740142962710461637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740143219510491637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': 'vvl1e0RqtbO0sv8Lwdnd281w2jk5', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/index/index","query":{}}', 'EagleEye-TraceID': '4f9b379c164740143471610521637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400

    # 接口描述
    # 数据
    # 请求
    response = request(
        "get",
        url="https://userapi.yundiketang.com/student-provider/open/student/vip/status",
        headers={'Host': 'userapi.yundiketang.com', 'Connection': 'keep-alive', 'EagleEye-pAppName': 'dbzdilg9jb@301976d1e21637c', 'EagleEye-SessionID': '1wlg50sCtXw03Uay45hFmFFqCkkb', 'content-type': 'application/json;charset=UTF-8', 'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDdmZGY5Ni02ZjY4LTRjYTQtODViZS04NDI0OTVlM2ExYzQiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQ3MjUxODAxLCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQ3MjUxODAxLCJqdGkiOiJiZjM0NzNkNC1hYmZmLTQ5MzctYTIyMS0yMzIwNWZhZDkzMTcifQ.16coLGeltTdbe3D4MbjIBDxcjhH2T8PjwLOkI7KCVDM', 'sensor': '{"scene":1089,"path":"pages/me/me","query":{}}', 'EagleEye-TraceID': '4f9b379c164740143900010551637c', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001235) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx97458f4f57236ff5/6/page-frame.html'},
        params={}
    )
    # 数据提取
    # var = response.jmespath("expression")
    # 断言
    assert response.status_code < 400
