import os


def rename_images(folder_path):
    # 遍历输入文件夹中的所有视频文件夹
    for video_folder in os.listdir(folder_path):
        video_folder_path = os.path.join(folder_path, video_folder)
        # 确保当前文件是目录而不是文件
        if os.path.isdir(video_folder_path):
            # 获取文件夹中的所有图片文件
            image_files = [f for f in os.listdir(video_folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
            image_files.sort(key=lambda x: int(os.path.splitext(x)[0]))  # 自定义排序函数

            # 按顺序重命名图片
            for i, filename in enumerate(image_files):
                # 构造新的文件名
                new_filename = f"{str(i + 1).zfill(5)}.jpg"  # 使用zfill填充零

                # 构造旧文件路径和新文件路径
                old_filepath = os.path.join(video_folder_path, filename)
                new_filepath = os.path.join(video_folder_path, new_filename)

                # 重命名文件
                os.rename(old_filepath, new_filepath)
                print(f"Renamed {filename} to {new_filename}")


# 调用函数进行重命名，指定要重命名的文件夹路径
folder_path = "G:/dataset/object_tracker/sonar/val"
rename_images(folder_path)