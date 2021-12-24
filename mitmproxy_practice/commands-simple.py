"""Add a custom command to mitmproxy's command prompt."""
from mitmproxy import command
from mitmproxy import ctx

# 自定义命令
class MyAddon:
    def __init__(self):
        self.num = 0

    @command.command("myaddon.inc")
    def inc(self) -> None:
        self.num += 1
        ctx.log.info(f"num = {self.num}")


addons = [
    MyAddon()
]