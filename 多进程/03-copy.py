import sys
import os
import multiprocessing

srcDir = sys.argv[1]
dstDir = sys.argv[2]

if not os.path.isdir(srcDir):
    print('不存在源目录')
    exit(1)

if os.path.exists(dstDir) and not os.path.isdir(dstDir):
    print('目标目录不存在')

if os.path.exists(dstDir):
    os.mkdir(dstDir)


def copy_file(srcfile, dstfile):
    old_file = open(srcfile, 'rb')
    new_file = open(dstfile, 'wb')

    while True:
        data = old_file.read(1000)
        if not data:
            break
        new_file.write(data)

    old_file.close()
    new_file.close()

processes = []


def copy_dir(srcDir, dstDir):
    for file in os.listdir(srcDir):
        srcfile = srcDir + '/' + file
        dstfile = dstDir + '/' + file

        #  若是文件，直接调用copy_file
        if os.path.isfile(srcfile):
            process = multiprocessing.Process(target=copy_file, args=(srcfile, dstfile))
            process.start()
            processes.append(process)

        # 若对应的是目录
        elif os.path.isdir(srcfile):
            #  创建目录
            os.mkdir(dstfile)
            #  递归调用拷贝目录
            copy_dir(srcfile, dstfile)


# 调用拷贝目录
copy_dir(srcDir, dstDir)

#  等待所有进程结束
for process in processes:
    process.join()

print('copy end')
