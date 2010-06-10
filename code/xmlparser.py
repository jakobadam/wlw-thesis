from xml.sax.handler import ContentHandler

class XMLParser(ContentHandler):
        '''Simple XML Parser. 
      
        Extracts node content from the elements in the xmlelements list. These
        elements MUST NOT be nested in the XML document.
        Note: Duplicate named elements will result in the content of the 
        last processed element.  
        '''
        def __init__(self, values={}, xmlelements=[]):
            '''
            Initializes instance of XMLParser.
            
            Args:
                values: dictionary where result is put.
                elements: list of XML element names to extract values from.
            '''
            ContentHandler.__init__(self)
            self.values = values
            self.xmlelements = xmlelements
            self.node_content = []
            self.in_element = False
            
        def startElement(self, name, attrs):
            if name in self.xmlelements:
                self.in_element = True
               
        def endElement(self,name):
            if self.in_element:
                self.values[name] = ''.join(self.node_content)
                self.node_content = []
                self.in_element = False
        
        def characters(self, string):
            if self.in_element:
                self.node_content.append(string)
