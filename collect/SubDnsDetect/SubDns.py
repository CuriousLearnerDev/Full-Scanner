from collect.SubDnsDetect import bing,fofa,crt,censys,ip138
#from lib.choose import UseStyle # 设置颜色
import ttkbootstrap as ttk

def DNS_Interface(args):

    keywords="site:"+args.SubDNS

    Dns_List=[] # 统计
    # -----------------------------------------------------------------------------
    print("正在用搜索引擎进行探测DNS")
    DNS_Bing=bing.DNS_Climb_bing(keywords,args.SubDNS) # bing搜索

    Dns_List+=DNS_Bing # 统计
    print('\n'.join(str(i.rstrip()) for i in DNS_Bing)) #一行循环输出搜索出来的结果

    # -----------------------------------------------------------------------------

    DNS_ip138=ip138.DNS_Climb_ip38(args.SubDNS) # ip38搜索

    diff_list = list(set(DNS_ip138) - set(Dns_List))  # 用于检查没有出来的域名进行输出

    Dns_List += DNS_ip138  # 统计

    print('\n'.join(str(i.rstrip()) for i in diff_list))  # 一行循环输出搜索出来的结果

    # -----------------------------------------------------------------------------
    print("正在用证书进行探测DNS")
    # DNS_censys = censys.DNS_Climb_censys(args.SubDNS)  # censys证书探测
    #
    # diff_list = list(set(DNS_censys) - set(Dns_List))  # 用于检查没有出来的域名进行输出
    #
    # Dns_List += DNS_censys  # 统计
    #
    # print('\n'.join(str(i.rstrip()) for i in diff_list))  # 一行循环输出搜索出来的结果

    #-----------------------------------------------------------------------------
    DNS_crt=crt.DNS_Climb_Crt(args.SubDNS)  # crt证书探测

    diff_list = list(set(DNS_crt) - set(Dns_List))  # 用于检查没有出来的域名进行输出

    Dns_List += DNS_crt # 统计

    print('\n'.join(str(i.rstrip()) for i in diff_list))  # 一行循环输出搜索出来的结果

    # -----------------------------------------------------------------------------
    # DNS_Fofa=fofa.Dns_Request(args.SubDNS) # fofa探测
    #
    # diff_list = list(set(DNS_Fofa) - set(Dns_List)) # 用于检查没有出来的域名进行输出
    #
    # Dns_List += diff_list  # 统计
    #
    # print('\n'.join(str(i.rstrip()) for i in diff_list))  # 一行循环输出搜索出来的结果

def GUI(DNS,result):
    keywords = "site:" + DNS
    result.insert(ttk.END, f"你输入的是：{DNS}\n")

    Dns_List = []  # 统计

    # -----------------------------------------------------------------------------
    result.insert(ttk.END, f"正在用搜索引擎进行探测DNS\n")
    DNS_Bing=bing.DNS_Climb_bing(keywords,DNS) # bing搜索

    Dns_List+=DNS_Bing # 统计

    for i in DNS_Bing:
        result.insert(ttk.END, i+'\n')
    # -----------------------------------------------------------------------------
    result.insert(ttk.END, f"正在用证书进行探测DNS\n")
    # DNS_censys = censys.DNS_Climb_censys(DNS)  # censys证书探测
    #
    # diff_list = list(set(DNS_censys) - set(Dns_List))  # 用于检查没有出来的域名进行输出
    #
    # Dns_List += DNS_censys  # 统计
    #
    # for i in diff_list:
    #
    #     result.insert(ttk.END, i+'\n')

    # -----------------------------------------------------------------------------
    DNS_crt = crt.DNS_Climb_Crt(DNS)  # crt证书探测

    diff_list = list(set(DNS_crt) - set(Dns_List))  # 用于检查没有出来的域名进行输出

    Dns_List += DNS_crt  # 统计

    for i in diff_list:
        result.insert(ttk.END, i+'\n')


    # -----------------------------------------------------------------------------
    result.insert(ttk.END, '完成！\n')