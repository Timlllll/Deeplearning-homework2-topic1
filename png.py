import cv2
import numpy as np
file = '/Users/lizijian/data/cifar-100-python/train'
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo,encoding='latin1')
    return dict
dict1 = unpickle(file)
print(dict1)
for i in range(50000):#我保存的50000张训练集
    img = dict1["data"][i]#得到图片的数据
    img = np.reshape(img, (3, 32,32))  #转为三维图片数组
    img = img.transpose((1,2,0))#通道转换为CV2的要求形式
    img_name = dict1["filenames"][i]#拿到图片的名字
    img_label = str(dict1["fine_labels"][i])#拿到图片的标签
    # cv2.imwrite("/Users/lizijian/data/cifar-100-python/转png/train/"+ str(i) + "_" + img_label, img)#保存
    cv2.imwrite("/Users/lizijian/data/cifar-100-python/转png/train/" +str(i) +"_" + img_label+"+"+img_name , img)

