from mitmproxy.addons.export import curl_command
import os

base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
base_dir = os.path.join(base_dir, "mitmproxy_practice")



def request(flow):
    curl = curl_command(flow)
    with open(os.path.join(base_dir, 'curl'), 'w', encoding='utf-8') as f:
        f.write(curl)