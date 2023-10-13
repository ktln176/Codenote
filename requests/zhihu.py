import requests
from bs4 import BeautifulSoup

from common import module

url = r'https://www.zhihu.com/hot'

head = {
    'Cookie': module.get_cookie_txt('zhihu_cookie'),
    'User-Agent': module.get_random_user_agent()
}

res_text = requests.get(url, headers=head).text

res_soup = BeautifulSoup(res_text, features='lxml')
print(res_soup.prettify())
