import requests
from urllib.parse import urlparse # urlparse提取url的dns
from lxml import etree


def DNS_Climb_ip38(domain):
    Dns_List = []  # 这个代码参考https://blog.csdn.net/qq_45859826/article/details/124030119
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'http://www.baidu.com/'
    }
    try:
        html = requests.get('https://site.ip138.com/' + domain + '/domain.htm', headers=headers)
        html = etree.HTML(html.text)
        divs = html.xpath(r'//div/div/p/a[@target="_blank"]/text()')  # 语法

        for DNS_Res in divs:

            if not (DNS_Res in Dns_List):  # 取反如果Dns_List列表里面有就不添加
                if domain in DNS_Res:  # 判断域名是否是指定的域名
                    Dns_List.append(DNS_Res)


    except Exception as bc:
        print("有错误！错误提示" + str(bc))

    return  Dns_List
    #print(Dns_List)

if __name__ == '__main__':
    DNS_Climb_ip38("jd.com")
