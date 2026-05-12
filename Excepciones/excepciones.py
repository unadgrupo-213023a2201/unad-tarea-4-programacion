# Nombre del script: Manejo de exepciones
# Autor: Andres Alfonso Julio Hernandez

class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass

class ReservaError(Exception):
    pass