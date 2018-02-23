from time import sleep
import os
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def Inicio():
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t\t\t\t{0}MENU PRINCIPAL\n').format(GREEN)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}Escoja una opcion del Menu:\n\n').format(WHITE)
    sleep(0.2)
    print('\t\t\t\t\t{0}[{1}1{2}]{3} Ingresar Nuevo Usuario').format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    print('\t\t\t\t\t{0}[{1}2{2}]{3} Configuracion').format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}E{2}]{3} Salir\n\n\n').format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    etiqueta = ('\t\t\t\t\t{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Op
