import os
import sys
import multiprocessing

#  命令行参数
srcDir = sys.argv[1]
dstDir = sys.argv[2]

#  src目录一定要存在，若不存在，结束
if not os.path.isdir(srcDir):  # 使用os.path.isdir()函数判断某一路径是否为目录
    print('源目录不存在')
    exit(1)

# 目标目录名对应的文件，一定要目录
if os.path.exists(dstDir) and not os.path.isdir(dstDir):
    print('目标目录不存在')
    exit(1)

#  若目标无任何东西，创建一个目录
if not os.path.exists(dstDir):  # 判断路径是否存在
    os.mkdir(dstDir)


#  拷贝文件
def copy_file(srcfile, dstfile):
    old_file = open(srcfile, 'rb')
    new_file = open(dstfile, 'wb')

    while True:
        data = old_file.read(1006)
        if not data:
            break
        new_file.write(data)

    old_file.close()
    new_file.close()

processes = []


#  拷贝目录
def copy_dir(srcDir, dstDir):
    # 遍历源目标，listdir只是列出当前目录下的第一层的所有文件名
    for file in os.listdir(srcDir):
        srcfile = srcDir + '/' + file
        dstfile = dstDir + '/' + file

        #  若是文件，直接调用copy_file
        if os.path.isfile(srcfile):
            process = multiprocessing.Process(target=copy_file, args=(srcfile, dstfile))
            process.start()
            processes.append(process)

        #  若对应的是目录
        elif os.path.isdir(srcfile):
            #  创建目录
            os.mkdir(dstfile)
            #  递归调用拷贝目录
            copy_dir(srcfile, dstfile)

#  调用拷贝目录
copy_dir(srcDir, dstDir)

#  等待所有进程结束
for process in processes:
    process.join()

print('copy end')
