# Nombre del script: Script para manejo de clientes
# Autor: Andres Alfonso Julio Hernandez

from Modelos.modelo import Entidad
from Excepciones.excepciones import ClienteError


class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    # GETTERS    
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

   
    # SETTERS
    def set_nombre(self, nombre):

        if not nombre or not isinstance(nombre, str):
            raise ClienteError("Nombre inválido")

        self.__nombre = nombre

    def set_correo(self, correo):

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__correo = correo

    def set_telefono(self, telefono):

        if not telefono.isdigit():
            raise ClienteError("Teléfono inválido")

        self.__telefono = telefono


    # MÉTODOS
    def mostrar_info(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )