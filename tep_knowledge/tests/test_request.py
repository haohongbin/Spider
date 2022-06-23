from tep.client import request

request("get", url="", headers={}, json={})
request("post", url="", headers={}, params={})
request("put", url="", headers={}, json={})
request("delete", url="", headers={})

# upload excel
file_name = ""
file_path = ""
request("post",
        url="",
        headers={},
        files={
            "file": (
                file_name,
                open(file_path, "rb"),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        },
        verify=False
        )
