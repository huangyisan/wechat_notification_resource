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

### `out`: Sends a message to WeChat.

Send a message to Slack, with the configured parameters.

#### Parameters

You must specify one or more of the following:

- `url`:  WeChat webhook url
- `secret`: Your access_token
- `msgtype`: Message type
- `level`:  Alert level
- `pipeline`:  Pipeline name
- `content`: Content info