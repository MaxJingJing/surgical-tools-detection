# from xml.dom.minidom import Document
# import os
# import cv2
#
#
# # def makexml(txtPath, xmlPath, picPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
# def makexml(picPath, txtPath, xmlPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
#     """此函数用于将yolo格式txt标注文件转换为voc格式xml标注文件
#     """
#     # dic = {'0': "TissueForceps_14",  # 创建字典用来对类型进行转换
#     #        '1': "AppendixIntestinalClamp_16",
#     #        '2':'SPestractor_25',    # 此处的字典要与自己的classes.txt文件中的类对应，且顺序要一致
#     #        '3' :'MedicalTray_18.5',
#     #        '4' :'TowelForceps_11',
#     #        '5' :'StraightLigatureScissors_10',
#     #        '6' :'ElbowLigatureScissors_10',
#     #        '7' :'StraightLigatureScissors_18',
#     #        '8' :'ElbowLigatureScissors_16',
#     #        '9' :'Tweezrs_11',
#     #        '10' :'Tweezrs_14',
#     #        '11' :'Tweezrs_15',
#     #        '12' :'ThickScalpel_3',
#     #        '13' :'ThinScalpel_3',
#     #        '14' :'ThickScalpel_4',
#     #        '15' :'ThinScalpel_4',
#     #        '16' :'ElbowHemostasticForceps_12.5',
#     #        '17' :'StraightHemostasticForceps_14'
#     #        }
#     dic={'0':'Thyroid pull hook',
#           '1':'Tissue Forceps',
#           '2':'Appendix Forceps',
#           '3':'S deep pull hook',
#           '4':'Straight Oval Forceps',
#           '5':'Elbow Oval Forceps',
#           '6':'Bending Plate',
#           '7':'Towel Forceps',
#           '8':'Straight Ligature Scissors18',
#           '9':'Elbow Ligature Scissors16',
#           '10':'Medical Tweezers13',
#           '11':'Medical Tweezers14',
#           '12':'Medical Tweezers15',
#           '13':'Thick Scalpel3',
#           '14':'Thin Scalpel3',
#           '15':'Thick Scalpel4',
#           '16':'Thin Scalpel4',
#           '17':'Elbow Hemostatic Forceps12.5',
#           '18':'Straight Hemostatic Forceps14'
#     }
#     files = os.listdir(txtPath)
#     for i, name in enumerate(files):
#         xmlBuilder = Document()
#         annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
#         xmlBuilder.appendChild(annotation)
#         txtFile = open(txtPath + name)
#         txtList = txtFile.readlines()
#         img = cv2.imread(picPath + name[0:-4] + ".jpg")
#         Pheight, Pwidth, Pdepth = img.shape
#
#         folder = xmlBuilder.createElement("folder")  # folder标签
#         foldercontent = xmlBuilder.createTextNode("driving_annotation_dataset")
#         folder.appendChild(foldercontent)
#         annotation.appendChild(folder)  # folder标签结束
#
#         filename = xmlBuilder.createElement("filename")  # filename标签
#         filenamecontent = xmlBuilder.createTextNode(name[0:-4] + ".jpg")
#         filename.appendChild(filenamecontent)
#         annotation.appendChild(filename)  # filename标签结束
#
#         size = xmlBuilder.createElement("size")  # size标签
#         width = xmlBuilder.createElement("width")  # size子标签width
#         widthcontent = xmlBuilder.createTextNode(str(Pwidth))
#         width.appendChild(widthcontent)
#         size.appendChild(width)  # size子标签width结束
#
#         height = xmlBuilder.createElement("height")  # size子标签height
#         heightcontent = xmlBuilder.createTextNode(str(Pheight))
#         height.appendChild(heightcontent)
#         size.appendChild(height)  # size子标签height结束
#
#         depth = xmlBuilder.createElement("depth")  # size子标签depth
#         depthcontent = xmlBuilder.createTextNode(str(Pdepth))
#         depth.appendChild(depthcontent)
#         size.appendChild(depth)  # size子标签depth结束
#
#         annotation.appendChild(size)  # size标签结束
#
#         for j in txtList:
#             oneline = j.strip().split(" ")
#             object = xmlBuilder.createElement("object")  # object 标签
#             picname = xmlBuilder.createElement("name")  # name标签
#             namecontent = xmlBuilder.createTextNode(dic[oneline[0]])
#             picname.appendChild(namecontent)
#             object.appendChild(picname)  # name标签结束
#
#             pose = xmlBuilder.createElement("pose")  # pose标签
#             posecontent = xmlBuilder.createTextNode("Unspecified")
#             pose.appendChild(posecontent)
#             object.appendChild(pose)  # pose标签结束
#
#             truncated = xmlBuilder.createElement("truncated")  # truncated标签
#             truncatedContent = xmlBuilder.createTextNode("0")
#             truncated.appendChild(truncatedContent)
#             object.appendChild(truncated)  # truncated标签结束
#
#             difficult = xmlBuilder.createElement("difficult")  # difficult标签
#             difficultcontent = xmlBuilder.createTextNode("0")
#             difficult.appendChild(difficultcontent)
#             object.appendChild(difficult)  # difficult标签结束
#
#             bndbox = xmlBuilder.createElement("bndbox")  # bndbox标签
#             xmin = xmlBuilder.createElement("xmin")  # xmin标签
#             mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
#             xminContent = xmlBuilder.createTextNode(str(mathData))
#             xmin.appendChild(xminContent)
#             bndbox.appendChild(xmin)  # xmin标签结束
#
#             ymin = xmlBuilder.createElement("ymin")  # ymin标签
#             mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
#             yminContent = xmlBuilder.createTextNode(str(mathData))
#             ymin.appendChild(yminContent)
#             bndbox.appendChild(ymin)  # ymin标签结束
#
#             xmax = xmlBuilder.createElement("xmax")  # xmax标签
#             mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
#             xmaxContent = xmlBuilder.createTextNode(str(mathData))
#             xmax.appendChild(xmaxContent)
#             bndbox.appendChild(xmax)  # xmax标签结束
#
#             ymax = xmlBuilder.createElement("ymax")  # ymax标签
#             mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
#             ymaxContent = xmlBuilder.createTextNode(str(mathData))
#             ymax.appendChild(ymaxContent)
#             bndbox.appendChild(ymax)  # ymax标签结束
#
#             object.appendChild(bndbox)  # bndbox标签结束
#
#             annotation.appendChild(object)  # object标签结束
#
#         f = open(xmlPath + name[0:-4] + ".xml", 'w')
#         xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
#         f.close()
#
#
# if __name__ == "__main__":
#     picPath = "D:/Graduation_Project_Coding/dataset/JPEGImages/"  # 图片所在文件夹路径，后面的/一定要带上
#     txtPath = "D:/Graduation_Project_Coding/dataset/txtFile/"  # txt所在文件夹路径，后面的/一定要带上
#     xmlPath = "D:/Graduation_Project_Coding/dataset/Annotations/"  # xml文件保存路径，后面的/一定要带上
#     makexml(picPath, txtPath, xmlPath)
#




