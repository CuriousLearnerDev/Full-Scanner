






***
> github项目地址：[https://github.com/Zhao-sai-sai/Full-Scanner](https://github.com/Zhao-sai-sai/Full-Scanner)
>
> gitee项目地址：[https://gitee.com/wZass/Full-Scanner](https://gitee.com/wZass/Full-Scanner)

## 工具简介

做挖漏洞渗透测试有的时候要去用这个工具那个工具去找感觉麻烦我自己就写了一个简单的整合工具，有互联网大佬不要喷我，我也是废物 

Full-Scanner是一个多功能扫描工具，支持被动/主动信息收集，漏洞扫描，常见的POC和EXP

写这个工具花费了很多时间和精力这工具几乎全部是独立编写，这个工具是去年3月开始写的，已经将近一年了，写的时候也是断断续续三天打鱼两天晒网，因为不是做开发的，工具里面写的代码也是很垃，作者我英文也是废物，变量名起的也很随意<img src="https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/img/bqb.png" height="50xp" ><p/> 

有两个小模块一个cms识别一个web登录界面破解用的下面这两个项目

> 用到的工具项目地址

- https://github.com/yzddmr6/WebCrack
- https://github.com/F6JO/CmsVulScan



## Full-Scanner的拆分

Full-Scanner的拆分工具里面的单独工具

> 下面这几个是已经开发好的工具可以使用的
- 网站备份文件扫描工具下面地址：https://github.com/Zhao-sai-sai/Full_Scanner_ProbeBackup
- 后台扫描工具项目地址：https://github.com/Zhao-sai-sai/Full_Scanner_back
- 编码解码GUI小工具项目地址：https://github.com/Zhao-sai-sai/Full-Scanner_Encodeanddecode

## 目录结构

现在的目录结构

```bash
Full-Scanner
├── Full-Scanner.py # main
├── judge.py # 判断输入的命令
├── blasting # 爆破的一些脚本
│   ├── mysql_blasting #mysql爆破
│   │   ├── mysql.py
│   ├── ftp_blasting # ftp破解
│   │   ├── ftp.py
│   └── ssh_blasting # ssh破解
│       └── ssh.py
├── collect  # 被动搜集的一些脚本
│   ├── bing.py # bing搜索提取
│   ├── fofa.py # fofa搜索结果提取
│   ├── fofa_api.py # fofa的API搜索结果提取
│   ├── req_whois.py # whois查询
│   └── shodan.py # shodan信息收集
│   ├── google.py # 谷歌搜索提取
│   └── SubDnsDetect # 个采用的一些搜索引擎进行域名探测
│       ├── bing.py # 用的bing行域名探测
│       ├── censys.py # 用的censys的证书进行域名探测
│       ├── crt.py # 用的crt证书进行域名探测
│       ├── fofa.py # 用的fofa进行域名探测
│       ├── ip138.py # 使用138域名查询
│       └── SubDns.py # mian
├── conf # 配置文件
│   ├── config.py
├── dictionary # 存在着字典
│   ├── back 
│   ├── BackgroundDetection
│   ├── Backupfilescan
│   ├── extracted
│   ├── ftp
│   └── ssh
│   ├── mysql
├── Initiative # 主动信息收集的一些脚本
│   ├── backgroundscan # 后台扫描
│   │   ├── back.py
│   ├── Backupfilescan # 备份文件扫描
│   │   ├── ProbeBackup.py
│   └── portscan # 端口扫描
│       ├── port.py
├── leakscan #漏洞扫描
│   ├── awvs # python联动awvs 钉钉推送
│   │   └── python_awvs.py
│   ├── rad_xray_py # rad联动xray 钉钉推送
│   │   └── rad_xray.py
│   └── xray # xray文件的目录
│       ├── ca.crt
│       ├── ca.key
│       ├── config.yaml
│       ├── module.xray.yaml
│       ├── plugin.xray.yaml
│       ├── rad
│       ├── rad_config.yml
│       ├── readme.txt
│       ├── xray
│       └── xray.yaml
├── lib # 脚本需要的一些脚本
│   ├── GUI # GUI
│   │   ├── blasting # 爆破破解GUI
│   │   │   ├── crack_gui.py # 网页登录破解
│   │   │   ├── ftp_gui.py  # ftp破解
│   │   │   ├── mysql_gui.py #mysql破解
│   │   │   └── ssh_gui.py # ssh破解
│   │   ├── cs.py # 主GUI
│   │   ├── Information_Collection # 信息收集GUI
│   │   │   ├── back_gui.py # 后台扫描器
│   │   │   ├── Backupfilescan_gui.py # 备份文件扫描
│   │   │   ├── bing_gui.py # bing爬虫
│   │   │   ├── fofa_gui.py #  fofa搜索
│   │   │   ├── google_gui.py # google爬虫
│   │   │   ├── Port_scanning_gui.py #  端口扫描
│   │   │   ├── shodan_gui.py # shodan
│   │   │   ├── SubDns_gui.py # 子域名探测
│   │   │   └── whois_gui.py # whois查询
│   │   ├── leakscan # 漏洞扫描GUI
│   │   │   ├── Python_Awvs_gui.py
│   │   │   ├── Rad_and_Xray_dingtalk_gui.py
│   │   │   ├── Rad_and_Xray_gui.py
│   │   │   └── Single_Rad_and_Xray_gui.py
│   │   └── Utilities.py  # 实用小工具
│   │   ├── Coding_tools.py # 编码工具
│   ├── Auxiliary.py  # 杂东西
│   ├── choose.py  # 调用颜色
│   ├── cmdline
│   │   ├── cmdline.py # 命令行参数和图标
│   ├── choose_model  # 选项模式
│   │   ├── Big_Category.py
│   │   └── sub_options
│   │       ├── Active_Options.py
│   │       ├── blasting_Options.py
│   │       ├── Passive_Options.py
├── other # 其他脚本
│   ├── Contentextraction # 小工具：文件的中的域名提取
│   │   ├── extraction.py
│   └── portquery # 小工具：端口查询对应的服务
│       ├── potrquery.py
│       └── tcpudp.py
├── PocAndExpScript # 自己脚本或者POCEXP生成到工具里面
│   ├── generate #自己的脚步
│   │  
│   ├── main.py # 生成文件的关键文件 
│   ├── pecmdline
│   │   ├── pecmdline.py　# 命令行参数
│   ├── storage.py # 调研判断类似上面的 ├── judge.py # 判断输入的命令
│   └── storage.txt # 添加语法多次添加
├── result # 用于存放扫描下来的结果
│   ├── back
│   ├── cms
│   ├── fofa
│   ├── ftp
│   ├── ProbeBackup
│   ├── searchengine
│   ├── shodan
│   ├── ssh
│   ├── webcrack
│   └── whois
└── thirdparty # 用到的其他人写的工具
```

## GUI界面

![f0a7331054f193ceb3a91e8d5265390](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/img/f0a7331054f193ceb3a91e8d5265390.jpg)

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/2023-02-09_18-27.png)

![image-20230228203022826](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/img/image-20230228203022826.png)

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/2023-02-09_18-26.png)

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/img/ld.png)

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/2023-02-28_20-23.png)

