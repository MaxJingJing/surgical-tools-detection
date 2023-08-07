import os
import tarfile

def get_tar(tar_path,tar_name):
    # 创建压缩包名，获取压缩tar对象
    tar = tarfile.open(tar_name,"w:gz")
    # 创建压缩包
    for root, dir, files in os.walk(tar_path):  # os.walk() 方法可以创建一个生成器，用以生成所要查找的目录及其子目录下的所有文件。
        for file in files:
            fullpath = os.path.join(root, file)  # 拼接路径
            tar.add(fullpath)  # 添加压缩文件
    tar.close()  # 关闭压缩文件流
