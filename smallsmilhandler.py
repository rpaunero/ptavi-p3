#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.tags = []
        self.dicc = {'root-layout': ['width', 'height', 'backgroundcolor'],
                     'region': ['id', 'top', 'bottom', 'left', 'right'],
                     'img': ['src', 'region', 'begin', 'dur'],
                     'audio': ['src', 'begin', 'dur'],
                     'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name in self.dicc:
            tmpdic = {}
            for atributo in self.dicc[name]:
                tmpdic[atributo] = attrs.get(atributo,"")
            self.tags.append([name, tmpdic])
            

    def get_tags(self):
        return self.tags
        

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    misDatos = cHandler.get_tags()
    print(misDatos)