![image-20230302104804945](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/img/image-20230302104804945.png)

## 工具下载

```bash
git clone  https://github.com/Zhao-sai-sai/Full-Scanner.git
```
## 安装一些依赖

```bash
fcd Full-Scanner
pip install -r requirements.txt
```
## 工具的使用

**命令行B站演示：**https://www.bilibili.com/video/BV1ga411976w

```bash
************************************************************



         __|    | |       __|                              
         _||  | | |____|\__ \  _|  _` |   \    \   -_)  _| 
        _|\_,_|_|_|     ____/\__|\__,_|_| _|_| _|\___|_|  



作者：w啥都学Blog地址：www.zssnp.top
gitee项目地址：https://gitee.com/wZass/Full-Scanner
github项目地址：https://github.com/Zhao-sai-sai/Full-Scanner
 ************************************************************                              
usage: python3 Full-Scanner.py [参数] [目标] [其他参数]

本程序是一个多功能工具、支持信息收集、爆破、漏洞扫描、常见的POC和EXP

options:
  -h, --help            show this help message and exit

选择模式:
  如果不喜欢输入命令那样、可以用下面的参数
  -G                    选择使用选择模式(已经抛弃)
  -GUI                  图形化模式
[1][*]被动信息收集:
  下面是常见的被动信息收集方法会利用各大搜索引擎
[1]被动信息收集：[1]fofa搜索结果提取没有会员用户使用:
  -fofa [IP/域名]         fofa搜索结果提取  -Cookie [Cookie值]     Cookie需要验证、如果不想每次都指定可以去config.py文件里面添加
