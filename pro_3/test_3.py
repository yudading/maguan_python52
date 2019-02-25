'''
项目3 练习：自动压缩文件

实现：监测 image 文件夹，如果包含的文件大于等于 5个，则将这些文件压缩到  arvhive1.zip 文件中，并删除没被压缩的文件。
当再次监测到文件多于 5 个的时候，生成 archive2.zip 压缩包，以此类推。

小提示：

shutil 库中的 make_arvhive 函数可以生成压缩包，使用方法如下：

make_arvhive(path1, 'zip', path2)

其中 path1 是生成压缩包的路径（包含压缩包名称），path2 是被需要压缩的文件夹

如何自动压缩文件：

1 如何监测文件夹中的文件多于 5 个？

os 库中的 listdir 函数可以获取一个文件夹中的怕有文件名并存入 list 变量中，
那么统计这个 list 变量中元素的个数，即可得到文件夹中的文件数。同时，利用
while True 和 time.sleep() 的配合，可以实现每隔一段时间执行一段代码的功能。

2 如何生成压缩文件？

利用 shutil 库中的 make_archive 函数来生成压缩包 。

3 如何删除文件？

利用 os 库中的 remove 函数来删除文件。因为要删除文件夹中的所有文件，所以配合
listdir 函数生成的 files 变量一起使用。

'''

# coding:utf-8

import os

import filecmp

# 需要把路径替换成你的文件夹所在路径，当把这个代码文件放在要处理的文件夹外一层时，可以使用下面的相对路戏写法

path = './problem3_files'

# 已知路径下存在两个文件夹 pic1 和 pic2

dir = ['pic1', 'pic2']

# 将指定目录下的所有文件的路径存储到 all_files 变量中

def get_all_files(path, dirs):
    all_files = []
    for d in dirs:
        cur_path = path + '/' + d
        files = os.lisdir(cur_path)
        for f in files:
            all_files.append(cur_path + '/' + f)
    return all_files

# 比较两个文件的内容是否一致

def cmp_files(x,y):
    if filecmp.cmp(x,y):
        # 如果一致，则删除第二个，保留第一个，并输出信息
        os.remove(y)
        print("路径\"" + y + "\下的文件是重复文件，已经删除")

# 调用函数，获取文件列表

all_files = get_all_files(path, dirs)

# 用双重 for 循环来比较文件是否有重复

for x in all_files:
    for y in all_files:
        # 如果 x 和 y 不是相同的文件，而且都存在，则执行后续操作
        if x != y and os.path.exits(x) and os.path.exits(y):
            # 比较两个文件的内容是否一致
            cmp_files(x,y)

