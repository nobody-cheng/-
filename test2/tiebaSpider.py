"""
http: // tieba.baidu.com / f?kw = lol & ie = utf - 8 & pn = 0

http: // tieba.baidu.com / f?kw = lol & ie = utf - 8 & pn = 50

http: // tieba.baidu.com / f?kw = lol & ie = utf - 8 & pn = 100

"""
import urllib.parse
import urllib.response, urllib.request


def loadPage(url, filename):
    """
    根据url发送请求,获取服务器响应文件
    :param url: 请求路径
    :param filename: 文件名
    :return:
    """
    print("正在下载" + filename)

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read()


def writeFile(html, filename):
    """
    保存服务器响应文件到本地磁盘文件里
    :param html: 服务器响应文件
    :param filename: 本地磁盘文件名
    :return:
    """
    print("正在存储" + filename)
    with open(filename, "w") as f:
        f.write(html)
    print("*" * 20)


def tiebaSpider(url, beginPage, endPage):
    """
    负责处理URL,分配每个URL去发送请求
    :param url:
    :param beginPage: 爬虫执行的开始页面
    :param endPage:   爬虫执行的截止页面
    :return:
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        # 组合完整的URL,并且pn值每次增加50
        fullurl = url + "& pn = " + str(pn)

        # 调用loadPage()发送请求获取html页面
        html = loadPage(fullurl, filename).decode('ascii')
        # 获取的HTML写入本地磁盘文件
        writeFile(html, filename)


if __name__ == '__main__':
    kw = input("请输入需要爬取的贴吧:")
    # 输入起始页,str转为int
    beginPage = int(input("请输入开始页:"))
    endPage = int(input("请输入结束页"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})

    # url: http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider(url, beginPage, endPage)
