


import csv

from wxpy import *

imort time

def read_info():
    f = open('./sample.csv','r')
    reader = csv.DictReader(f)
    return [info for info in reader]


def make_msg(raw_info):
    t = '{n}-同学请于{t}时间参加{s}程，课程地址是{s}。收到请回复，谢谢！'
    return [t.format(n=info['姓名']
                     t=info['上课时间']
                     s=info['课程']
                     a=info['上课地址']
                    ) for info in raw_info]



def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        fren_name = msg.split('_')[0]

        f = bot.friends().search(fren_name)[0]
        if len(f) == 1:
            f[0].send()
        else:
            print(fren_name)
            print('Please check this name')
        time.sleep(3)


raw_info = read_info()
msg = make_msg(raw_info)
send(msg)
