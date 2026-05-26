continuar = True

while continuar:

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    while True:
        rut = input("RUT: ")

        if not existe_RUT(rut):
            break

        print("RUT ya existe")

    while True:
        contraseña = input("Contraseña: ")

        if contraseña_valida(contraseña):
            break

        print("Contraseña inválida")

    usuario = {
        "nombre": nombre,
        "rut": rut,
        "contraseña": contraseña
    }

    Registrardatos(usuario)

    opcion = input("¿Desea continuar? si/no: ").lower()

    if opcion != "si":
        continuar = False