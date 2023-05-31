# Deeplearning-homework2-topic
cutmix可视化图片，cutout可视化图片和mixup可视化图片，这三个文件用于生成经过数据增强后的样例图片，每种各三张，共九张。

png.py文件用于将从官网下载下来的二进制数据集转换为png格式，分别将数据集存储在train和test中。

CIFAR100(cutmix_dataset),CIFAR100(cutout_dataset),CIFAR100(mixup_dataset)这三个文件用于对数据集中的训练集进行处理，
加入经过数据增强后的图片，形成新的数据集，分别用于cutmix，cutout，mixup的训练

CIFAR(baseline)文件为baseline，使用Res18作为模型，对CIFAR100进行训练

CIFAR(cut_out),CIFAR(cut_mix),CIFAR(mix_up)三个文件分别是使用CIFAR100(cutout_dataset),CIFAR100(cutmix_dataset),CIFAR100(mixup_dataset)
这三个文件生成的数据集，以baseline作为模型，对数据集进行训练
