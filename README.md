制作VOT2016格式的单目标跟踪验证集，用于siammask的test.py

步骤： 

1、运行rename.py修改图片名称（1.png改成00001.jpg） 

2、运行imagecut.py改变图片大小（yutube-vos大小为1280*720）

3、用eiseg标注图片，生成mask掩膜图片 

4、运行mask2rectangle4.py生成groundtruth.txt，包含矩形框x、y、w、h信息 

5、转到matlab运行process_seqs.m生成groundtruth.txt，包含旋转框四个角坐标信息

6、运行gen_json.py生成VOT2016.json