[1]被动信息收集：[1]fofa搜索结果提取会员用户使用:
  -fofaapi [IP/域名]      fofa搜索结果提取  -key [api key]        api key值、如果不想每次都指定可以去config.py文件里面添加  -email [email邮箱]      用户email邮箱、如果不想每次都指定可以去config.py文件里面添加  -size [数量]            每页查询数量，默认为100

[1]被动信息收集：[2]shodan信息收集:
  -shodan [[IP]]        shodan信息收集  -api [api值]           用-API参数指定、如果不想每次都指定可以去config.py文件里面添加
[1]被动信息收集：[3]whois查询:
  -whois [域名]           whois查询、咧-whois https://www.baidu.com/

[1]被动信息收集：[4]搜索引擎爬虫:
  下面这个会用一下搜索引擎进行搜索提取搜索的URL

  -bing [查询语句]          搜索引擎爬虫、咧 -bing 'intitle:后台登陆 "学院"'
  -bingm [提取的页数]        可选！提取的页数如果不指定默认就是100000、咧 -bingm 5

[1]被动信息收集：[5]搜索引擎爬虫:
  下面这个会用一下搜索引擎进行搜索提取搜索的URL

  -google [查询语句]        搜索引擎爬虫、咧 -google 'intitle:后台登陆 "学院"'
  -googlem [提取的页数]      提取的页数如果不指定默认就是100000、咧 -google 5
  -googlep [代理地址]       设置代理、咧 -googlep 127.0.0.1:8080

[1]被动信息收集：[6]子域名查询:
  这个采用的一些搜索引擎进行域名探测有bing、138、crtsh、fofa、censys等、不需要输入API这个是采集的查询结果的页面进行提取的
  -SubDNS [域名]          子域名查询
[2][*]主动信息收集:
  下面是常见的主动信息收集方法
[2]主动信息收集：[1]目标cms识别:
  -cms [URL]            目标cms识别
[2]主动信息收集：[2]备份文件扫描:
  -PB [URL]             备份文件扫描 指定扫描的目标、比如 -PB https://baidu.com/
  -PBm [文件名]            可选！多个目标保存到一个文件里面进行批量扫描  -PBt [线程数]            可选！指定线程默认是1
  -PBd [字典文件]           可选！指定字典默认是自己生成  -PBp [代理地址]           可选！可选代理地址
[2]主动信息收集：[3]后台扫描:
  -BK [URL]             后台扫描、指定扫描的目标、比如 -BK https://baidu.com/
  -BKm [文件名]            可选！多个目标保存到一个文件里面进行批量扫描  -BKd [字典文件]           可选！指定字典默认是用的php.txt
  -BKt [线程数]            可选！指定线程默认是30
  -BKp [代理地址]           可选！设置代理
[2]主动信息收集：[4]端口扫描:
  -PS [IP]              端口扫描、比如 -PS 1.1.1.1
  -PSp [指定端口]           可选！指定端口、如果不指定默认常见的端口、指定比如-PSp 1-65535或者22,80,3306
  -PSt [线程数]            可选！指定线程、线程太多会出问题
[3][*]爆破:
  下面是常见、web爆破、和服务的爆破
[3]爆破：[1]网页登录界面自动化破解:
  -crack [URL]          登录界面自动化破解、比如-crack https://xxx.com/admin.php

[3]爆破：[2]ftp爆破:
  -ftp [目标地址]           ftp爆破、比如-ftp 1.1.1.1
  -ftpp [指定端口号]         可选！指定端口默认21
  -ftpt [线程数]           可选！指定线程默认线程1
  -ftpadmin [文件名]       可选！指定用户字典、不指定使用默认  -ftppasswd [文件名]      可选！指定密码字典、不指定使用默认
[3]爆破：[3]SSH破解:
  -ssh [目标地址]           ssh密码怕破解、比如 -ssh 1.1.1.1
  -sshp [指定端口号]         可选！指定端口、默认端口号22
  -sshu [指定字典]          可选！指定用户名字典、不指定使用默认字典  -sshd [指定字典]          可选！指定密码字典、不指定使用默认字典  -ssht [线程数]           可选！指定线程、线程太多会出问题、默认线程5

