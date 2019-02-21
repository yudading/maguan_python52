'''项目 2 练习 ： 如何实现文件自动归类

需求如下：

1 把 jpg png gif 文件夹中的所有文件移动到 image 文件中，然后删除 pg png gif ；

2 把 doc docx md ppd 文件夹中的所有文件移动到 document 文件夹中，然后删除 doc docx md ppd 文件夹。

问题拆解提示：

1 如何创建目标文件夹？
2 如何浏览各个文件夹？
3 如何移动文件夹中的文件？
4 如何删除文件夹？

问题解决提示：

1 利用 os 模块中的 makedirs 函数，可以在指定路径创建文件夹。在本题中，可以先创建好
image 和 document 文件夹，在进行后续的处理。

2 os 模块中的 listdir 函数和 for 语句配合，可以完成浏览文件夹中所有文件的功能。在
本题中需要注意的是，要浏览的文件夹有 7 个，所以先将 7 个文件夹的名称存到了 list 变量中，
便于使用。

3 shutil 模块中的 move 函数提供了移动文件的功能。需要指定文件所在路径和目标路径。

4 os 模块中的 removedir 函数提供了删除文件夹的功能。
'''

# coding:utf-8
import os

import shutil

# 需要把路径替换成你的文件夹所在路径，当把这个代码文件放在要处理的文件夹外一层时，可以使用下面的相对路径写法
path = './problem2_files'
# 创建目标文件夹
os.makedirs(path + '/image')
os.makedirs(path + '/document')
# 将需要处理的后缀名存储到 list 中
image_suffix = ['jpg','png','gif']
doc_suffix = ['doc','docx','ppt','md']

# 移动 jpg png gif 文件中的文件
for i in image_suffix:
    cur_path = path + '/' + i
    files = os.listdir(cur_path)
    for f in files:
        # 移动文件夹中的文件
        shutil.move(cur_path + '/' + f, path + '/image')
    # 删除文件夹
    os.removedirs(cur_path)

# 移动 doc docx md ppt 文件夹中的文件，步骤与前面类似
for d in doc_suffix:
    cur_path = path + '/' + d
    files = os.listdir(cur_path)
    for f in files:
        shutil.move3(cur_path + '/' +f, path + '/document')
    os.removedirs(cur_path)



