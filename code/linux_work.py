
import argparse
import Capture_video
import Zip_file
# import Control_GPIO
import Send_file
# import Rename_file
import tar_File
import os
import loader

def parameters():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # GPIO参数
    parser.add_argument("--localPath",default ="/home/tzx/GPIO/Raspberry/image_dataset")
    parser.add_argument("--top_lamp",default=17)
    parser.add_argument("--swith_light",default=27)
    parser.add_argument("--rotary_swith",default=18)
    parser.add_argument("--camera_swith",default=23)
    parser.add_argument("--swith",default=22)
    # 图像拍摄
    parser.add_argument("--input_capture_video",default="/home/tzx/GPIO/Raspberry/image_dataset")# Capture_video参数
    # 压缩文件
    parser.add_argument("--dirpath",default="/home/tzx/GPIO/Raspberry/image_dataset")
    parser.add_argument("--outFullName",default="/home/tzx/GPIO/Raspberry/image_dataset.zip ")
    #发送文件
    parser.add_argument("--fromaddr",default="2801221277@qq.com")#发送用户
    parser.add_argument("--password",default="kbvhultuggyidfdc")#授权码
    parser.add_argument("--toaddrs",default="1430548476@qq.com")#接收用户
    parser.add_argument("--zipFile",default="//home/tzx/GPIO/Raspberry/image_dataset.zip")#附件
    parser.add_argument("--qq_server",default="smtp.qq.com")
    # 更换名称
    # parser.add_argument("--file_path",default="/home/tzx/GPIO/Raspberry/run/")
    # parser.add_argument("--file_name",default="Capture.zip")
    # parser.add_argument("--tar_name",default ="/home/tzx/GPIO\Raspberry/run/capture.tar.gz")
    # parser.add_argument("--tar_path",default ="/home/tzx/GPIO\Raspberry/run/input_capture_video")

    return  parser.parse_args()
def main():
    '''
    采集箱工作步骤：
    第一 开启gpio引脚
    第二 开始拍摄
    第三 开始压缩
    第四 开始发送
    第五 循环步骤
    :return:
    '''
    args=parameters()
    # Control_GPIO.ControlGPIO_Start(args.top_lamp,
    #                                         args.with_light,
    #                                         args.rotary_swith,
    #                                         args.camera_swith,
    #                                         args.swith)#GPIO开启设置

    # Capture_video.capturePicture(args.localPath)# 拍摄图像
    loader.capturePicture(args.localPath)

    # Control_GPIO.ControlGPIO_ending(args.rotary_swith,
    #                                        args.camera_swith)#关闭GPIO引脚

    # Zip_file.getZipDir(args.dirpath,
    #                    args.outFullName)#压缩文件夹
    #tar_File.get_tar(args.tar_path,args.tar_name)
    #print(os.system("ls"))
    #zip_file
    os.system("sudo zip -r /home/tzx/GPIO/Raspberry/image_dataset.zip /home/tzx/GPIO/Raspberry/image_dataset")
   

    Send_file.sendFile(args.fromaddr,
                       args.password,
                       args.toaddrs,
                       "/home/tzx/GPIO/Raspberry/image_dataset.zip",
                       args.qq_server)#发送文件
'''
    # Rename_file.rename_file(args.file_path,args.file_name)
    
'''

if '__main__':
    main()

    	    











