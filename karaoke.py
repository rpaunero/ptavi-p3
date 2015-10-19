#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler


def crearlinea(misDatos):
    linea=''
    for sublista in misDatos:
        linea = linea + sublista[0]
        dicc = sublista[1]
        for atributo in dicc:      
            if dicc[atributo] != "":
                linea = linea + "\t" + atributo + "=" + (dicc[atributo] + " ")
    print(linea)

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichero)) 
    misDatos = cHandler.get_tags()
    crearlinea(misDatos)
