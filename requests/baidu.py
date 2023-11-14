import requests
from bs4 import BeautifulSoup

from module import Common

url = r'https://top.baidu.com/board?tab=realtime'

head = {
    'Cookie': Common.get_cookie_txt('baidu_cookie'),
    'User-Agent': Common.get_random_user_agent()
}

res_text = requests.get(url, headers=head).text

# 格式化
# res_soup = BeautifulSoup(res_text, features='lxml').prettify()

res_soup = BeautifulSoup(res_text, "lxml")

elements = res_soup.findAll('div', class_='category-wrap_iQLoo horizontal_1eKyQ')
print(len(elements))

for index, value in enumerate(elements):
    print(index + 1)
    # print(value)
    print(value.findAll('div', class_='c-single-text-ellipsis')[0].string)
    if len(value.findAll('div', class_='hot-desc_1m_jR small_Uvkd3 ellipsis_DupbZ')) >= 1:
        print(value.findAll('div', class_='hot-desc_1m_jR small_Uvkd3 ellipsis_DupbZ')[0].text)
    else:
        print('None')
