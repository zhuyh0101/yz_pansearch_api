"""
    Created by fre123 at 2024-10-11.
    Description: 项目HTTP启动文件
        - 启动: pipenv run python ./src/http_app.py
    Changelog: all notable changes to this file will be documented
"""

import requests

from flask import Flask

from src.config import LOGGER, Config
from src.views import bp_api


def create_app():
    """
    建立 web 应用
    :return:
    """
    flask_app = Flask(__name__)

    with flask_app.app_context():
        from src.databases import MongodbBase, MongodbManager, RedisBase, RedisManager

        # 初始化 MongoDB
        # mongodb_base: MongodbBase = MongodbManager.get_mongo_base(
        #     mongodb_config=Config.MONGODB_CONFIG
        # )
        # 初始化 Redis
        redis_base: RedisBase = RedisManager.get_redis_base(
            redis_config=Config.REDIS_CONFIG
        )
        # 项目内部配置
        flask_app.config["app_config"] = Config
        # flask_app.config["mongodb_base"] = mongodb_base
        flask_app.config["redis_base"] = redis_base
        flask_app.config["app_logger"] = LOGGER
        flask_app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024
        # 全局请求 session
        req_session = requests.session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=200, pool_maxsize=200)
        req_session.mount("http://", adapter)
        req_session.mount("https://", adapter)
        flask_app.config["app_req_session"] = req_session
        flask_app.config["app_logger"] = LOGGER

        # 打印启动日志
        api_version = Config.get_version()
        LOGGER.info(
            f"Service({Config.PROJECT_NAME}) started successfully: {api_version}"
        )

    # 注册相关蓝图
    flask_app.register_blueprint(bp_api)
    return flask_app


app = create_app()

if __name__ == "__main__":
    app.run(port=Config.HTTP_PORT, debug=Config.DEBUG)