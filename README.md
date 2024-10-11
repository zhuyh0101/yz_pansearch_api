# 网盘搜索 API

> 元站CMS&资源搜索引擎是一套内容管理系统，所有人都可以基于元站快速起站，构建自己的创意站点，目前盈利模式是基于内容做 SEO，通过底层的网盘分佣、会员以及流量广告赚钱。

元站本身是一个类似 WordPress 的内容管理系统，本身不提供资源搜索能力，仅仅是个站点构建系统，但是元站的用户可以通过元站的插件系统，自行开发一个网盘搜索 API 插件，实现网盘搜索功能，示例网站👉[夸克搜](https://www.quark.so/)。

本站就是一个符合[元站](https://www.moneysou.com/zsyz/89s4uc)搜索接口规范的网盘搜索 API 插件项目，基于本项目，所有购买元站的用户都可以自行搭建一个网盘搜索 API 服务，方便实现**全网搜**功能。

如果你感兴趣，可以通过我的[邀请码](https://www.moneysou.com/login?ref=moneysou)注册购买。

![元站](https://img.fre123.com/i/2024/10/11/6708f20fbc21d.jpg)

## 使用

直接基于 Docker 部署：

```shell
docker run -d -p 8067:8067 --name yz_pansearch_api --restart unless-stopped \
-e APP_TOKEN=设置 token \
-e REDIS_HOST=Redis 用户名 \
-e REDIS_PORT=Redis 端口 \
-e REDIS_PASSWORD=Redis 密码 \
-e REDIS_DB=11 \
-e REDIS_CACHE_TTL=600 \
howie6879/yz_pansearch_api:http-v0.1.0
```

目前支持的源有：

- kk: http://z.kkkob.com/
- 更多支持中

启动成功后，通过 `http://ip:8067`，curl 的请求示例如下：

```shell
curl --request POST \
  --url http://127.0.0.1:8067/v1/search/get_kk \
  --header 'APP-ID: yz_pansearch_api' \
  --header 'APP-TOKEN: 你启动服务自己设置的 Token' \
  --header 'PAN-TYPE: quark' \
  --header 'content-type: application/json' \
  --data '{
  "kw": "xx"
}'
```

返回格式（符合元站官方标准即可）：

```json
{
  "data": {
    "total": 1,
    "data": [
      {
        "title": "七龙珠",
        "description": "",
        "res_dict": {
          "quark": [
            "https://pan.quark.cn/s/xxx"
          ],
          "baidu": [
            "https://pan.baidu.com/s/xxx"
          ]
        }
      }
    ]
  },
  "info": "ok",
  "status": 0
}
```

## 开发

```shell
git clone https://github.com/fre123-com/yz_pansearch_api
cd yz_pansearch_api
# 请先确认本机存在 python 3.11 的开发环境
# pipenv install --python=/~/anaconda3/envs/python3.11/bin/python3.11 --dev --skip-lock
pipenv install --python={YOUR_PYTGHON_PATH} --dev --skip-lock
# 推荐使用 VSCode 打开项目
```

## 说明

项目相关文档：
 - [接口文档](./docs/bruno/): 直接使用 [Bruno](https://github.com/usebruno/bruno) 打开即可调试接口&阅读文档
