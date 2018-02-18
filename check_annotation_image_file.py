import os

cwd = os.getcwd()

wd = os.path.join(cwd,'VOCdevkit/VOC2018/JPEGImages/')
all_images = os.listdir(wd)
all_image_ids = []
for i in all_images:
    id, ext = i.split('.')
    all_image_ids.append(id)
all_image_ids = set(all_image_ids)

wd = os.path.join(cwd,'VOCdevkit/VOC2018/Annotations/')
annotated_images = os.listdir(wd)
annotated_image_ids = []
for i in annotated_images:
    id, ext = i.split('.')
    annotated_image_ids.append(id)
annotated_image_ids = set(annotated_image_ids)

count = 0
for i in annotated_image_ids:
    if i in all_image_ids:
        count+=1
    else:
        os.remove(wd+i+'.xml')

print(count)