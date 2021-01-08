WeChat notification sending resource
=================================
[![Build Status](http://jenkins.kirakirazone.com:60080/buildStatus/icon?job=wechat_notification_resource%2Ffeature-auto-ci)](http://jenkins.kirakirazone.com:60080/job/wechat_notification_resource/job/feature-auto-ci/)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/huangyisan/wechat_notification_resource?style=flat)

Sends message to [WeChat](https://www.wechat.com/)

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

WeChat Webhook, go to
<https://open.work.weixin.qq.com/api/doc/90000/90135/90236>

Behavior
--------
### `check`: Not support
### `in`: Not support
### `out`: Sends a message to WeChat.

Send a message to WeChat group, with the configured parameters.

#### Parameters

You must specify one or more of the following:

- `secret`: Required. The WeChart Group robot's access token.
- `msgtype`: Required. Message type, current only support markdown.
- `level`:  Required. Message level (success, failed, abort, error).
- `content`: Required. Static text of the message to send.

Optional:

- `url`: Optional. Override webhook url send message to.

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

Docker image
---------------
https://hub.docker.com/r/dockerhuangyisan/wechat-notification-resource



