"""
    Created by fre123 at 2024-10-11.
    Description: 项目整体配置文件
    Changelog: all notable changes to this file will be documented
"""

import os

from src.utils.tools import read_file


class Config:
    """
    Basic config
    """

    # Application config
    DEBUG = True
    TIMEZONE = "Asia/Shanghai"
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    ROOT_DIR = os.path.join(os.path.dirname(BASE_DIR))
    PROJECT_NAME = os.getenv("PROJECT_NAME", ROOT_DIR.split("/")[-1])
    API_DIR = os.path.join(BASE_DIR, "views")
    HOST = os.getenv("HOST", "0.0.0.0")
    HTTP_PORT = os.getenv("HTTP_PORT", 8067)
    WORKERS = os.getenv("WORKERS", 1)

    APP_ID_CONFIG = {"yz_pansearch_api": os.getenv("APP_TOKEN", "123456")}
    MONGODB_CONFIG = {
        "mongodb_uri": os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27067/admin"),
        "operate_db": os.getenv("MONGODB_DB", "yz_pansearch"),
    }
    REDIS_CONFIG = {
        "host": os.getenv("REDIS_HOST", "127.0.0.1"),
        "port": int(os.getenv("REDIS_PORT", "6389")),
        "password": os.getenv("REDIS_PASSWORD", "1234562"),
        "db": int(os.getenv("REDIS_DB", "6")),
        "cache_ttl": int(os.getenv("REDIS_CACHE_TTL", "600")),
    }

    TAG = {
        "info": f"{PROJECT_NAME.replace('_', '-')}-info",
        "warn": f"{PROJECT_NAME.replace('_', '-')}-warn",
        "error": f"{PROJECT_NAME.replace('_', '-')}-error",
    }

    @staticmethod
    def get_version() -> str:
        """获取当前服务版本, 需要自定义 version 文件"""
        version_list = read_file(os.path.join(Config.ROOT_DIR, "version"))
        return version_list[0] if version_list else "undefined"


if __name__ == "__main__":
    print(Config.API_DIR)