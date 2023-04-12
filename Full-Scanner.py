#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
主程序

'''

h='\t\t\t  注意：输入-h/--help查看工具的使用\n'




from lib.cmdline import cmdline  # 图标
import judge
import platform
from colorama import init
init(autoreset=True)

if __name__ == '__main__':
    # 图标
    print(cmdline.banner())
    args = cmdline.help_h()
    judge=judge.whether()

#选择使用选择模式
    judge.G_(args.G)
#选择使用选择模式
    judge.GUI(args.GUI)  # GUI

# 被动信息收集
    # fofa
    judge.fofa_judge(args.fofa,args.cookie)

    # fofa_api
    judge.fofa_api_judge(args.fofaapi,args.key,args.email,args.size)

    # shodan
    judge.shodan_judge(args.shodan,args.api)

    # whois
    judge.whois_judge(args.whois,args)

    # bing
    judge.google_judge(args.bing, args)

    # DNS查询
    judge.SubDNS_judge(args.SubDNS, args)

    # google
    judge.Google_judge(args.google,args)
# 主动信息收集
    #cms探测
    judge.CmsVulScan_judge(args.cms)


    # 备份文件扫描
    judge.BP_judge(args.PB,args.PBm,args)

    #后台扫描
    judge.BK_judge(args.BK,args.BKm,args)

    #端口扫描
    judge.PS_judge(args.PS, args)
# 爆破

    # 登录界面自动化破解
    judge.webcrack_judge(args.crack)

    # ftp
    judge.ftp_judge(args.ftp,args)

    # ssh
    judge.ssh_judge(args.ssh, args)

    # Mysql
    judge.mysql_judge(args.mysql, args)

# 其他

    #端口对应服务查询

    judge.portquery_judge(args.tcp,args)
    judge.portquery_judge(args.udp,args)

    #judge.Acting_judge(args.PSC)
    judge.Contentextraction_judge(args.mdns,args.mhttpdns)
# PE
    judge.PE_judge(args.PE,args.refresh,args.reset,args)
# 漏洞扫描
    judge.Rad_Xray(args.rxurl, args.mrx, args.rxdd)

    # awvs

    judge.Python_Awvs(args.AwvsUrl,args.AwvsAPI,args.AwvsFile,args.AwvsVelocity,args.AwvsTime,args.AwvsName,args.AwvsProxyIP,args.AwvsProxyPort,args.AwvsDingtalk)