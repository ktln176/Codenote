import random
from os import path


def get_random_user_agent() -> str:
    """返回随机user-agent"""
    user_agent_list = []
    with open(r'../static/user-agents.txt', 'r', encoding='utf-8') as f:
        for user_agent in f:
            user_agent_list.append(str(user_agent).replace('\n', ''))

    return user_agent_list[random.randint(0, len(user_agent_list) - 1)]


def get_cookie_txt(filename: str or path) -> str:
    """
    返回指定txt文件字符串
    :param filename: txt文件名称
    :return: txt文本str
    """
    with open(rf'../static/{filename}.txt', 'r', encoding='utf-8') as f:
        text = ''.join(i for i in f).replace('\n', '')
    return text
