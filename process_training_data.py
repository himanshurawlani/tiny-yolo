import os
from shutil import copyfile
import xml.etree.ElementTree as ET

cwd = os.getcwd()
classes = os.listdir(cwd)
new_annotation_dir = os.path.join("train", "Annotation")
new_image_dir = os.path.join("train", "Images")
os.makedirs(new_image_dir)
os.makedirs(new_annotation_dir)

# Iterating over every class folder in the current directory
for class_name in classes:
    # Skip the python file in the current directory
    if class_name.find('.py') >= 0:
        continue
    curr_class_dir = os.path.join(cwd, class_name)
    folders = os.listdir(curr_class_dir)
    # Expected folders array to be ['n07753592', 'Annotation']
    if folders[0] == "Annotation":
        image_dir = os.path.join(curr_class_dir,folders[1])
        annotation_dir = os.path.join(curr_class_dir, "Annotation", folders[1])
        class_id = folders[1]
    else:
        image_dir = os.path.join(curr_class_dir,folders[0])
        annotation_dir = os.path.join(curr_class_dir, "Annotation", folders[0])
        class_id = folders[0]

    # Creating a set of ids for efficient intersection operation
    all_image_ids = set([image_filename.split('.')[0] for image_filename in os.listdir(image_dir)])
    all_annotation_ids = set([annotation_filename.split('.')[0] for annotation_filename in os.listdir(annotation_dir)])

    # Performing intersection of the the two sets
    common_ids = all_image_ids & all_annotation_ids
    print("Total annotated images in", class_name, ":", len(common_ids), sep=' ')

    for id in common_ids:
        copyfile(os.path.join(image_dir,id) + '.JPEG', os.path.join(new_image_dir,str(id)) + '.jpg')

    # Processing and copying the XML file
    obj_name = class_name.lower()
    for file in common_ids:
        file_name = str(file) + '.xml'
        in_file = open(os.path.join(annotation_dir,file_name))
        tree = ET.parse(in_file)
        root = tree.getroot()
        filename = root.find('filename')
        filename.text = filename.text + '.jpg'
        for obj in root.iter('object'):
            name_tag = obj.find('name')
            name_tag.text = obj_name
        tree.write(os.path.join(new_annotation_dir,file_name))
