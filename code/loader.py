import msvcrt

import numpy as np
import cv2
import os
import time
import keyboard
import pyautogui

'''
这是第二个文件，加载数据；
实现在线相机标定；
在线开启摄像头；
'''
#加载数据
with np.load('data.npz') as X:
    #加载上一部生成的参数
    mtx, dist, rvecs, tvecs,newcameramtx,roi= [X[i] for i in ('mtx','dist','rvecs','tvecs','newcameramtx','roi')]
    # print(mtx,'------',dist)

#打开摄像机

def travelFilelist(path):
    filelist = os.listdir(path)#遍历文件夹
    numlist = []#创建空列表
    if len(filelist) !=0:

        # for i in range(len(filelist)):
        #     CurrentFileName = filelist[i]
        #     labelname,line= CurrentFileName.split("-")#以"_"分割
        #     num,png= line.split(".")#以"."分割
        #     numlist.append(int(num))#转换int整型
        #
        # numlist.sort()#排序

        CurrentFileName = filelist[-1]
        labelname,line= CurrentFileName.split("-")#以"_"分割
        num,png= line.split(".")#以"."分割
        numlist.append(int(num))#转换int整型

        numlist.sort()#排序
        return numlist[-1]+1#返回最大值
    else:
        return 1
    # print(numlist[-1])

def videoDemo(label_name,local_path):
    print('开始')
    start_time = time.time()


    label_filename = os.path.join(local_path,label_name) # 拼接路径：文件路径+标签名字组成新路径

    if os.path.exists(label_filename):
        photoname = travelFilelist(label_filename)
    else:
        os.mkdir(label_filename)# 不存在就创建
        photoname = 1#文件名序号初始值

    i = 0#定时装置初始值
    photonum=1
    cap = cv2.VideoCapture(0)  # 电脑自身摄像头
# cv2.resizeWindow("capture", cv2.WINDOW)
    while True:
        i = i + 1
        # if keyboard.is_pressed('esc'):
        #     break  # 退出循环
        reg, frame = cap.read()
        frame = cv2.flip(frame, -1)  # 图片左右调换
        # --------------------------------
        #
        frame = cv2.undistort(frame, mtx, dist, None, newcameramtx)
        # x, y, w, h = roi   # 裁剪图像，输出纠正畸变以后的图片
        # frame = frame[y:y + h, x:x + w]

        # --------------------------------
        cv2.imshow('capture', frame)
        if i == 30:  # 定时装置，定时截屏，可以修改。
            name = label_name +"-"+ str(photoname)
            filename = name + '.jpg'  # 图片命名：标签名_数字，将photoname作为编号命名保存的截图

            cv2.imwrite(label_filename +"\\" + filename, frame)  # 截图
            print(filename + '保存成功')  # 打印保存成功
            i = 0  # 清零

            photoname = photoname + 1
            photonum = photonum + 1

        if photonum >= 30:  # 最多截图20张 然后退出（如果调用photoname = 1 不用break为不断覆盖图片）
            # photoname = 10
            print("打印完成")
            break
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    end_time = time.time()
    all_time = end_time-start_time
    print("采集{}张图片用时{}秒".format(photonum,all_time))
    # 释放资源
    cap.release()
# def return_num():
#     return 0
def capturePicture(local_path):
    while True:

        start = time.time()
        label_file = os.listdir(local_path)
        # if len(label_file) !=0:
        #     # print("请输入英文标签！")
        #     print("已存在的标签类别为：{}".format(label_file))
        #     for i,name in enumerate(label_file):
        #         print("对应码：{}，文件夹：{}".format(i,name))
        #
        #     str ="如果已存在标签文件名请输入1\n如果退出拍摄任务请输入2\n"
        #     print(str)
        #
        #     key = int(input("请输入key值："))
        #
        #     if key==1 :
        #         filelist_num = int(input("请输入已存在文件夹的对应码："))
        #         if filelist_num not in range(len(label_file)):
        #             print("***您输错了，请重新输入！***")
        #             filelist_num = int(input("请输入已存在文件夹的对应码："))
        #             input_file_name = label_file[filelist_num]
        #             videoDemo(input_file_name,local_path)
        #
        #         input_file_name = label_file[filelist_num]
        #         videoDemo(input_file_name,local_path)
        #
        #     elif key==2:
        #         # break
        #         input_file_name =input("请输入标签：")
        #         videoDemo(input_file_name,local_path)
        #
        #     else:
        #         # input_file_name =input("请输入标签：")
        #         # videoDemo(input_file_name,local_path)
        #         break
        #
        # else:
        #
        #     input_file_name =input("请输入标签：")
        #     videoDemo(input_file_name,local_path)


        # --------------------------------------

        # print("请输入英文标签！")
        print("已存在的标签类别为：{}".format(label_file))
        for i,name in enumerate(label_file):
            print("对应码：{}，文件夹：{}".format(i,name))
        print("*"*20)
        str ="如果已存在标签文件名请输入1\n如果输入标签文件名请输入2\n如果退出拍摄任务请输入任意键"
        print(str)
        print("*"*20)

        key = int(input("请输入key值："))

        if key==1 :
            filelist_num = int(input("请输入已存在文件夹的对应码："))
            if filelist_num not in range(len(label_file)):
                print("***您输错了，请重新输入！***")
                filelist_num = int(input("请输入已存在文件夹的对应码："))
                input_file_name = label_file[filelist_num]
                videoDemo(input_file_name,local_path)

            input_file_name = label_file[filelist_num]
            videoDemo(input_file_name,local_path)

        elif key==2:
            # break
            input_file_name =input("请输入标签：")
            videoDemo(input_file_name,local_path)

        else:
            # input_file_name =input("请输入标签：")
            # videoDemo(input_file_name,local_path)
            b = pyautogui.confirm('是否停止拍摄', buttons=['enter', 'cancel'])
            # print(b)
            if b =="enter":
                break
            else:
                continue

        # -------------------------------------------


        cv2.destroyAllWindows()
        end = time.time()
        times = start-end
        print("一次拍摄需要{}秒".format(times))
        # print("结束拍摄")

if "__name__=__main__":
    local_path = "D:\Graduation_Project_Coding\pythonProject\Raspberry\image_dataset"
    capturePicture(local_path)



