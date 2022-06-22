#! /usr/bin/env python3
#
# The Well.Row and Well.Column elements are expected to be
# 0-based indexed but the original companion files had
# 1-based indexed values

import shutil
import sys
import xml.etree.ElementTree as ET

filename = sys.argv[1]
OME_NS = "http://www.openmicroscopy.org/Schemas/OME/2016-06"
ET.register_namespace('', OME_NS)

shutil.copyfile(filename, filename + ".bak")
tree = ET.parse(filename)
root=tree.getroot()
for well in root.findall(f"./*/{{{OME_NS}}}Well"):
    well.set("Row", str(int(well.attrib["Row"])-1))
    well.set("Column", str(int(well.attrib["Column"])-1))

tree.write(filename, encoding="utf-8",xml_declaration=True)
