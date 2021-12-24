import json
from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 加上过滤条件

    if flow.request.path.endswith('/getScores'):
    # if "http://api.pangxiaolu.com/pangxiaolu/score/getScores" in flow.request.pretty_url:
        # 将响应内容转成字典格式
        data = json.loads(flow.response.content)
        # 修改对应字段的值
        data["data"]["records"][0]["name"] = "第1课 上学的日子88888"
        # 把修改后的数据转成字符串赋值给原始数据
        flow.response.text = json.dumps(data)
