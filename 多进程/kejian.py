

# python3 T10DirCopy.py srcDir dstDir

import os
import sys
import multiprocessing

# 命令行参数
srcDir = sys.argv[1]
dstDir = sys.argv[2]

# src目录一定要存在，如果不存在，结束了
if not os.path.isdir(srcDir):
    print('src not dir')
    exit()

# 目标目录名对应的文件，一定要是个目录
# /a --- b
# /c --- d
# /a -- b + d
if os.path.exists(dstDir) and not os.path.isdir(dstDir):
    print('dst not dir')
    exit(1)

# 如果目标没有任何东西，创建一个目录
if not os.path.exists(dstDir):
    os.mkdir(dstDir)

# 拷贝文件
def copyFile(srcfile, dstfile):
    iFile = open(srcfile, 'rb')
    oFile = open(dstfile, 'wb')

    while True:
        data = iFile.read(1024)
        if not data:
            break
        oFile.write(data)

    iFile.close()
    oFile.close()

processes = []

# 拷贝目录
def copyDir(srcDir, dstDir):
    # 遍历srdDir
    # listdir只是列出当前目录下的第一层的所有的文件名
    for file in os.listdir(srcDir):
        srcfile = srcDir + '/' + file
        dstfile = dstDir + '/' + file

        # 如果完整的文件名，对应的是文件，直接调用copyFile
        if os.path.isfile(srcfile):
            # copyFile(srcfile, dstfile)
            process = multiprocessing.Process(target=copyFile, args=(srcfile, dstfile))
            process.start()
            processes.append(process)

        # 如果对应的是目录
        elif os.path.isdir(srcfile):
            # 目标创建目录
            os.mkdir(dstfile)
            # 递归调用拷贝目录
            copyDir(srcfile, dstfile)

# 调用拷贝目录
copyDir(srcDir, dstDir)

# 等待所有进程结束
for process in processes:
    process.join()

print('copy end2')


