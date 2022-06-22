#! /usr/bin/env python3
#
# For HCS OME-XML, Bio-Formats rewrites the Image IDs to be of
# format Image:<series>. Any deviation including a different
# starting index will lead to erroneous mapping as the ImageRef
# values are not updated. 

import shutil
import sys
import xml.etree.ElementTree as ET

filename = sys.argv[1]
OME_NS = "http://www.openmicroscopy.org/Schemas/OME/2016-06"
ET.register_namespace('', OME_NS)

shutil.copyfile(filename, filename + ".bak")
tree = ET.parse(filename)
root = tree.getroot()

for index, imageref in enumerate(
        root.findall(f"./*/*/*/{{{OME_NS}}}ImageRef")):
    imageref.set("ID",f"Image:{index}")

for index, image in enumerate(root.findall(f"./{{{OME_NS}}}Image")):
    image.set("ID",f"Image:{index}")

tree.write(filename, encoding="utf-8",xml_declaration=True)
