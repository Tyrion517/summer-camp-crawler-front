import json
import requests
from bs4 import BeautifulSoup


def get_title_addr(URL: str, selector: str, encoding='utf-8') -> dict:
    """

    :param URL: 要爬的网站
    :param selector: 要爬的元素，用于筛选
    :param encoding: 编码格式，默认为utf-8.要与目标网站header里的charset一致，否则出现乱码
    :return: 标题和网址为键值对的字典
    """
    resp = requests.get(URL)  # 获取网页数据
    resp.encoding = encoding
    soup = BeautifulSoup(resp.text, 'lxml')  # 解析resp
    data = soup.select(selector)  # 选择需要的信息
    result = {}
    for i in range(len(data)):
        title = data[i].text.strip()
        addr = URL + data[i].get("href")  # href为相对地址，所以前要加URL
        if title:
            result.update({f'{title}': f'{addr}'})  # 储存到字典中去
    return result

# 保存信息到json文件
with open("data.json", "r+") as f:
    result = get_title_addr('https://xly.ustc.edu.cn', 'div.top10 ul li a', 'gbk')
    json.dump(result, f)

