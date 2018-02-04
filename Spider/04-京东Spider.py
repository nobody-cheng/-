"""
https://list.jd.com/list.html?cat=9987,653,655
https://list.jd.com/list.html?cat=9987,653,655&page=2&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main
https://list.jd.com/list.html?cat=9987,653,655&page=3&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main
https://list.jd.com/list.html?cat=9987,653,655&page=4&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main
"""
import urllib.request


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


def jdSpider(url0, beginPage, endPage):
    for i in range(beginPage, endPage + 1):
        page = i
        filename = "京东手机第" + str(page) + "页.html"
        if page == 1:
            url = url0
            html = loadPage(url, filename).decode('ascii', 'ignore')
        else:
            url = url0 + "&page=%s" % page + url2
            html = loadPage(url, filename).decode('ascii', 'ignore')
        writeFile(html, filename)


if __name__ == '__main__':
    url0 = "https://list.jd.com/list.html?cat=9987,653,655"
    url2 = "&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main"
    beginPage = int(input("请输入开始页:"))
    endPage = int(input("请输入结束页"))
    jdSpider(url0, beginPage, endPage)
