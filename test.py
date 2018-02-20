import os
os.path.realpath(_file_)——返回真实路径

os.path.split()——返回路径的目录和文件名

os.getcwd()——得到当前工作的目录

__file__ 是用来获得模块所在的路径的 

print(os.path.realpath(__file__))
print(os.path.split(os.path.realpath(__file__)))
print(os.getcwd())
