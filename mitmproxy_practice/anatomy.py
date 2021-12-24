"""
Basic skeleton of a mitmproxy_practice addon.

Run as follows: mitmproxy_practice -s anatomy.py
"""

from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)


addons = [
    Counter()
]