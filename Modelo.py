from abc import ABC, abstractmethod

#Plantilla general para otras clases
class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass