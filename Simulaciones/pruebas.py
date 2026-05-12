# Importa clases
from Modelos.cliente import Cliente
from Modelos.servicio_sala import ServicioSala
from Modelos.servicio_equipo import ServicioEquipo
from Modelos.servicio_asesoria import ServicioAsesoria
from Modelos.reserva import Reserva

# Importa excepciones
from Excepciones.excepciones import ClienteError
from Excepciones.excepciones import ServicioError
from Excepciones.excepciones import ReservaError

# Importa logger
from Utilidades.logger import registrar_log


# Función principal de pruebas
def ejecutar_pruebas():

    # Mensaje inicial
    print("\n========== INICIO DE PRUEBAS ==========\n")



    # ==================================================
    # PRUEBAS VALIDAS
    # ==================================================

    print("========== OPERACIONES VALIDAS ==========\n")


    # ---------------- OPERACION 1 ----------------
    # Cliente válido

    try:

        cliente1 = Cliente(
            "Samuel",
            "samuel@gmail.com",
            "3001234567"
        )

        print(cliente1.mostrar_info())

    except ClienteError as error:

        registrar_log(f"ERROR CLIENTE: {error}")

        print(error)



    # ---------------- OPERACION 2 ----------------
    # Servicio válido

    try:

        servicio1 = ServicioSala(
            "Sala Premium",
            100
        )

        print(servicio1.mostrar_info())

    except ServicioError as error:

        registrar_log(f"ERROR SERVICIO: {error}")

        print(error)



    # ---------------- OPERACION 3 ----------------
    # Servicio válido

    try:

        servicio3 = ServicioAsesoria(
            "Consultoría",
            200
        )

        print(servicio3.mostrar_info())

    except ServicioError as error:

        registrar_log(f"ERROR SERVICIO: {error}")

        print(error)



    # ---------------- OPERACION 4 ----------------
    # Reserva válida

    try:

        reserva1 = Reserva(
            cliente1,
            servicio1,
            3
        )

        reserva1.procesar_reserva()

        print(reserva1.mostrar_info())

    except ReservaError as error:

        registrar_log(f"ERROR RESERVA: {error}")

        print(error)



    # ---------------- OPERACION 5 ----------------
    # Cálculo válido

    try:

        costo = servicio3.calcular_costo(
            5,
            19,
            10
        )

        print(f"Costo calculado: ${costo}")

    except Exception as error:

        registrar_log(f"ERROR GENERAL: {error}")

        print(error)




    # ==================================================
    # PRUEBAS INVALIDAS
    # ==================================================

    print("\n========== OPERACIONES INVALIDAS ==========\n")



    # ---------------- OPERACION 6 ----------------
    # Cliente inválido

    try:

        cliente2 = Cliente(
            "",
            "correo",
            "abc"
        )

        print(cliente2.mostrar_info())

    except ClienteError as error:

        registrar_log(f"ERROR CLIENTE: {error}")

        print(error)



    # ---------------- OPERACION 7 ----------------
    # Servicio inválido

    try:

        servicio2 = ServicioEquipo(
            "Laptop",
            -50
        )

        print(servicio2.mostrar_info())

    except ServicioError as error:

        registrar_log(f"ERROR SERVICIO: {error}")

        print(error)



    # ---------------- OPERACION 8 ----------------
    # Reserva inválida por duración

    try:

        reserva2 = Reserva(
            cliente1,
            servicio3,
            -2
        )

        reserva2.procesar_reserva()

    except ReservaError as error:

        registrar_log(f"ERROR RESERVA: {error}")

        print(error)



    # ---------------- OPERACION 9 ----------------
    # Servicio no disponible

    try:

        servicio1.disponible = False

        reserva3 = Reserva(
            cliente1,
            servicio1,
            2
        )

        reserva3.procesar_reserva()

    except ReservaError as error:

        registrar_log(f"ERROR RESERVA: {error}")

        print(error)



    # ---------------- OPERACION 10 ----------------
    # Encadenamiento de excepciones

    try:

        valor = int("abc")

    except ValueError as error:

        try:

            raise ReservaError(
                "Conversión inválida"
            ) from error

        except ReservaError as nuevo_error:

            registrar_log(
                f"ERROR ENCADENADO: {nuevo_error}"
            )

            print(nuevo_error)



    # Mensaje final
    print("\n========== FIN DE PRUEBAS ==========\n")