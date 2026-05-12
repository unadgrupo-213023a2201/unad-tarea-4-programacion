#Autor: Samuel José Briceño Castro

# Importa herramientas abstractas
from abc import abstractmethod

# Importa clase abstracta principal
from Modelos.modelo import Entidad

# Importa excepción
from Excepciones.excepciones import ServicioError


# Clase abstracta Servicio
class Servicio(Entidad):

    # Constructor
    def __init__(self, nombre, costo_base, disponible=True):

        # Guarda atributos
        self.nombre = nombre
        self.costo_base = costo_base
        self.disponible = disponible

        # Valida datos
        self.validar()

    # Método de validación
    def validar(self):

        # Verifica costo inválido
        if self.costo_base <= 0:
            raise ServicioError("Costo inválido")

    # Método abstracto para calcular costo
    @abstractmethod
    def calcular_costo(self, horas=1, impuesto=0, descuento=0):
        pass

    # Método abstracto para describir servicio
    @abstractmethod
    def mostrar_info(self):
        pass