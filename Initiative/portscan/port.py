# -*- coding:utf-8 -*-
#导入库
import ttkbootstrap as ttk
import socket
import time
import argparse
import queue
import threading
from lib.choose import UseStyle # 设置颜色
from colorama import init



GUT_output=0 # 输出到GUI
GUT_Sure=0 # 判断是否用到GUI
GUI_state=0 # GUI扫描进度

count = 1 # 记录请求多少次

schedule=1 # 记录端口数量

import time
time_start = time.time()  # 记录开始时间
# function()   执行的程序
time_end = time.time()  # 记录结束时间
time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s

def current_time():
    return time.strftime("[%Y-%m-%d_%H:%M:%S]: [*]", time.localtime())


def socketk(Host,Port_):
    global GUT_output # 输出到GUI
    global GUT_Sure # 判断是否用到GUI


    global schedule  # 记录端口数量
    global count# 记录请求多少次

    global GUI_state  # 状态栏扫描进度

    while not Port_.empty():
        port=Port_.get()
        # 域名解析
        Host=socket.gethostbyname(Host)

        # 创ipv4,和TCP类型的建套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #发送信息
        s.settimeout(1) # 设置超时时间
        #print(port)
        try:
            s.connect((Host,int(port)))

            if GUT_Sure==1:
                GUT_output.insert(ttk.END, f'开发端口：{port}\n')
                GUI_state['value'] += 1

            else:
                #s.recv(4096)
                print(UseStyle(f'\n\n开发端口：{port}\n', fore='green'))
            count += 1
        except :
            if GUT_Sure == 1:
                GUI_state['value'] += 1
            else:
                print(f"\r{current_time()}正在扫描。。。。。", end='')
            #pass

        #关闭套接字
        s.close()

# 多线程
def Thread(Host,Port_,T):
    threadpool = []
    for _ in range(int(T)):
        Threads = threading.Thread(target=socketk, args=(Host,Port_, ))
        threadpool.append(Threads)
    for th in threadpool:
        th.start()
    for th in threadpool:
        threading.Thread.join(th)


def splicing(args_host,args_port,args_thread):
    global GUT_output # 输出到GUI
    global GUT_Sure # 判断是否用到GUI

    global schedule # 记录端口数量
    schedule=0
    port = queue.Queue()
    # 默认线程
    if args_thread == None or args_thread == '':
        args_thread = 1
        thread_default = "默认线程：1"
    else:
        thread_default = "当前指定的线程数：" + str(args_thread)
    # 默认端口
    if args_port == None or args_port == '':

        args_port = ['0', '1', '2', '3', '5', '7', '9', '11', '13', '17', '18', '19', '20', '21', '22', '23', '24',
                     '25', '27', '29', '31', '33', '35', '37', '38', '39', '41', '42', '43', '44', '45', '46', '47',
                     '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63',
                     '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79',
                     '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '96',
                     '97', '98', '99', '100', '101', '102', '103', '105', '106', '107', '108', '109', '110', '111',
                     '112', '113', '114', '115', '116', '117', '118', '119', '121', '122', '123', '128', '129', '130',
                     '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '143', '144', '145',
                     '149', '150', '152', '156', '158', '159', '160', '161', '162', '163', '164', '166', '169', '170',
                     '177', '178', '179', '180', '181', '184', '185', '186', '187', '189', '190', '191', '192', '193',
                     '194', '197', '198', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210',
                     '211', '213', '218', '219', '220', '223', '224', '241', '245', '246', '257', '258', '259', '260',
                     '261', '266', '267', '268', '281', '282', '286', '308', '313', '318', '333', '344', '345', '346',
                     '347', '348', '358', '359', '362', '363', '372', '373', '374', '376', '377', '378', '379', '380',
                     '381', '382', '383', '384', '385', '386', '387', '389', '395', '396', '400', '401', '402', '406',
                     '408', '409', '410', '411', '412', '413', '414', '415', '423', '424', '425', '427', '434', '435',
                     '443', '444', '445', '446', '447', '448', '456', '458', '459', '464', '469', '470', '472', '481',
                     '487', '489', '491', '499', '500', '509', '510', '512', '513', '514', '515', '516', '518', '519',
                     '520', '525', '526', '529', '530', '531', '532', '533', '534', '537', '542', '543', '544', '546',
                     '547', '552', '554', '555', '556', '563', '564', '565', '566', '567', '568', '569', '570', '571',
                     '572', '573', '574', '581', '582', '583', '584', '585', '586', '587', '589', '595', '597', '598',
                     '599', '600', '601', '604', '606', '608', '609', '610', '611', '612', '613', '614', '615', '616',
                     '617', '619', '620', '623', '624', '631', '633', '637', '641', '647', '648', '649', '666', '808',
                     '1001', '1011', '1024', '1025', '1026', '1027', '1030', '1031', '1033', '1034', '1036', '1070',
                     '1071', '1074', '1080', '访问INTERNET', '1110', '1125', '1203', '1204', '1206', '1222', '1233',
                     '1234', '1243', '1245', '1273', '1289', '1290', '1333', '1334', '1335', '1336', '1349', '1350',
                     '1371', '1372', '1374', '1376', '1377', '1378', '1380', '1381', '1386', '1387', '1388', '1389',
                     '1390', '1391', '1392', '1393', '1394', '1395', '1396', '1397', '1398', '1399', '1433', '1434',
                     '1492', '1509', '1512', '1524', '1600', '1645', '1701', '1731', '1801', '1807', '1900', '1912',
                     '1981', '1999', '2000', '2001', '2003', '2023', '2049', '2115', '2140', '2500', '2504', '2565',
                     '2583', '2801', '2847', '3024', '3128', '3129', '3150', '3210', '3306', '3333', '3389', '3456',
                     '3457', '3527', '3700', '3996', '4000', '4060', '4092', '4133', '4134', '4141', '4142', '4143',
                     '4145', '4321', '4333', '4349', '4350', '4351', '4453', '4454', '4455', '4456', '4457', '4480',
                     '4500', '4547', '4555', '4590', '4672', '4752', '4800', '4801', '4802', '4848', '4849', '4950',
                     '5000', '5001', '5006', '5007', '5022', '5050', '5051', '5052', '5137', '5150', '5154', '5190',
                     '5191', '5192', '5193', '5222', '5225', '5226', '5232', '5250', '5264', '5265', '5269', '5306',
                     '5321', '5400', '5401', '5402', '5405', '5409', '5410', '5415', '5416', '5417', '5421', '5423',
                     '5427', '5432', '5550', '5569', '5599', '5600', '5601', '5631', '5632', '5673', '5675', '5676',
                     '5678', '5679', '5720', '5729', '5730', '5731', '5732', '5742', '5745', '5746', '5755', '5757',
                     '5766', '5767', '5768', '5777', '5800', '5801', '5802', '5803', '5900', '5901', '5902', '5903',
                     '6000', '6001', '6002', '6003', '6004', '6005', '6006', '6007', '6008', '6009', '6456', '6471',
                     '6505', '6506', '6507', '6508', '6509', '6510', '6566', '6580', '6581', '6582', '6588', '6631',
                     '6667', '6668', '6670', '6671', '6699', '6701', '6788', '6789', '6841', '6842', '6883', '6939',
                     '6969', '6970', '7000', '7002', '7003', '7004', '7005', '7006', '7007', '7008', '7009', '7011',
                     '7012', '7013', '7014', '7015', '7020', '7021', '7100', '7121', '7300', '7301', '7306', '7307',
                     '7308', '7323', '7511', '7588', '7597', '7626', '7633', '7674', '7675', '7676', '7720', '7743',
                     '7789', '7797', '7798', '8000', '8001', '8007', '8008', '8009', '8010', '8011', '8022', '8080',
                     '8081', '8082', '8118', '8121', '8122', '8181', '8225', '8311', '8351', '8416', '8417', '8473',
                     '8668', '8786', '8787', '8954', '9000', '9001', '9002', '9021', '9022', '9023', '9024', '9025',
                     '9026', '9101', '9102', '9103', '9111', '9217', '9281', '9282', '9346', '9400', '9401', '9402',
                     '9594', '9595', '9800', '9801', '9802', '9872', '9873', '9874', '9875', '9899', '9909', '9911',
                     '9989', '9990', '9991', '10000', '10001', '10005', '10008', '10067', '10113', '10115', '10116',
                     '10167', '11000', '11113', '11233', '12076', '12223', '12345', '12346', '12361', '13223', '13224',
                     '16959', '16969', '17027', '19191', '20000', '20001', '20034', '21554', '22222', '23444', '23456',
                     '25793', '26262', '26263', '26274', '27374', '30100', '30129', '30303', '30999', '31337', '31338',
                     '31339', '31666', '31789', '32770', '33333', '33434', '34324', '36865', '38201', '39681', '40412',
                     '40421', '40422', '40423', '40426', '40843', '43210', '43190', '44321', '44322', '44334', '44442',
                     '44443', '44445', '45576', '47262', '47624', '47806', '48003', '50505', '50766', '53001', '54320',
                     '54321', '61466', '65000', '65301']
        schedule = len(args_port)
        port_default = "默认端口"
        for i in args_port:
            port.put(i)
    else:  # 过滤指定端口

        # 这个是指定多少到多端口1-65535
        if '-' in args_port:  # 查看参数里面是否有-
            port_default = "当前指定端口：" + str(args_port)
            port2 = args_port.split('-')  # 已-分割
            for i in range(int(port2[0]), int(port2[1])):
                port.put(str(i))
                schedule += 1
                #print(i)
                #port.put(i)
                #print(i)
                #print(args_port)

        # 这个是指定多个ip比如1,2,3,4

        elif ',' in args_port:  # 查看参数里面是否有,
            port_default = "当前指定端口：" + str(args_port)
            port2 = args_port.split(',')  # 已,分割
            for i in port2:
                print(i)
                schedule += 1
                port.put(i)

        # 这个就是单个
        else:
            schedule += 1
            port.put(args_port)

    global GUI_state  # 状态栏扫描进度


    if GUT_Sure == 1:
        print(int(schedule))
        GUI_state['maximum'] = int(schedule-1)  # 记录一共数量
        GUT_output.insert(ttk.END, f"目标是：{args_host}\n{thread_default}\n{port_default}\n")
    else:
        print(UseStyle(f"目标是：{args_host}\n{thread_default}\n{port_default}\n", fore='red'))

    Thread(args_host, port, int(args_thread))


