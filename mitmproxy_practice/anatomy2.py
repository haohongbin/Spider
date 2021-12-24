"""An addon using the abbreviated scripting syntax."""

# 插件机制的简写
def request(flow):
    flow.request.headers["myheader"] = "value"