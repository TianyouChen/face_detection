本仓库是ssd源码以及自己编写的widerface、fddb人脸数据处理程序以及转化为lmdb的程序,进入caffe_ssd目录下编译caffe_ssd，方法参考wiki 教程。
其中face_data下存放的是widerface和fddb数据以及标签文件

models/vgg_iter_260000.caffemodel是训练最好的人脸检测模型，目前最高精度map=83.7%，安卓上检测40ms每张图，并且人脸数增加，检测效率不降低；

models/train-ssd-face-384-8.prototxt是训练网络

models/deploy-ssd-face-384-8.prototxt是模型的测试网络

python/wider.py是处理widerface数据程序，在终端输入python wider.py --FileDir=your path for input --OutDir=your_out_path运，程序处理FileDir/wider_face_all_bbx_gt.txt并会在OutDir/下生成wider_all_data.txt,里面对应保存的是widerface图像和边框标注文件的路径，此外还对应生成wider_all_box存放对应每一张图片的人脸groundtrue坐标。

face_data在百度云盘,链接: https://pan.baidu.com/s/1C7CYy8zldH3OSSJj_W4rMw 提取码: rjmj

python/create_wider_lmdb.sh和create_wider_lmdb.sh是调用caffe_ssd工具生成lmdb脚本，./create_*_lmdb.sh运行脚本，会在相应目录下生成训练所需的widerface以及fddb人脸数据的lmdb