[3]爆破：[4]Mysql破解:
  -mysql [目标地址]         Mysql密码怕破解、比如 -Mysql 1.1.1.1
  -mysqlp [指定端口号]       可选！指定端口、默认端口号3306
  -mysqlu [指定字典]        可选！指定用户名字典、不指定使用默认字典  -mysqld [指定字典]        可选！指定密码字典、不指定使用默认字典  -mysqlt [线程数]         可选！指定线程、线程太多会出问题、默认线程5

[4][*]漏洞扫描:

[4]漏洞扫描：[1]Rad联动Xray (目前只支持amd_linux):
  -RXURL [URL]          请输入目标地址  -MRX [文件名]            批量文件  -MRXDD [token]        可选！钉钉推送的token，不想每次都添加可以去config配置文件里面添加
[4]漏洞扫描：[2]AWVS批量扫描:
  -AwvsUrl [URL]        AWVS的服务地址  -AwvsAPI [API]        AWVS的API
  -AwvsFile [文件]        指定批量扫描的文件  -AwvsVelocity [速度]    可以设置三个，slow、moderate、fasts，说明：slow(慢)、moderate(中)、fasts(快)
  -AwvsTime [秒]         设置多少秒添加一个扫描任务  -AwvsName [名字]        可选！扫描备注名  -AwvsProxyIP [IP]     可选！代理IP
  -AwvsProxyPort [端口]   可选！代理端口  -AwvsDingtalk [token]
                        可选！钉钉推送的token，扫描状态和漏洞状态钉钉推送，不想每次都添加可以去config配置文件里面添加
[*]其他：小工具:

小工具：端口查询对应的服务:
  -tcp [端口]             tcp查询  -udp [端口]             udp查询
小工具：文件的中的域名提取:
  -mdns [文件]            光提取文件中的域名/IP、比如文件有一个http://1.1.1.1/x/x/x/x、提取出来的就是1.1.1.1
  -mhttpdns [文件]        取文件中的和[http/https://]+域名、比如文件有一个http://1.1.1.1/x/x/x/x、提取出来的就是http://1.1.1.1

添加POCEXP或者自己的脚步:
  -PE [PE]              使用POC/EXP
  -refresh [REFRESH]    刷新添加POC/EXP
  -reset [RESET]        清空POC/EXP

```

## 导入自己的脚本

叫文件方到`PocAndExpScript/generate`
导入的时候他会按照下面的方式进行导入
比如

```bash
# filename漏洞编号，这个将变成命令参数使用最好不要用中文
# main这个就是接口函数
# name 这个是这个漏洞代码的说明
# important就是必要要用的参数
# 其他的都会当做参数来用

he_lp={
    'filename':'CVE-2022-26134', # filename漏洞编号，这个将变成命令参数使用最好不要用中文
    'main':'main', # main这个就是接口函数
    'name':'CVE-2022-26134Confluence远程命令执行漏洞', # name 这个是这个漏洞代码的说明
    'important':['u'], # important就是必要要用的参数
    'u':'目标', # 其他的都会当做参数来用
    .......
}
```

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github%2FFullScanner%2Fyanshi222.gif)

## 已知问题

> 应为我系统是linux系统在linux运行测试的比较多，Windows系统可能会出现很多问题

1. Windows会出现读取文件编码问题程序报错、解决方法修改文件的编码格式
2. Windows系统会出现多线程无法Ctrl+c结束程序的问题、这个我在找解决方法、linux不会出现这个问题
3. 爬虫问题、在信息收集可能会用到外国的网站、使用工具可能会卡在那访问不了、解决方法开代理
4. 有的工具不能用了或者报错、问题原因可能就是我调用那个网站的界面改了导致爬虫爬取不到、这个问题我会在测试的时候碰见了我会重新写爬取策略

## 使用截图

> 就下面这几个参数可以用bug还多,我太难了
>
>  <img src="https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/bqbwq.gif" height="50xp" ><p/> 

> 界面我用来两种格式
 - 默认是参数模式
 - -GU I#图像


  ![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/mian333.png)

![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/dns.png)

![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github%2FFullScanner%2Fsb111.png)

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github%2FFullScanner%2Fbing.png)

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github%2FFullScanner%2Ffofaapi.png)

![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/crack111.png)



![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/wh.png)

![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/cms111.png)



![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/c111.png)


![mian](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github/FullScanner/b111.png)

![](https://zssnp-1301606049.cos.ap-nanjing.myqcloud.com/github%2FFullScanner%2Fdr.png)

## 警告

***
### 请勿用于非法用途！否则自行承担一切后果
