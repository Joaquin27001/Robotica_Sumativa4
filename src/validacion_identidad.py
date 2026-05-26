"""Módulo de validación de identidad para el sistema de registro."""

import re

# Límites para campos de texto
MIN_LARGO_TEXTO = 2
MAX_LARGO_TEXTO = 50

# Límites para RUT chileno
MIN_CUERPO_RUT = 1_000_000


def validar_texto(campo: str, valor: str) -> bool:
    """Valida que un campo de texto cumpla formato, largo y contenido.

    Args:
        campo: Nombre del campo evaluado.
        valor: Texto ingresado por el usuario.

    Returns:
        True si el valor es válido, False en caso contrario.
    """
    try:
        valor_limpio = valor.strip()

        if not valor_limpio:
            print(f"  Error: El campo '{campo}' no puede estar vacío.")
            return False

        if len(valor_limpio) < MIN_LARGO_TEXTO:
            print(f"  Error: '{campo}' debe tener al menos {MIN_LARGO_TEXTO} caracteres.")
            return False

        if len(valor_limpio) > MAX_LARGO_TEXTO:
            print(f"  Error: '{campo}' no puede superar los {MAX_LARGO_TEXTO} caracteres.")
            return False

        patron = r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$"
        if not re.match(patron, valor_limpio):
            print(f"  Error: '{campo}' solo debe contener letras y espacios.")
            return False

        return True

    except (TypeError, AttributeError):
        print(f"  Error: El campo '{campo}' recibió un valor inesperado.")
        return False


def existe_RUT(rut: str) -> bool:  # pylint: disable=invalid-name
    """Valida estructural y matemáticamente un RUT chileno.

    Args:
        rut: RUT ingresado por el usuariopython3 -m pylint src/validacion_identidad.py.

    Returns:
        True si el RUT es válido, False en caso contrario.
    """
    try:
        rut_limpio = rut.strip().replace(".", "").replace("-", "").upper()

        if not rut_limpio:
            print("  Error: El RUT no puede estar vacío.")
            return False

        patron = r"^\d{7,8}[0-9K]$"
        if not re.match(patron, rut_limpio):
            print("  Error: Formato de RUT inválido. Ejemplo válido: 12.345.678-9")
            return False

        cuerpo = rut_limpio[:-1]
        digito_ingresado = rut_limpio[-1]

        if int(cuerpo) < MIN_CUERPO_RUT:
            print("  Error: El cuerpo del RUT no corresponde a un RUT válido.")
            return False

        suma = 0
        multiplicador = 2

        for digito in reversed(cuerpo):
            suma += int(digito) * multiplicador
            multiplicador = multiplicador % 7 + 1

        residuo = 11 - (suma % 11)

        if residuo == 11:
            digito_calculado = "0"
        elif residuo == 10:
            digito_calculado = "K"
        else:
            digito_calculado = str(residuo)

        if digito_calculado != digito_ingresado:
            print("  Error: El dígito verificador del RUT es incorrecto.")
            return False

        return True

    except (ValueError, TypeError, AttributeError):
        print("  Error: El RUT ingresado contiene un valor inesperado.")
        return False
