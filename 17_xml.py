from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('xml/myfile.xml')

items = mydoc.getElementsByTagName('to')

items[0].childNodes[0].data = "new data"
print(items[0].childNodes[0].data)

with open('xml/mytest.xml','w') as f:
    f.write(mydoc.toxml())