def Interface(args):

    args_host=args.PS # IP
    args_port=args.PSp # 端口
    args_thread=args.PSt #线程

    splicing(args_host,args_port,args_thread)



def GUI(host,port,thread,result,progressbar):
    global GUT_output # 输出到GUI
    global GUI_state # 状态栏扫描进度
    global GUT_Sure # 判断是否用到GUI

    GUI_state=progressbar

    GUT_output=result # 输出到GUI
    GUT_Sure=1  # 判断是否用到GUI
    splicing(host, port, thread)

    # print(args.host,args.port,args.thread)
    #splicing(args)
# if __name__=='__main__':
#     parser = argparse.ArgumentParser(description="警告：请勿用于非法用途！否则自行承担一切后果",
#                                      usage='python3 Full_Scanner_back.py  [目标] [其他参数]')
#
#     Active_collect_message = parser.add_argument_group("参数",
#                                                        "下面是参数和参数的使用说明")
#
#     Active_collect_message.add_argument('-H', '--host',
#                                         dest='host',
#                                         type=str,
#                                         nargs='?',
#                                         help="指定扫描的目标，比如1.1.1.1")
#     Active_collect_message.add_argument('-p', '--port',
#                                         dest='port',
#                                         type=str,
#                                         nargs='?',
#                                         help="指定端口，不指定默认")
#
#     Active_collect_message.add_argument('-t', '-thread',
#                                         dest='thread',
#                                         type=int,
#                                         nargs='?',
#                                         help="指定线程、线程太多会出问题")
#
#
#     args=parser.parse_args()
#     Host = '192.168.0.113'  # 目标主机ip
#     args.host=Host
#      # socketk(Host, 3389)
#     if args.host != None:
#
#         # 默认线程
#         if args.thread == None:
#             args.thread = 1
#             print("默认线程 1")
#         splicing(args)
