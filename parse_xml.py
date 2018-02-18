import xml.etree.ElementTree as ET

tree = ET.parse('n07753592_76.xml')
root = tree.getroot()

for child in root.iter('name'):
    print(child.tag, child.attrib)
    child.text = 'banana'

tree.write('output.xml')