import os

cwd = os.getcwd()
wd = os.path.join(cwd,'VOCdevkit/VOC2018/Annotations/')

filenames = os.listdir(wd)
n = len(filenames)
train_f = open('VOCdevkit/VOC2018/ImageSets/Main/train.txt', 'w')
val_f = open('VOCdevkit/VOC2018/ImageSets/Main/val.txt','w')
for i in range(n//10):
    id, ext = filenames[i].split('.')
    val_f.write('%s\n'%(id))

for i in range(n//10,n):
    id, ext = filenames[i].split('.')
    train_f.write('%s\n'%(id))

wd = os.path.join(cwd,'VOCdevkit/VOC2018/JPEGImages/')
all_fnames = os.listdir(wd)
test_f = open('test.txt','w')
count = 0
for name in all_fnames:
    if name not in filenames:
        id, ext = name.split('.')
        test_f.write('%s%s.jpg\n'%(wd, id))
        count+=1
    if count > n//10:
        break

test_f.close()
train_f.close()
val_f.close()