import urllib.request
url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&pvid=8d9fc16562984f179809d03f049a60fc'
#发送请求
request = urllib.request.Request(url)
#打开和读取URL请求并抓取网页内容
response = urllib.request.urlopen(request)
data = response.read()
# 设置解码方式
data = data.decode('utf-8')
# 打印结果
print(data)