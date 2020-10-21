WeChat notification sending resource
=================================

Sends message to [WeChat](https://weixin.qq.com/)

Resource Type Configuration
---------------------------
```yaml
resource_types:
- name: wechat-notification
  type: docker-image
  source:
    repository: dockerhuangyisan/wechat-notification-resource
    tag: latest
```

Source Configuration
---------------------------------

Wechat Webhook, go to
<https://open.work.weixin.qq.com/api/doc/90000/90135/90236>

Behavior
--------
### `check`: Not support
### `in`: Not support
### `out`: Sends a message to WeChat.

Send a message to Slack, with the configured parameters.

#### Parameters

You must specify one or more of the following:

- `url`:  WeChat webhook url
- `secret`: Your access_token
- `msgtype`: Message type
- `level`:  Alert level
- `content`: Content info

Pipeline Example
----------------

```yaml

jobs:
- name: test-run
  plan:
  - params:
      level: failed
      msgtype: markdown
      secret: [YOUR-WECHAT-TOKEN]
      content: JOB FAILED
    put: wx-alert
resource_types:
- name: wechat-notification
  source:
    repository: dockerhuangyisan/wechat-notification-resource
    tag: "latest"
  type: docker-image
resources:
- name: wx-alert
  type: wechat-notification
```

#### Wechat Message Example
![wechat_message_example](https://image.kirakirazone.com/image/wechat_message.png)



Docker image
---------------
https://hub.docker.com/r/dockerhuangyisan/wechat-notification-resource



