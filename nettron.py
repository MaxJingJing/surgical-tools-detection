# import netron
# netron.start(R"runs/train/exp49/weights/best.onnx")



import os


def covertFukeSize(size):
    kb=1024
    mb=kb*1024
    gb=mb*1024
    tb=gb*1024

    if size>=tb:
        return "%.1f TB"% float(size / tb)
    if size>=gb:
        return "%.1f GB"% float(size / gb)
    if size>=mb:
        return "%.1f MB"% float(size / mb)
    if size>=kb:
        return "%.1f KB"% float(size / kb)
wav_path = 'yolov5n.pt'
fsize = os.path.getsize(wav_path)
a =covertFukeSize(fsize)

print(a)