import os
import glob
from PIL import Image

voc_annotations = 'D:/Graduation_Project_Coding/dataset/Annotations/'
yolo_txt = 'D:/Graduation_Project_Coding/dataset/txtFile/'
img_path = 'D:/Graduation_Project_Coding/dataset/JPEGImages/'
# labels = ['A', 'B', 'C']  # label for datasets
labels = ['Thyroid pull hook',
'Tissue Forceps',
'Appendix Forceps',
'S deep pull hook',
'Straight Oval Forceps',
'Elbow Oval Forceps',
'Bending Plate',
'Towel Forceps',
'Straight Ligature Scissors18',
'Elbow Ligature Scissors16',
'Medical Tweezers13',
'Medical Tweezers14',
'Medical Tweezers15',
'Thick Scalpel3',
'Thin Scalpel3',
'Thick Scalpel4',
'Thin Scalpel4',
'Elbow Hemostatic Forceps12.5',
'Straight Hemostatic Forceps14']
# # 图像存储位置
# src_img_dir = img_path  # 添加你的路径
# # 图像的txt文件存放位置
#
#
# src_txt_dir = yolo_txt
# src_xml_dir = voc_annotations
#
# img_Lists = glob.glob(src_img_dir + '/*.jpg')
#
# img_basenames = []
# for item in img_Lists:
#     img_basenames.append(os.path.basename(item))
#
# img_names = []
# for item in img_basenames:
#     temp1, temp2 = os.path.splitext(item)
#     img_names.append(temp1)
#
# for img in img_names:
#     im = Image.open((src_img_dir + '/' + img + '.jpg'))
#     width, height = im.size
#
#     # 打开txt文件
#     gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()
#     print(gt)
#     if gt:
#         # 将主干部分写入xml文件中
#         xml_file = open((src_xml_dir + '/' + img + '.xml'), 'w')
#         xml_file.write('<annotation>\n')
#         xml_file.write('    <folder>VOC2007</folder>\n')
#         xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
#         xml_file.write('    <size>\n')
#         xml_file.write('        <width>' + str(width) + '</width>\n')
#         xml_file.write('        <height>' + str(height) + '</height>\n')
#         xml_file.write('        <depth>3</depth>\n')
#         xml_file.write('    </size>\n')
#
#         # write the region of image on xml file
#         for img_each_label in gt:
#             spt = img_each_label.split(' ')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
#             print(f'spt:{spt}')
#             xml_file.write('    <object>\n')
#             print(str(labels[int(spt[0])]))
#             xml_file.write('        <name>' + str(labels[int(spt[0])]) + '</name>\n')
#             xml_file.write('        <pose>Unspecified</pose>\n')
#             xml_file.write('        <truncated>0</truncated>\n')
#             xml_file.write('        <difficult>0</difficult>\n')
#             xml_file.write('        <bndbox>\n')
#
#             center_x = round(float(spt[1].strip()) * width)
#             center_y = round(float(spt[2].strip()) * height)
#             bbox_width = round(float(spt[3].strip()) * width)
#             bbox_height = round(float(spt[4].strip()) * height)
#             xmin = str(int(center_x - bbox_width / 2))
#             ymin = str(int(center_y - bbox_height / 2))
#             xmax = str(int(center_x + bbox_width / 2))
#             ymax = str(int(center_y + bbox_height / 2))
#
#             xml_file.write('            <xmin>' + xmin + '</xmin>\n')
#             xml_file.write('            <ymin>' + ymin + '</ymin>\n')
#             xml_file.write('            <xmax>' + xmax + '</xmax>\n')
#             xml_file.write('            <ymax>' + ymax + '</ymax>\n')
#             xml_file.write('        </bndbox>\n')
#             xml_file.write('    </object>\n')
#
#         xml_file.write('</annotation>')

