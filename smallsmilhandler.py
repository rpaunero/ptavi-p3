#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):


    def __init__(self):
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('background-color',"")
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top'"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
        elif name == 'img':
            self.src_img = attrs.get('src',"")
            self.region_img = attrs.get('region',"")
            self.begin_img = attrs.get('begin',"")
            self.dur_img = attrs.get('dur',"")
        elif name == 'audio':
            self.src_audio = attrs.get('src',"")
            self.begin_audio = attrs.get('begin',"")
            self.dur_audio = attrs.get('dur',"")
        elif name == 'textstream':
            self.src_text = attrs.get('src',"")
            self.region_text = attrs.get('region',"")

    def get_tags(self):
        self.tags = [{'width': self.width, 'height': self.height, 'background-color': self.backgroundcolor},
                     {'id': self.id, 'top': self.top, 'bottom': self.bottom, 'left': self.left, 'right': self.right},
                     {'src': self.src_img, 'region': self.region_img, 'begin': self.begin_img, 'dur': self.dur_img},
                     {'src': self.src_audio, 'begin': self.begin_audio, 'dur': self.dur_audio},
                     {'src': self.src_text, 'region': self.region_text}]
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
