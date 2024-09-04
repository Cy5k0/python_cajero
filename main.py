# Excepciones del Banco
class NombreIncorrectoError(Exception):
    pass


class NumeroCuentaIncorrectoError(Exception):
    pass


class PinIncorrectoError(Exception):
    pass


# Clase usuario
class Usuario:
    def __init__(self, nombre, numero_cuenta, pin):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.pin = pin


USUARIO_CORRECTO = Usuario("Pepe", "123456789", "1234")


def Validar_usuario(usuario):
    """
    Validamos la información del usuario
    """

    # Validar la información
    if usuario.nombre != USUARIO_CORRECTO.nombre:
        raise NombreIncorrectoError
    ("El nombre que ingresaste es incorrecto")
    if usuario.numero_cuenta != USUARIO_CORRECTO.numero_cuenta:
        raise NumeroCuentaIncorrectoError(
            "El numero de cuenta que ingresaste es incorrecto"
        )
    if usuario.pin != USUARIO_CORRECTO.pin:
        raise PinIncorrectoError("El pin que ingresaste es incorrecto")


def cajero_electronico():
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:

        try:
            # Ingreso de datos del usuario
            nombre = input("Ingrese su nombre: ")
            numero_cuenta = input("Ingrese su numero de cuenta: ")
            pin = input("Ingrese su pin: ")

            # Crear una instancia
            usuario = Usuario(nombre, numero_cuenta, pin)

            # validar usuario
            Validar_usuario(usuario)

            # Todo bien 😎
            print("Accediste a tu cuenta")
            break

        except (
            NombreIncorrectoError,
            NumeroCuentaIncorrectoError,
            PinIncorrectoError,
        ) as e:
            intentos += 1
            print(f"Error {e}")
            if intentos < max_intentos:
                print(f"Tienes {max_intentos - intentos} intentos restantes")
            else:
                print("Alcanzaste la cantidad de intentos permitidos")

        finally:
            print("Se termino el intento de acceder")


# invocar la función
cajero_electronico()
