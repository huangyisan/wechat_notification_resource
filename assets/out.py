#!/usr/bin/python
import json
import sys
import requests
import time


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


pipeline = sys.argv[2]

base_info = {
    "msgtype": "markdown",
    "markdown": {
        "content": ""
    }
}

base_content_info = '''
>**事件详情**
>时 间：<font color=\"info\">{time}</font>
>Pipeline：`{pipeline}`
'''.format(time=get_time(), pipeline=pipeline)

level = sys.argv[1]
title_info = ""
if level.lower() == "success":
    title_info = "<font color=\"info\">Job Success</font>"
elif level.lower() == "failed":
    title_info = "<font color=\"warning\">Job Failed</font>"
elif level.lower() == "abort":
    title_info = "<font color=\"comment\">Job Abort</font>"

content = base_content_info

base_info.get("markdown")["content"] = title_info + '\n' + content

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send"

params = {
    "key": "3d1ecb4e-af78-4a92-9dd2-d8af4565c95a"
}

data = json.dumps(base_info)

headers = {
    'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=data, params=params)
if response.status_code == 200:
    pass
else:
    print(response.text)

