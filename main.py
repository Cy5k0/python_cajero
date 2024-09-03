# Excepciones del Banco


class NombreIncorrectoError(Exception):
    pass


class NumeroCuentaIncorrectoError(Exception):
    pass


class PinIncorrectoError(Exception):
    pass


# Constantes
NOMBRE_CORRECTO = "Pepe"
NUMERO_CUENTA_CORRECTO = "123456789"
PIN_CORRECTO = "1234"


def cajero_electronico():
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:

        try:
            # Ingreso de datos del usuario
            nombre = input("Ingrese su nombre: ")
            numero_cuenta = input("Ingrese su numero de cuenta: ")
            pin = input("Ingrese su pin: ")

            # Validar la información
            if nombre != NOMBRE_CORRECTO:
                raise NombreIncorrectoError
            ("El nombre que ingresaste es incorrecto")
            if numero_cuenta != NUMERO_CUENTA_CORRECTO:
                raise NumeroCuentaIncorrectoError(
                    "El numero de cuenta que ingresaste es incorrecto"
                )
            if pin != PIN_CORRECTO:
                raise PinIncorrectoError("El pin que ingresaste es incorrecto")

            # Si todo va bien
            print("Felicidades pudiste acceder a tu cuenta")
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


# invocar la función
cajero_electronico()
