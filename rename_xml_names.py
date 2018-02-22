import xml.etree.ElementTree as ET
import os

cwd = os.getcwd()
annotations_dir = os.path.join(cwd,'darkflow/train/Annotations/')
os.chdir(annotations_dir)

obj_name = 'banana'

new_annotations_dir = os.path.join(annotations_dir,'Annotations/')
os.makedirs(new_annotations_dir)

for file in os.listdir(annotations_dir):
    if file.find('.xml') == -1:
        continue
    in_file = open(file)
    tree = ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):
        name_tag = obj.find('name')
        name_tag.text = obj_name
    tree.write(new_annotations_dir+file)
