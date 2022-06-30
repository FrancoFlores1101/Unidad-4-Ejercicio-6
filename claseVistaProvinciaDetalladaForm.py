import tkinter as tk
from claseProvincia import Provincia
from Tiempo import Tiempo
from claseVistaProvinciaForm import VistaProvinciaForm


class VistaProvinciaDetalladaForm(VistaProvinciaForm):
    _fields = VistaProvinciaForm._fields + ("Temperatura", "Sensación térmica", "Humedad")

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
    

    def mostrarEstadoProvinciaEnFormulario(self, unaProvincia:Provincia, tiempo:Tiempo):
        # Muestra los atributos de la provincia y su tiempo asociado
        values = (unaProvincia.getNombre(), unaProvincia.getCapital(), unaProvincia.getHabitantes(), unaProvincia.getDepartamentos(), tiempo.getTemperatura(), tiempo.getSensacionTermica(), tiempo.getHumedad())
        # Limpia cada entrada del formulario y la llena con los datos correspondientes
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))