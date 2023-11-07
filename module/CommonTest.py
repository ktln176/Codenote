from unittest import TestCase

import Common


class Test(TestCase):

    def test_get_random_user_agent(self):
        """返回随机user-agent"""
        res = Common.get_random_user_agent()
        print(res)

    def test_get_cookie_txt(self):
        """返回指定cookie文本"""
        res = Common.get_cookie_txt('zhihu_cookie')
        print(res)
