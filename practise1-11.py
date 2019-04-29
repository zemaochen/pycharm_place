import requests
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        response = requests.get(url, timeout=15)#timeout限制请求时间
        response.raise_for_status()#如果发送了一个错误请求抛出异常
        response.encoding = response.apparent_encoding
        # print(html.status_code)
        return response.text
    except:
        print("页面访问异常")
def getIp(html):
    result = {}#存放结果
    try:
        soup = BeautifulSoup(html, "lxml")
        soupDiv = soup.find('div', attrs={'class': 'WhoIpWrap'})
        soupT = soup.find(attrs={'class': 'bg-blue08'})
        soupP = soupDiv.find(attrs={'class': 'bor-b1s'})
        data = soupP.find_all('span')
        title = soupT.find_all('span')
        for i in range(len(data)):
            key = title[i].text
            value = data[i].text
            result[key] = value
        soupRightDiv = soup.find('div', attrs={'class', 'IpMainWrap-right fr'})
        soupRightDl = soupRightDiv.find('dl', attrs={'class', 'IpMRig-tit'})
        dt = soupRightDl.find_all('dt')
        dd = soupRightDl.find_all('dd')
        for i in range(len(dt)):
            key = dt[i].text
            value = dd[i].text
            result[key] = value
        print(result)
    except:
        print("转换异常")
url = "http://ip.tool.chinaz.com/"
temp = input("请输入ip地址:")
getIp(getHtml(url + temp))#拼接url
# test:192.168.106.1