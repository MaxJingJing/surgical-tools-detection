import shutil
import cv2
import time
import os


def videoDemo(image_path,cap_num):
    print('开始')
    start_time = time.time()
    cv2.namedWindow('camera')
    cap = cv2.VideoCapture(cap_num+cv2.CAP_DSHOW)
    # cap.set(3,1280)# 外部摄像头
    # cap.set(4,960)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1280)
    cap.set(cv2.CAP_PROP_BRIGHTNESS,-40)
    # cap = cv2.VideoCapture(0)  # 电脑自身摄像头

    print('weight:{}'.format(cap.get(cv2.CAP_PROP_BRIGHTNESS)))
    # print('height:{}'.format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    cap.set(cv2.CAP_PROP_FPS, 30)
    # print(cap.isOpened())

    i = 0#定时装置初始值
    photoname=1
    photonum=1
    while True:
        i = i + 1
        reg, frame = cap.read()
        frame = cv2.flip(frame, 1)  # 图片左右调换
        cv2.imshow('camera', frame)
        if i == 30:  # 定时装置，定时截屏，可以修改。
            name = str(photoname)
            filename = name + '.png'  # 图片命名：标签名_数字，将photoname作为编号命名保存的截图

            cv2.imwrite(image_path +"\\" + filename, frame)  # 截图
            # print('1')
            print(filename + '保存成功')  # 打印保存成功
            i = 0  # 清零

            photoname = photoname + 1
            photonum = photonum + 1

        if photonum >= 1000:  # 最多截图20张 然后退出（如果调用photoname = 1 不用break为不断覆盖图片）
            # photoname = 1
            print("打印完成")
            break
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    end_time = time.time()
    all_time = end_time-start_time
    print("采集{}张图片用时{}秒".format(photonum,all_time))
    # 释放资源
    cap.release()

def capturePicture(input_capture_video,cap_num):

    # label_file = os.listdir(local_path)
    # 图像保存文件夹
    if os.path.exists(input_capture_video):
        shutil.rmtree(input_capture_video)
        # print(os.listdir(input_capture_video))
        videoDemo(input_capture_video,cap_num)
        cv2.destroyAllWindows()
    else:
        os.mkdir(input_capture_video)
        videoDemo(input_capture_video,cap_num)
        cv2.destroyAllWindows()
if __name__ == '__main__':
    capture_video_1 = 'image/images-1'
    capture_video_2 = 'image/images-3'

    capturePicture(capture_video_2,2)
    # capturePicture(capture_video_2,1)