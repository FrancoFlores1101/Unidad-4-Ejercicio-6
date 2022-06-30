import json
import requests
from claseProvincia import Provincia


class Tiempo:
    __temperatura = None
    __sensacion= None
    __humedad = None
    def __init__(self, unaProvincia:Provincia) -> None:
        aux = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=825d2666936ffeb12928cc97daea10ae".format(unaProvincia.getCapital())).content)
        self.__temperatura = aux["main"]["temp"]
        self.__sensacion = aux["main"]["feels_like"]
        self.__humedad = aux["main"]["humidity"]
        pass
    def getTemperatura(self):
        return self.__temperatura
    def getSensacionTermica(self):
        return self.__sensacion
    def getHumedad(self):
        return self.__humedad
