#Autor: Samuel José Briceño Castro

# Importa excepción personalizada
from Excepciones.excepciones import ReservaError

# Importa logger
from Utilidades.logger import registrar_log

class Reserva:
    # Constructor
    def __init__(self, cliente, servicio, horas):

        # Guarda atributos
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    # Método para confirmar reserva
    def confirmar(self):

        # Cambia estado
        self.estado = "Confirmada"

        # Registra log
        registrar_log("Reserva confirmada")

    # Método para cancelar reserva
    def cancelar(self):

        # Cambia estado
        self.estado = "Cancelada"

        # Registra log
        registrar_log("Reserva cancelada")

    # Método para procesar reserva
    def procesar_reserva(self):

        try:

            # Verifica disponibilidad
            if self.servicio.disponible is False:
                raise ReservaError("Servicio no disponible")

            # Verifica horas inválidas
            if self.horas <= 0:
                raise ReservaError("Duración inválida")

        except ReservaError as error:

            # Registra error
            registrar_log(f"ERROR: {error}")

            # Muestra error
            print(error)

        else:

            # Confirma reserva
            self.confirmar()

            # Muestra mensaje
            print("Reserva procesada correctamente")

        finally:

            # Mensaje final
            print("Finalizó el proceso de reserva")

    # Método para mostrar información
    def mostrar_info(self):

        return f"Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Horas: {self.horas} | Estado: {self.estado}"