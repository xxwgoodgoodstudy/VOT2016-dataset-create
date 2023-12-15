from PIL import Image
import os
import cv2
import glob
import sys
from tools.test import *


def resize_images(input_folder, output_folder, width, height):
    # 遍历输入文件夹中的所有视频文件夹
    for video_folder in os.listdir(input_folder):
        video_folder_path = os.path.join(input_folder, video_folder)
        # 确保当前文件是目录而不是文件
        if os.path.isdir(video_folder_path):
            output_path = os.path.join(output_folder, video_folder)
            os.makedirs(output_path,exist_ok=True)

            # 遍历输入文件夹中的所有图片文件
            for filename in os.listdir(video_folder_path):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    input_path = os.path.join(video_folder_path, filename)

                    # 打开图片
                    image = Image.open(input_path)

                    # 调整大小
                    resized_image = image.resize((width, height))
                    # 转换格式为JPEG
                    converted_image = resized_image.convert("RGB")

                    # 保存调整后的图片为JPEG格式
                    output_file_name = os.path.splitext(filename)[0] + ".jpg"
                    output_file_path = os.path.join(output_path, output_file_name)

                    # 保存调整后的图片
                    # resized_image.save(output_file_path)
                    converted_image.save(output_file_path)


# 设置输入文件夹、输出文件夹以及目标分辨率
input_folder = "G:/dataset/object_tracker/sonar/val/JPEGImages_initsize"
output_folder = "G:/dataset/object_tracker/sonar/val"
target_width = 1280
target_height = 964

# 调用函数进行批量修改图片分辨率
resize_images(input_folder, output_folder, target_width, target_height)
