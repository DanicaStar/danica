# -*- coding: utf-8 -*-
# @Time    : 2022/9/30 10:42 上午
# @Author  : danica
# @FileName: common.py
# @Software: PyCharm
from socket import create_connection

import requests


# 定义一个common的类，它的父类是object
class Common(object):
    # common的构造函数
    def __init__(self, url_root, api_type):
        """
        :param api_type:接口类似当前支持http、ws，http就是HTTP协议，ws是WebSocket协议
        :param url_root: 被测系统的根路由
        """
        if api_type == 'ws':
            self.ws = create_connection(url_root)
        elif api_type == 'http':
            self.ws = 'null'
            self.url_root = url_root

    # # 被测系统的根路由
    #     self.url_root = 'http://127.0.0.1:12356'

    # ws协议的消息发送
    def send(self, params):  # 封装send()
        """
        :param params: websocket接口的参数
        :return: 访问接口的返回值
        """
        self.ws.send(params)
        res = self.ws.recv()
        return res

    # common类的析构函数，清理没有用的资源
    def __del__(self):
        if self.ws != 'null':
            self.ws.close()

    # 封装你自己的get请求，uri是访问路由，params是get请求的参数，如果没有默认为空
    def get(self, uri, params=None):
        # 拼凑访问地址
        if params is not None:
            url = self.url_root + uri + params
        else:
            url = self.url_root + uri
        # 通过get请求访问对应地址
        res = requests.get(url)
        # 返回request的Response结果，类型为requests的Response类型
        return res

    # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
    def post(self, uri, params=None):
        # 拼凑访问地址
        url = self.url_root + uri
        if params is not None:
            # 如果有参数，那么通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url)
        return res

    def put(self, uri, params=None):
        """
        封装你自己的put方法，uri是访问路由，params是put请求需要传递的参数，如果没有参数这里为空
        :param uri: 访问路由
        :param params: 传递参数，string类型，默认为None
        :return: 此次访问的response
        """
        url = self.url_root + uri
        if params is not None:
            # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.put(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.put(url)
        return res

    def delete(self, uri, params=None):
        """
        封装你自己的delete方法，uri是访问路由，params是delete请求需要传递的参数，如果没有参数这里为空
        :param uri: 访问路由
        :param params: 传递参数，string类型，默认为None
        :return: 此次访问的response
        """
        url = self.url_root + uri
        if params is not None:
            # 如果有参数，那么通过delete方式访问对应的url，并将参数赋值给requests.delete默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.delete(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.delete(url)
        return res
