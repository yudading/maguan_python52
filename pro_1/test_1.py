'''1 练习：如何模糊搜索文件

下载：https://video.mugglecode.com/files.zip
1 除了 git 类型之外的其它类型
2 名字中包含有关键词 "project30" 或者 "commercial"
'''

# coding:utf-8

import os

# 需要把路径替换成你的文件夹所在路径

path = "./files"

# 利用 os 模块中的 lisdir 函数和 for 语句，浏览所有文件

files = os.listdir(path)

for f in files:
    # 判断文件是否符合要求
    if (not f.endswith('.git')) and ('project30' in f or 'commercial' in f):
        # 如果符合要求，则输出文件名
        print(f)