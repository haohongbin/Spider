from mitmproxy import flow
from mitmproxy.addons.export import curl_command


def durl(f: flow.Flow):
    print(curl_command(f))