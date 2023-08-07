
import os
import datetime

def rename_file(file_path,file_name):
    time = datetime.datetime.today().strftime('%H{h}%M{f}%S{s}'). \
        format(h='时', f='分',s='秒')
    try:
        file_list = os.listdir(file_path)
        print(file_list)
        if file_name in file_list:
            print("文件存在")
            old = file_path+file_name
            new = file_path+'{}'.format(time)+file_name
            os.rename(old,new)
            print("更换文件名为{}".format(new))

    except:
        return 'error'