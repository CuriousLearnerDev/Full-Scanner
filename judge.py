#from collect.search_engine import main


#from lib.choose_model import Big_Category

# from Activelibrary.backgroundscan import mian



class whether():
    # 选择使用选择模式
    def G_(self,G):
        if G==True:
            from lib.choose_model import Big_Category
            Big_Category.Category()
    def GUI(self,Gui):
        if Gui==True:
            from lib.GUI import cs
    # 被动信息收集
    # fofa_
    def fofa_judge(self,Fofa_Parameter, Cookie):
        try:
            if Fofa_Parameter != None:
                from collect import fofa
                fofa.Interface(Fofa_Parameter, Cookie)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    def fofa_api_judge(self, Fofa_api_fofaapi, Fofa_api_key,Fofa_api_email,Fofa_api_size):
        if Fofa_api_fofaapi != None:
            from collect import fofa_api

            fofa_api.Interface(Fofa_api_fofaapi,Fofa_api_key,Fofa_api_email,Fofa_api_size)
            #print(Fofa_api_size)
            #print(Fofa_api_fofaapi)

    # shodan搜索
    def shodan_judge(self,Shodan_Parameter, api):
        # try:
        if Shodan_Parameter != None:
            from collect import shodan
            shodan.shod(Shodan_Parameter, api)
        # except Exception as bc:
        #     print("有错误！错误提示" + str(bc))

    # whois查询
    def whois_judge(self,whois_Parameter,args):

        try:
            if whois_Parameter != None:
                from collect import req_whois
                req_whois.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    # bing提取
    def google_judge(self,google_Parameter,args):

        if google_Parameter !=None:
            from collect import bing
            bing.Interface(args)

    # dns
    def SubDNS_judge(self,SubDNS_Parameter,args):

        if SubDNS_Parameter!=None:
            from collect.SubDnsDetect import SubDns
            #print(SubDNS_Parameter)
            SubDns.DNS_Interface(args)
    # Google
    def Google_judge(self,SubDNS_Parameter,args):

        if SubDNS_Parameter!=None:
            from collect import google
            #print(SubDNS_Parameter)
            google.Interface(args)
    # # 主动信息收集

    # cms识别
    def CmsVulScan_judge(self,Cms_Parameter):


        try:
            if Cms_Parameter!=None:
                from thirdparty.CmsVulScan import CmsVulScan
                CmsVulScan.Interface(Cms_Parameter)
        except Exception as bc:
                print("有错误！错误提示" + str(bc))

    # 备份文件扫描
    def BP_judge(self,BP,BPm,args):

        #try:
        if BP != None: # 单个扫描
            from Initiative.Backupfilescan import ProbeBackup
            ProbeBackup.Interface(args)

        elif BPm!=None: # 批量扫描
            from Initiative.Backupfilescan import ProbeBackup
            ProbeBackup.Interface(args)

        # except Exception as bc:
        #     print("有错误！错误提示" + str(bc))

    # 后台扫描
    def BK_judge(self,BK,BKm,args):

        # try:
        if BK != None:
            from Initiative.backgroundscan import back
            back.Interfacemian(args)
        elif BKm != None:  # 批量扫描
            from Initiative.backgroundscan import back
            back.Interfacemian(args)
        # except Exception as bc:
        #         print("有错误！错误提示" + str(bc))

    # 端口扫描
    def PS_judge(self,PS,args):

        try:
            if PS != None:
                from Initiative.portscan import port
                port.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))



    # 暴力破解
    # 登录界面爆破
    def webcrack_judge(self,Crack_Parameter):


        try:
            if Crack_Parameter!=None:
                from thirdparty.extracted import webcrack
                webcrack.Interface(Crack_Parameter)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))
    #
    #  Ftp爆破
    def ftp_judge(self,Ftpcrack_Parameter,args):

        #try:
        if Ftpcrack_Parameter !=None:
            from blasting.ftp_blasting import ftp
            ftp.fill_in(args)
        # except Exception as bc:
        #     print("有错误！错误提示" + str(bc))

    #  ssh爆破
    def ssh_judge(self,ssh_crack,args):

        try:
            if ssh_crack !=None:
                from blasting.ssh_blasting import ssh
                #print(ssh_crack)
                ssh.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    def mysql_judge(self,mysql,args):
        if mysql != None:
            from blasting.mysql_blasting import mysql
            # print(ssh_crack)
            mysql.Interface(args)

    # # 其他
    # 端口对应服务查询
    def portquery_judge(self,Portquery_Parameter,args):

        if Portquery_Parameter!=None:
            from other.portquery import potrquery
            potrquery.Interfacemian(args)

    # 文件的中的域名提取
    def Contentextraction_judge(self,mdns_Parameter, mhttp_Parameter):


        # 光提取文件中的域名/IP、比如文件有一个http://1.1.1.1/x/x/x/x、提取出来的就是1.1.1.1
        if mdns_Parameter != None:
            from other.Contentextraction import extraction
            extraction.Interface_dns(mdns_Parameter)

        # 取文件中的和[http/https://]+域名、比如文件有一个http://1.1.1.1/x/x/x/x、提取出来的就是http://1.1.1.1
        elif mhttp_Parameter!=None:
            from other.Contentextraction import extraction
            extraction.Interface_http(mhttp_Parameter)


    # def Acting_judge(self,PSC_Parameter):
    #     from other.acting import Agentmian
    #     if PSC_Parameter != False:
    #         print("dsads")


    # POC/EXP
    def PE_judge(self,PEP_Parameter,refresh_Paramete,reset_Paramete,args):


        if PEP_Parameter!=False: #使用POC/EXP
            from PocAndExpScript import storage # 调用
            storage.whether(args)

        elif refresh_Paramete!=False: # 更新POC/EXP
            from PocAndExpScript import main
            main.Interface()

        elif reset_Paramete!=False: # 重置
            from PocAndExpScript import main
            main.default()

# 漏洞扫描
    def Rad_Xray(self,RXURL,MRX,RXDD):
        if RXURL != None:
            from leakscan.rad_xray_py import rad_xray
            rad_xray.main(RXURL,MRX,RXDD)
        elif MRX !=None:
            from leakscan.rad_xray_py import rad_xray
            rad_xray.main(RXURL,MRX,RXDD)
    def Python_Awvs(self,AwvsUrl,AwvsAPI,AwvsFile,AwvsVelocity,AwvsTime,AwvsName,AwvsProxyIP,AwvsProxyPort,AwvsDingtalk):
        if AwvsUrl !=None:
            from leakscan.awvs import python_awvs
            python_awvs.mian(AwvsUrl,AwvsAPI,AwvsFile,AwvsVelocity,AwvsTime,AwvsName,AwvsProxyIP,AwvsProxyPort,AwvsDingtalk)