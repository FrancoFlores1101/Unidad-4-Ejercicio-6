from typing import List
from claseProvincia import Provincia
from claseManejadorProvincias import ManejadorProvincias
from claseObjectEncoder import ObjectEncoder


class RepositorioProvincias:
    __conn = None
    __manejador = None
    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)
    def obtenerListaProvincias(self) :
        return self.__manejador.getListaProvincias()
    def agregarProvincia(self, unaProvincia):
        self.__manejador.agregarProvincia(unaProvincia)
        return unaProvincia
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
