"""
CENTRO DE BIOTECNOLOGIA AGROPECUARIO SENA

FICHA:    2877795
APRENDIZ: NICOLAS ANDRES ACOSTA HIGUERA
FECHA:    06 / 06 / 2024
PROGRMA:  Tablas de multiplicar Aleatorias
VERSION:  3.0
"""

# Importar modulos

# Importaciones de bibliotecas de terceros
from colorama import Fore, Back

# Importaciones locales
from modules.Fnc import *

def main():
    """
    Función principal del programa. Muestra un título, genera un número aleatorio de tablas de multiplicar,
    imprime las tablas y solicita al usuario si desea continuar.
    """

    print((Back.GREEN),(Fore.WHITE))
    titulo()
    mensaje()

    while True:
        # Generar número aleatorio entre 1 y 20
        num_tablas = generar_numero_aleatorio()
        print(f'Número de tablas a generar: {num_tablas}')

        # Generar tablas de multiplicar
        for i in range(1, num_tablas + 1):
            imprimir_tabla(i)
            input('\nPresione Enter para continuar . . .')

        # Preguntar si desea generar más tablas
        if not preguntar_repeticion():
            print('Gracias por usar el programa')
            break

if __name__ == "__main__":
    main()