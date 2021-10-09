# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 15:54
# @Author  : wanghc
# @File    : cookies.py
# @Software: PyCharm

import requests

'''
1、用cookie来维持登录状态
'''

headers = {
    'Cookie': '_octo=GH1.1.2050777581.1630467575; _device_id=cf890f57ea9d496ac5339987de6d4475; user_session=AKeGi3HgORdEnEa_vYnU_Xz4lTu0sZB7-XelymiokMcMbMfY; __Host-user_session_same_site=AKeGi3HgORdEnEa_vYnU_Xz4lTu0sZB7-XelymiokMcMbMfY; logged_in=yes; dotcom_user=xiaoyaowang18; has_recent_activity=1; color_mode={"color_mode":"dark","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; tz=Asia/Shanghai; _gh_sess=p4ZtvPNSqyWHsoO+Oc8Kx1GCoygm/yqYUC04BNDAXAsZri2CYkNTXhBZ+D8xkECnCz405l/LLDwcnPUVMoTzW2sOy622q1LJURgLb1WieJmLXaDB3ZwbZ0aPOK5ewrPVYOS9wWJ7GbIFfbMoBW2iLGH0wjV8WIxE9EfO1SsCAVESxDq95JN/kDH5Y5JTY7/+--Lh61AhLy+idhHuUN--fjm9deFg2JKKBItJiNXO8w==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

# r = requests.get("https://github.com", headers=headers)

'''
2、通过cookie参数来设置Cookies的信息，构造一个RequestCookieJar对象
'''

cookies = '_octo=GH1.1.2050777581.1630467575; _device_id=cf890f57ea9d496ac5339987de6d4475; user_session=AKeGi3HgORdEnEa_vYnU_Xz4lTu0sZB7-XelymiokMcMbMfY; __Host-user_session_same_site=AKeGi3HgORdEnEa_vYnU_Xz4lTu0sZB7-XelymiokMcMbMfY; logged_in=yes; dotcom_user=xiaoyaowang18; has_recent_activity=1; color_mode={"color_mode":"dark","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; tz=Asia/Shanghai; _gh_sess=p4ZtvPNSqyWHsoO+Oc8Kx1GCoygm/yqYUC04BNDAXAsZri2CYkNTXhBZ+D8xkECnCz405l/LLDwcnPUVMoTzW2sOy622q1LJURgLb1WieJmLXaDB3ZwbZ0aPOK5ewrPVYOS9wWJ7GbIFfbMoBW2iLGH0wjV8WIxE9EfO1SsCAVESxDq95JN/kDH5Y5JTY7/+--Lh61AhLy+idhHuUN--fjm9deFg2JKKBItJiNXO8w=='
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

# r = requests.get("https://github.com", cookies=jar,headers=headers)

