# VOT2016-dataset-create
制作VOT2016格式的单目标跟踪验证集，用于siammask的test.py

步骤： 

1、运行rename.py修改图片名称（1.png改成00001.jpg） 

2、运行imagecut.py改变图片大小（yutube-vos大小为1280*720）

3、用eiseg标注图片，生成mask掩膜图片 

4、运行mask2rectangle4.py生成groundtruth.txt，包含矩形框x、y、w、h信息 

5、转到matlab运行process_seqs.m生成groundtruth.txt，包含旋转框四个角坐标信息

6、运行gen_json.py生成VOT2016.json


参考：

矩形框转旋转框：https://zhuanlan.zhihu.com/p/59486758

如何把数据集做成VOT2018竞赛的数据集那种格式：https://www.zhihu.com/question/334410652

matlab代码：https://github.com/vojirt/bbox_from_segmentation
