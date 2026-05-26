#codigo fuente sumativa4
cuentas = []

###---------------------------------------------------MAIN-----------------------------------------------------------###
def main():
    print("Bienvenido al sistema de creación de cuentas.")


    while True:
        print("Por favor, ingrese los siguientes datos para crear su cuenta.")


        Nombre = input("Ingrese su nombre: ")
        while (not ingrese_string(Nombre)):
            Nombre = input("Ingrese nuevamente su nombre: ")
        
        apellido_P = input("Ingrese su apellido paterno: ")
        while (not ingrese_string(apellido_P)):
            apellido_P = input("Ingrese nuevamente su apellido paterno: ")

        apellido_M = input("Ingrese su apellido materno: ")
        while (not ingrese_string(apellido_M)):
            apellido_M = input("Ingrese nuevamente su apellido materno: ")

        while existe_cuenta(Nombre, apellido_P, apellido_M):
            Nombre = input("Ingrese su nombre: ")
            while (not ingrese_string(Nombre)):
                Nombre = input("Ingrese nuevamente su nombre: ")
            
            apellido_P = input("Ingrese su apellido paterno: ")
            while (not ingrese_string(apellido_P)):
                apellido_P = input("Ingrese nuevamente su apellido paterno: ")

            apellido_M = input("Ingrese su apellido materno: ")
            while (not ingrese_string(apellido_M)):
                apellido_M = input("Ingrese nuevamente su apellido materno: ")


        RUT = input("ingrese su RUT (sin puntos ni guion): ")
        while (not existe_RUT(RUT)):
            RUT = input("Ese RUT ya existe. Ingrese otro RUT: ")


        contraseña = input("Ingrese su contraseña: ")
        while (not contraseña_valida(contraseña)):
            contraseña = input("Ingrese nuevamente: ")


        New_Account = {
            "Nombre": Nombre,
            "Apellido Paterno": apellido_P,
            "Apellido Materno": apellido_M,
            "RUT": RUT,
            "Contraseña": contraseña
        }


        Registrardatos(New_Account)


        opcion = input("¿Desea continuar? si/no: ").lower()
        while opcion not in ["si", "no"]:
            opcion = input("Opción no válida. Por favor, ingrese 'si' o 'no': ").lower()
        if opcion == "no":
            print("Gracias por usar el sistema de creación de cuentas. ¡Hasta luego!")
            break






###-----------------------------------------------------FUNCIONES---------------------------------------------------------###

def contraseña_valida(contraseña): #valida la contraseña ingresada por el usuario
    if len(contraseña) == 0:
        print("La contraseña no puede estar vacía.")
        return False
    if len(contraseña) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return False
    if len(contraseña) > 12:
        print("La contraseña no puede tener más de 12 caracteres.")
        return False
    if not any(char.isdigit() for char in contraseña):
        print("La contraseña debe contener al menos un número.")
        return False
    if not any(char.isupper() for char in contraseña):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False
    if not any(char.islower() for char in contraseña):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False
    if contraseña.isalnum():
        print("La contraseña debe contener al menos un carácter especial.")
        return False
    return True


def Registrardatos(cuenta): #agrega la cuenta creada a la lista de cuentas y muestra un mensaje de confirmación con los datos de la cuenta creada, excepto la contraseña por razones de seguridad.
    cuentas.append(cuenta)

    print("Cuenta creada exitosamente:")
    for i in cuentas:
        print(f"Nombre: {i['Nombre']}, Apellido Paterno: {i['Apellido Paterno']}, Apellido Materno: {i['Apellido Materno']}, RUT: {i['RUT']}")  


    return True


def existe_cuenta(Nombre, apellido_P, apellido_M): #verifica si ya existe una cuenta con el mismo nombre y apellidos ingresados por el usuario
    for cuenta in cuentas:
        if (cuenta["Nombre"] == Nombre and cuenta["Apellido Paterno"] == apellido_P and cuenta["Apellido Materno"] == apellido_M):
            print("Ya existe una cuenta con ese nombre y apellidos. Por favor, ingrese otros datos.")
            return True
    return False


def existe_RUT(rut): #valida el rut ingresado por el usuario, verificando que no esté vacío, que tenga una longitud adecuada, que contenga solo caracteres alfanuméricos y que cumpla con el formato del RUT chileno.
    if len(rut) == 0:
        print("El RUT no puede estar vacío.")
        return False
    if len(rut) < 9 or len(rut) > 10:
        print("El RUT debe tener entre 8 y 9 caracteres.")
        return False
    if not rut.isalnum():
        print("El RUT debe contener solo números y un dígito verificador al final.")
        return False
    if not rut.isdigit():
        if not alfanumerico(rut):
            return False
    return True


def alfanumerico(rut): #verifica la combinacion de letras y numeros en el rut para validar el formato del RUT chileno, que puede contener números y un dígito verificador al final, que puede ser un número o la letra 'K'.
    i = 0
    posicionLetras = []

    while i <= len(rut) - 1:
        if not rut[i].isdigit():
            posicionLetras.append(i)
        i += 1

    if len(posicionLetras) > 1:
        print("El RUT no puede contener más de un carácter no numérico.")
        return False
    if posicionLetras[0] != len(rut) - 1:
        print("El carácter no numérico en el RUT debe ser el dígito verificador, ubicado al final.")
        return False
    if  rut[posicionLetras[0]].upper() != 'K':
        print("El carácter no numérico en el RUT debe ser 'K' o 'k'.")
        return False
    return True


def ingrese_string(string):
    if (len(string) == 0) or (string.isspace()):
        print("No puede ingresar una palabra vacia.")
        return False
    if not string.isalpha():
        print("No puede ingresar números ni caracteres especiales.")
        return False
    if " " in string:
        print("El string no puede contener espacios.")
        return False
    return True




main()