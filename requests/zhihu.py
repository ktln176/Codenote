import requests
from bs4 import BeautifulSoup

from module import Common

url = r'https://www.zhihu.com/hot'

head = {
    'Cookie': Common.get_cookie_txt('zhihu_cookie'),
    'User-Agent': Common.get_random_user_agent()
}

res_text = requests.get(url, headers=head).text

# 格式化
# res_soup = BeautifulSoup(res_text, features='lxml').prettify()

res_soup = BeautifulSoup(res_text, "lxml")
elements = res_soup.findAll('section')
print(len(elements))
for index, value in enumerate(elements):
    print(index + 1)
    print(value.find_all('a')[0]['title'])
    if len(value.find_all('p')) == 1:
        print(value.find_all('p')[0].string)
    else:
        print('None')
