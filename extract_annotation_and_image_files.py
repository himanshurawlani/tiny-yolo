import os
from shutil import copyfile,move

cwd = os.getcwd()

image_dir = os.path.join(cwd,'VOCdevkit/VOC2018/JPEGImages/')
all_images = os.listdir(image_dir)
all_image_ids = []
for i in all_images:
    id, ext = i.split('.')
    all_image_ids.append(id)
all_image_ids = set(all_image_ids)

annotations_dir = os.path.join(cwd,'VOCdevkit/VOC2018/Annotations/')
annotated_images = os.listdir(annotations_dir)
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
        os.remove(annotations_dir+i+'.xml')

print(count,"annotations and corresponding images found.", sep=' ')

new_image_dir = os.path.join(image_dir, 'Images/')
os.makedirs(new_image_dir)
new_annotations_dir = os.path.join(annotations_dir, 'Annotations/')
os.makedirs(new_annotations_dir)

count = 0
for i in all_image_ids:
    if i in annotated_image_ids:
        count+=1
        copyfile(annotations_dir+i+'.xml',new_annotations_dir+i+'.xml')
        copyfile(image_dir+i+'.jpg', new_image_dir+i+'.jpg')
    else:
        os.remove(image_dir + i + '.jpg')

print(count,"annotated image files extracted.", sep=' ')


move(new_image_dir,'darkflow/train/')
print('Moved images to darkflow/train/Images')
move(new_annotations_dir,'darkflow/train/')
print('Moved annotations to darkflow/train/Annotations')