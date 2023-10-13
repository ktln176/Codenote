import random
from os import path


def get_random_user_agent() -> str:
    """返回随机user-agent"""
    user_agent_list = []
    with open(r'../static/user-agents.txt', 'r', encoding='utf-8') as f:
        for user_agent in f:
            user_agent_list.append(str(user_agent).replace('\n', ''))

    return user_agent_list[random.randint(0, len(user_agent_list) - 1)]


def test_get_random_user_agent():
    res = get_random_user_agent()
    print(res)


def get_cookie_txt(filename: str or path) -> str:
    """返回指定cookie文本"""
    with open(rf'../static/{filename}.txt', 'r', encoding='utf-8') as f:
        cookie_txt = ''.join(i for i in f).replace('\n', '')
    return cookie_txt


def test_get_cookie_txt():
    res = get_cookie_txt('zhihu_cookie')
    print(res)


if __name__ == '__main__':
    test_get_random_user_agent()
    test_get_cookie_txt()
