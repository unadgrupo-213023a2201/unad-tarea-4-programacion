#Autor: Samuel José Briceño Castro

# Importa clase Servicio
from Modelos.servicio import Servicio


# Clase para asesorías
class ServicioAsesoria(Servicio):

    # Método para calcular costo
    def calcular_costo(self, horas=1, impuesto=0, descuento=0):

        # Calcula subtotal
        subtotal = self.costo_base * horas

        # Aplica descuento
        subtotal -= subtotal * (descuento / 100)

        # Aplica impuesto
        subtotal += subtotal * (impuesto / 100)

        return subtotal

    # Método para mostrar información
    def mostrar_info(self):

        return f"Servicio Asesoría: {self.nombre} | Costo Base: ${self.costo_base}"