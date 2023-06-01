# Deeplearning-homework2-topic
cutmix可视化图片，cutout可视化图片和mixup可视化图片，这三个文件用于生成经过数据增强后的样例图片，每种各三张，共九张。

png.py文件用于将从官网下载下来的二进制数据集转换为png格式，分别将数据集存储在train和test中。

CIFAR100(cutmix_dataset),CIFAR100(cutout_dataset),CIFAR100(mixup_dataset)这三个文件用于对数据集中的训练集进行处理，
加入经过数据增强后的图片，形成新的数据集，分别用于cutmix，cutout，mixup的训练

CIFAR(baseline)文件为baseline，使用Res18作为模型，对CIFAR100进行训练

CIFAR(cut_out),CIFAR(cut_mix),CIFAR(mix_up)三个文件分别是使用CIFAR100(cutout_dataset),CIFAR100(cutmix_dataset),CIFAR100(mixup_dataset)
这三个文件生成的数据集，以baseline作为模型，对数据集进行训练

一．	训练acc曲线
Baseline：经过10个epoch的训练后，训练准确率达到99.6%，训练损失下降为0.032，但在验证集上的准确率仅为54.2%，在4个epoch后训练集与验证集的准确率有明显分歧，存在过拟合现象
 
Cutout：在对训练集加入cutout后经过10个epoch的训练后，训练集准确率达到99.5%，训练损失下降到0.039，但验证集上的准确率为52.7%，仍较低，存在过拟合现象，并未达到预期目的。
![image](https://github.com/Timlllll/Deeplearning-homework2-topic1/assets/123872391/0450bdcb-0f54-4c6f-9e8f-75fb53f3bedd)
<img width="282" alt="image" src="https://github.com/Timlllll/Deeplearning-homework2-topic1/assets/123872391/3ce38312-0fc6-4d91-ba98-baaddae6a811">
cutmix：在对训练集加入cutmix后经过10个epoch的训练后，训练集准确率达到99.6%，训练损失下降到0.032，但验证集上的准确率为51.4%，仍较低，存在过拟合现象，并未达到预期目的。
<img width="293" alt="image" src="https://github.com/Timlllll/Deeplearning-homework2-topic1/assets/123872391/657da420-c73b-480a-af9b-1de2c083a3c3">
mixup：在对训练集加入mixup后经过10个epoch的训练后，训练集准确率达到90.8%，训练损失下降到0.431，但验证集上的准确率为38.7%，仍较低，存在过拟合现象，并未达到预期目的。
<img width="293" alt="image" src="https://github.com/Timlllll/Deeplearning-homework2-topic1/assets/123872391/f189edc7-b238-4e5f-9b95-9a2031d141b8">

