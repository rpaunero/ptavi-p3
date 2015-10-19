#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import urllib
import json


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.misDatos = cHandler.get_tags()

    def __str__(self):
        linea = ''
        for sublista in self.misDatos:
            linea = linea + sublista[0]
            dicc = sublista[1]
            for atributo in dicc:
                if dicc[atributo] != "":
                    linea = linea + "\t" + atributo + "=" + (dicc[atributo])
        return (linea)

    def to_json(self, name):
        if name.split(".")[1] == "json":
            name = name
        elif name.split(".")[1] != "json":
            name = name.split(".")[0] + ".json"
#Pasar datos a formato json
        datosJson = json.dumps(self.misDatos)
#Crear el nuevo fichero con los datos en el nuevo formato
        with open(name, 'w') as ff:
            json.dump(datosJson, ff)

    def do_local(self):
        for sublista in self.misDatos:
            dicc = sublista[1]
            for atributo in dicc:
                if atributo == 'src':
                    if dicc[atributo].split('/')[0] == "http:":
                        urllib.request.urlretrieve(dicc[atributo], dicc[atributo].split('/')[-1])
                        dicc[atributo] = dicc[atributo].split('/')[-1]

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
        karaoke = KaraokeLocal(fichero)
        print(karaoke)
        karaoke.do_local()
        print(karaoke)
        karaoke.to_json(fichero)
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
