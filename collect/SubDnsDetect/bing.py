# -- coding:UTF-8 --
import requests
from lxml import etree
import urllib3
from urllib.parse import urlparse # urlparse提取url的dns

urllib3.disable_warnings()  # 忽略https证书告警

def DNS_Climb_bing(keywords,DNS):
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    amount = 5 # 默认页数
    Dns_List=[]
    for i in range(0, int(amount)):
        url = f"https://cn.bing.com/search?q={keywords}&PC=U316&first={i}0&FORM=PERE"
        try:
            html = requests.get(url=url, headers=headers, verify=False, timeout=5)
            # //div[@id="search"]//div//div//div//div//div//div/a[@data-ved]/@href
            html = etree.HTML(html.text)
            divs = html.xpath(r'//div/h2/a/@href')  # 语法


            #print(divs2)
            for i in divs:
                if DNS in i:
                    DNS_Res = urlparse(i).netloc #　获得url里面的域名
                    if not(DNS_Res in Dns_List): # 取反如果Dns_List列表里面有就不添加

                        if DNS in DNS_Res: # 判断域名是否是指定的域名

                            Dns_List.append(DNS_Res)

        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    return Dns_List

if __name__=="__main__":

    DNS=DNS_Climb_bing("site:zssnp.top",'zssnp.top')
    for i in DNS:
        print(i)