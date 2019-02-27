'''
test_4: 如何群发图片

使用 wxpy 库给 3 个人群发同一张图片

如何群发图片：

1 如何通过 wxpy 库找到好友？

参考课程中的内容，利用 bot.friends(),search("name") 实现按名字搜索好友。

2 如何给好友发送图片？

课程中我们利用 send() 函数发送信息，阅读文档发现，send_image() 函数可以发送图片。

test_4: 群发定制信息

如何定制群发信息：

1 如何读取 csv 文件？

利用 python 内置的 csv 库，通过调用 csv.DictReader() 函数，读取并解析 csv 文件

小技巧：利用列表解析式生成  list , list 中的每一个元素代表了 csv 文件中的一行

2 如何根据 csv 内容生成对应的文字信息？

利用内置的 format() 函数，根据文字模板和指定内容，生成对应的信息。

3 如何发送信息？

利用 wxpy 库，查找好友并发送信息。


'''
# coding:utf-8

from wxpy import *

# 指定图片文件的路径
image_path = "./image/owl.jpg" # 这里替换成你的路径

# 初始化微信机器人
bot = Bot()

# 将要发送的好友的名字存到 list 中

friends = ['王总'，'麻瓜编程君'，'沫沫']

# 定义用于群发操作的函数

def send_to_friend(friends):
    for friend in friends:
        # 搜索好友
        friends_search = bot.friends().search(friend)
        # 如果搜索结果仅有一个，则发送图片，否则返回错误信息
        if (len(friend_search) == 1):
            friends_search[0].send_image(image_path)
        else:
            print("发送失败！请检查用户名:" + friend)

# 调用函数

send_to_friend(friends)


'''群发定制信息'''

import csv

import time

from wxpy import *

FREINDS = ['李总'，'麻瓜编程君'，'沫沫']
CSV_PATH = './meeting_msg_csv'

# 定义函数获取 csv 中的内容

def read_csv(path):
    f = open(path, 'r', encoding='utf-8')
    reader = csv.DictReader(f)
    #print([info for info in reader])
    return [info for info in reader]


# 定义获取发送内容的函数

def get_msg(infos, name):
    template = "{name},提醒下，{time}记得来参加{event}，地点在{location}， {note}"

    for info in infos:
        if info[''] == name:
            msg = template.format(
                name = info['微信昵称']
                time = info['时间']
                event = info['事件']
                location = info['地址']
                note = info['备注']
            )
            return msg
    # 如果在 infos 列表中没有找到对应的微信昵称，则输出 None
    return None

# 定义用于群发操作的函数

def send_to_friends(infos, friends):
    # 初始化微信机器人
    bot = Bot()

    for friend in friends:
        # 搜索好友
        friend_search = bot.friends().search(friend)
        # 如果搜索结果仅有一个，则发送图片，否则返回错误信息
        if (len(friend_search) == 1):
            msg = get_msg(infos, friend)
            if msg:
                friend_search[0].send(msg)
            else:
                print("发送失败！用户名不在 csv 中：" + friend)
        else:
            print("发送失败！请检查用户名：" + friend)
        time.sleep(3)

# 调用群发函数
send_to_friend(read_csv(CSV_PATH), FREINDS)
