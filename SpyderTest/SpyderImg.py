import urllib.request
import re
# 获取网页源码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = r'src="([.*\S]*.jpg)" pic_ext="jpeg"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist
html = getHtml("http://tieba.baidu.com/p/3205263090")
html = html.decode("UTF-8")
imglist = getImg(html)
imgName = 0
for imagePath in imglist:
    f = open(str(imgName)+'.jpg', 'wb')
    f.write((urllib.request.urlopen(imagePath)).read())
    f.close()
    imgName += 1
    print('正在下载第%s张图片'%imgName)
print("下载完成")

