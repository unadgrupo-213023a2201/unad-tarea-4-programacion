# Función para registrar logs

def registrar_log(mensaje):

    # Abre el archivo en modo agregar
    with open("logs.txt", "a", encoding="utf-8") as archivo:

        # Escribe el mensaje en el archivo
        archivo.write(mensaje + "\n")