import os
from PIL import Image
import glob

yolo_img = 'D:/Graduation_Project_Coding/dataset/JPEGImages/'
# yolo_txt = 'D:/shuichi_test/yolo/txt/'
voc_xml = 'D:/Graduation_Project_Coding/dataset/Annotations/'
#
# # 目标类别
# labels = ['HLB', 'health', 'ill']
# 匹配文件路径下的所有jpg文件，并返回列表
img_glob = glob.glob(yolo_img + '*.jpg')

img_base_names = []

for img in img_glob:
    # os.path.basename:取文件的后缀名
    img_base_names.append(os.path.basename(img))

img_pre_name = []

for img in img_base_names:
    # os.path.splitext:将文件按照后缀切分为两块
    temp1, temp2 = os.path.splitext(img)
    img_pre_name.append(temp1)
    print(f'imgpre:{img_pre_name}')
for img in img_pre_name:
    with open(voc_xml + img + '.xml', 'w') as xml_files:
        image = Image.open(yolo_img + img + '.jpg')
        img_w, img_h = image.size
        xml_files.write('<annotation>\n')
        xml_files.write('   <folder>folder</folder>\n')
        xml_files.write(f'   <filename>{img}.jpg</filename>\n')
        xml_files.write('   <source>\n')
        xml_files.write('   <database>Unknown</database>\n')
        xml_files.write('   </source>\n')
        xml_files.write('   <size>\n')
        xml_files.write(f'     <width>{img_w}</width>\n')
        xml_files.write(f'     <height>{img_h}</height>\n')
        xml_files.write(f'     <depth>3</depth>\n')
        xml_files.write('   </size>\n')
        xml_files.write('   <segmented>0</segmented>\n')
        with open(yolo_txt + img + '.txt', 'r') as f:
            # 以列表形式返回每一行
            lines = f.read().splitlines()
            for each_line in lines:
                line = each_line.split(' ')
                xml_files.write('   <object>\n')
                xml_files.write(f'      <name>{labels[int(line[0])]}</name>\n')
                xml_files.write('      <pose>Unspecified</pose>\n')
                xml_files.write('      <truncated>0</truncated>\n')
                xml_files.write('      <difficult>0</difficult>\n')
                xml_files.write('      <bndbox>\n')
                center_x = round(float(line[1]) * img_w)
                center_y = round(float(line[2]) * img_h)
                bbox_w = round(float(line[3]) * img_w)
                bbox_h = round(float(line[4]) * img_h)
                xmin = str(int(center_x - bbox_w / 2))
                ymin = str(int(center_y - bbox_h / 2))
                xmax = str(int(center_x + bbox_w / 2))
                ymax = str(int(center_y + bbox_h / 2))
                xml_files.write(f'         <xmin>{xmin}</xmin>\n')
                xml_files.write(f'         <ymin>{ymin}</ymin>\n')
                xml_files.write(f'         <xmax>{xmax}</xmax>\n')
                xml_files.write(f'         <ymax>{ymax}</ymax>\n')
                xml_files.write('      </bndbox>\n')
                xml_files.write('   </object>\n')
        xml_files.write('</annotation>')



