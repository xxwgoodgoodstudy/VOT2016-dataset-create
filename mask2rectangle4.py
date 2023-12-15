import cv2
import numpy as np
import os


def mask_find_bboxs(mask):
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)  # connectivity参数的默认值为8
    stats = stats[stats[:, 4].argsort()]
    return stats[:-1]  # 排除最外层的连通图


def main(input_folder):
    for video_folder in os.listdir(input_folder):
        video_folder_path = os.path.join(input_folder, video_folder)
        result_path = os.path.join(video_folder_path, 'groundtruth.txt')
        groundtruth = []
        # 遍历输入文件夹中的所有图片文件
        for filename in os.listdir(video_folder_path):

            if filename.endswith(".jpg") or filename.endswith(".png"):
                input_path = os.path.join(video_folder_path, filename)
                # 获取mask（灰度图）
                # mask = cv2.imread(input_path, cv2.COLOR_BGR2GRAY)
                image = cv2.imread(input_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # 转换成二值图
                ret, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
                bboxs = mask_find_bboxs(mask)

                x, y = bboxs[0][0], bboxs[0][1]
                w = bboxs[0][2]
                h = bboxs[0][3]
                groundtruth.append(f'{x},{y},{w},{h}')

                x0,y0 = bboxs[0][0], bboxs[0][1]
                x1 = bboxs[0][0] + bboxs[0][2]
                y1 = bboxs[0][1] + bboxs[0][3]
                start_point, end_point = (x0, y0), (x1, y1)
                color = (0, 0, 255)  # Red color in BGR；红色：rgb(255,0,0)
                thickness = 1  # Line thickness of 1 px
                mask_BGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # 转换为3通道图，使得color能够显示红色。
                mask_bboxs = cv2.rectangle(mask_BGR, start_point, end_point, color, thickness)
                cv2.imshow('show_image', mask_bboxs)
                cv2.waitKey(0)
        with open(result_path, "w") as fin:
            for line in groundtruth:
                fin.write(line + "\n")
                    # print(f'x0:{x0}, y0:{y0}, x1:{x1}, y1:{y1}')
                    # start_point, end_point = (x0, y0), (x1, y1)
                    # color = (0, 0, 255)  # Red color in BGR；红色：rgb(255,0,0)
                    # thickness = 1  # Line thickness of 1 px
                    # mask_BGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # 转换为3通道图，使得color能够显示红色。
                    # mask_bboxs = cv2.rectangle(mask_BGR, start_point, end_point, color, thickness)
                    #
                    # """
                    # # Displaying the image
                    # cv2.imshow('show_image', mask_bboxs)
                    # cv2.waitKey(0)
                    # """
                    # cv2.imwrite(r'\mask_bboxs.png', mask_bboxs)


if __name__ == '__main__':
    path = 'C:/Users/USER/Desktop/3'
    main(path)