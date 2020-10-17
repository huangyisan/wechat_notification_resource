#!/usr/bin/python
import json
import sys
import requests
import time
from common import eprint


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def get_args(stream):
    eprint(stream)
    payload = json.load(stream)
    eprint(payload)
    return payload


def payload_data(payload):
    # source = payload["source"]
    source = payload["params"]
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send" if not source.get("url") else source.get("url")
    secret = source["secret"]
    msgtype = "markdown" if not source.get("msgtype") else source.get("msgtype")
    # success, failed, abort
    level = "success" if not source.get("level") else source.get("level")
    # pipeline name
    pipeline = source["pipeline"]
    content = "No content" if not source.get("content") else source.get("content")
    payload_dict = {"url": url, "secret": secret, "msgtype": msgtype, "level": level, "pipeline": pipeline, "content":content}
    return payload_dict


def get_title_info(level):
    title_info = ""
    if level.lower() == "success":
        title_info = "<font color=\"info\">Job Success</font>"
    elif level.lower() == "failed":
        title_info = "<font color=\"warning\">Job Failed</font>"
    elif level.lower() == "abort":
        title_info = "<font color=\"comment\">Job Abort</font>"
    elif level.lower() == 'error':
        title_info = "<font color=\"comment\">Job Error</font>"
    return title_info


def message(msgtype, pipeline, level, content):
    message = {
        "msgtype": msgtype,
        "markdown": {
            "content": ""
        }
    }

    base_content_info = '''
>**事件详情**
>时 间: <font color=\"info\">{time}</font>
>Pipeline: `{pipeline}`
>Content: `{content}`
'''.format(time=get_time(), pipeline=pipeline, content=content)

    content = base_content_info

    message.get("markdown")["content"] = get_title_info(level) + "\n" + content

    return message


def post_message(url, secret, data):
    headers = {
        'Content-Type': 'text/plain'
    }

    params = {
        "key": secret
    }
    # pprint(type(data))
    data = json.dumps(data)
    # pprint(type(data))
    response = requests.request("POST", url, headers=headers, data=data, params=params)
    # pprint(response.text, stream=sys.stderr)
    if response.status_code != 200:
        print(response.json())


def get_timestamp():
    return str(int(time.time()))


def _out(stream):
    payload = get_args(stream)
    payload_dict = payload_data(payload)

    url, secret, msgtype, level, pipeline, content = payload_dict.values()

    data = message(msgtype, pipeline, level, content)
    post_message(url, secret, data)
    timestamp = get_timestamp()
    return {"version": {"version": timestamp}}


if __name__ == "__main__":
    print(json.dumps(_out(sys.stdin)))
