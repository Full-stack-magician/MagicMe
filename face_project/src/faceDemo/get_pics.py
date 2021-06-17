import urllib.request
import urllib.error
import urllib.response
import re
import bs4
import gzip
from io import BytesIO
import requests
import chardet
import certifi
import idna


def ask_url(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)
    html = ""
    respond = urllib.request.urlopen(request)
    respond = gzip.GzipFile(fileobj=BytesIO(respond.read()))
    html = respond.read().decode('UTF-8')
    # print(html)
    return html


findLink = re.compile(r'"objURL":"(.*?)"')


def get_pics(i, name):
    baseurl = "https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=" + name
    # baseurl = "http://xinhuanet.com/"

    dataList = []
    html = ask_url(baseurl)

    bs = bs4.BeautifulSoup(html, 'html.parser')
    pic_urls = re.findall(findLink, str(bs))
    j = 0
    for pic_url in pic_urls:
        # print(pic_url)
        if j < (len(pic_urls)) // 2:
            print("picsForTrain")
            pic = requests.get(pic_url, timeout=15)
            with open('./picsForTrain/' + str(i) + '.jpg', 'wb') as f:
                print('./picsForTrain/' + str(i) + '.jpg')
                f.write(pic.content)
        else:
            print("picsForTest")
            pic = requests.get(pic_url, timeout=15)
            with open('./picsForTest/' + str(i-((len(pic_urls)) // 2)) + '.jpg', 'wb') as f:
                f.write(pic.content)
        i += 1
        j += 1
    # for pic_url in enumerate(pic_urls):
    #     try:
    #         pic = requests.get(pic_url, timeout=15)
    #         string = str(i + 1) + '.jpg'
    #         with open(string, 'wb') as f:
    #             f.write(pic.content)
    #             print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
    #     except Exception as e:
    #         print('.图片/下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
    #         print(e)
    #         continue

    return dataList


def start():
    i = 30
    name = 'telangpu'
    get_pics(i, name)


if __name__ == "__main__":
    start()
