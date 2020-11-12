from xml.dom import minidom
import xml.sax

# parse an xml file by name
mydoc = minidom.parse('xml/myfile.xml')

items = mydoc.getElementsByTagName('to')

items[0].childNodes[0].data = "new data"
print(items[0].childNodes[0].data)

with open('xml/mytest.xml','w') as f:
    f.write(mydoc.toxml())


import xml.sax


# define a Custom ContentHandler class that extends ContenHandler
class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.postCount = 0
        self.entryCount = 0
        self.editMode = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        if(tagName == "to"):
            self.editMode = True


    # Handle endElement
    def endElement(self, tagName):
        self.editMode = False

    # Handle text data
    def characters(self, chars):
        if(self.editMode):
            chars = "tsadg"
            print(chars)

    # Handle startDocument
    def startDocument(self):
        print('About to start!')

    # Handle endDocument
    def endDocument(self):
        print('Finishing up!')


# handler = CustomContentHandler()
#
# xml.sax.parse("xml/myfile.xml", handler)
#
# xml.sax.xmlreader()



parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
# override the default ContextHandler
Handler = CustomContentHandler()
parser.setContentHandler( Handler )
parser.parse("xml/myfile.xml")


