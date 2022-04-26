# -*- coding:utf-8 -*-
# @Time : 2022/4/26 21:56
# @Author : huichuan LI
# @File : logger.py
# @Software: PyCharm
import logging
from functools import wraps


def Debug(func):
    """Debug decorator"""

    @wraps(func)  # 使用 functools 的 wraps 装饰器包装一下 func 的信息
    def debug(*args, **kwargs):
        res = func(*args, *kwargs)  # 调用 func 函数
        logging.getLogger().debug(
            "{} is invoked with {}".format(
                func.__name__, args if len(args) > 0 else kwargs
            )
        )  # 输出日志信息
        return res

    return debug


def Info(func):
    """Info decorator"""

    @wraps(func)
    def info(*args, **kwargs):
        res = func(*args, *kwargs)
        logging.getLogger().info(
            "{} is invoked with {}".format(
                func.__name__, args if len(args) > 0 else kwargs
            )
        )
        return res

    return info


def Warning(func):
    """Warning decorator"""

    @wraps(func)
    def warning(*args, **kwargs):
        res = func(*args, *kwargs)
        logging.getLogger().warning("{} is invoked with {}".format(
            func.__name__, args if len(args) > 0 else kwargs))
        return res

    return warning


def Error(func):
    """Error decorator"""

    @wraps(func)
    def error(*args, **kwargs):
        res = func(*args, *kwargs)
        logging.getLogger().error("{} is invoked with {}".format(
            func.__name__, args if len(args) > 0 else kwargs))
        return res

    return error


def Critical(func):
    """Critical decorator"""

    @wraps(func)
    def critical(*args, **kwargs):
        res = func(*args, *kwargs)
        logging.getLogger().critical("{} is invoked with {}".format(
            func.__name__, args if len(args) > 0 else kwargs))
        return res

    return critical
