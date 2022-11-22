# -*- coding: utf-8 -*-
"""
    处理jwt，返回给前端进行校验
"""

import jwt
import time

headers = {
    'alg': "HS256",  # 声明所使用的算法
}


def generate_token(username):
    payload = {
        'expired_time': int(time.time()) + 3600,
        'login_time': int(time.time()),
        'username': username
    }
    jwt_token = jwt.encode(payload, 'abcdefg', algorithm="HS256", headers=headers)
    return jwt_token