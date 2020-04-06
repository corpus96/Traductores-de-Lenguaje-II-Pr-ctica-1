'''
Traductores de Lenguaje II - Practica 1
Alumno: Emmanuel Corpus Ávila

------------------------------------
Detalles:
|
 ---- Parte 1:
|       -> Ingresar cadena como el ejemplo anterior
|       -> Devolver cadena postfijo
|       -> Verificar si es trivialidad
 ---- Parte 2:
|       -> Lo mismo pero de postfijo a infijo
|       -> [PISTA] Son muy parecidos
 ---- General:
|       ->Hacer funcion coincidir
|       ->Se salta toda la cadena que se pone en coincidir
'''
import os
import time
from colorama import Fore

glob_flag = True
vueltas = 0

def menu():
    global vueltas

    exit_flag = False

    while(exit_flag == False):
        os.system("cls")
        final_string = ""
        vueltas = 0
        c = 0

        print("\t ----------------------------------------------")
        print("\t|   ANALIZADOR SINTACTICO DECENDENTE RECURSIVO |")
        print("\t ----------------------------------------------")
        print("\n\t\t   (1) Infijo -> Postfijo")
        print("\t\t   (2) Postfijo -> Infijo")
        print("\t\t   (0) Salir del programa")
        menu_option = input("\t\t   Ingrese opcion: ")

        if(menu_option == "1"):
            infijo_postfijo()
        elif(menu_option == "2"):
            postfijo_infijo()
        elif(menu_option == "0"):
            print("Saliendo del programa...")
            exit_flag = True
        else:
            print("Esa opcion no esta en el menu:")

        input("\nPresione cualquier tecla para continuar")

def infijo_postfijo():
    cadena = input("Ingresar cadena: ")

    if cadena == "" or cadena == " ":
        print("\n\033[32m" + "Cadena aceptada")
        print("\033[39m")
    else:
        expr(cadena)

def postfijo_infijo():
    cadena = input("Ingresar la cadena: ")

    if cadena == "" or cadena == " ":
        print("\n\033[32m" + "Cadena aceptada")
        print("\033[39m")
    else:
        expr_v2(cadena)

#infijo -> postfijo
def expr(cadena):
    global glob_flag
    contador = len(cadena)
    c = 0
    glob_flag = True

    #Recorrer cada caracter de la cadena
    while(c < contador):
        c = term(c, cadena)
        c = resto(c, cadena, contador)

        if c != None:
            if c >= contador or c == None:
                break
        else:
            break

    if glob_flag == True:
        print("\n\033[32m" + "Cadena aceptada")
        print("\033[39m")

#postfijo -> infijo
def expr_v2(cadena):
    global glob_flag
    contador = len(cadena)
    c = 0


    while c < contador:
        glob_flag = True
        c = term_v2(c, cadena)
        c = resto_v2(c, cadena, contador)

        if c != None:
            if c >= contador or c == None:
                vueltas = 0
                break
        else:
            vueltas = 0
            break

    if glob_flag == True:
        print("\n\033[32m" + "Cadena aceptada")
        print("\033[39m")

#infijo -> postfijo
def term(c, cadena):
    global glob_flag
    if(cadena[c].isdigit()):
        t = cadena[c]
        c = coincidir(cadena[c], c)
        print(t, end='')
    else:
        print("\033[31m" + "\nERROR DE SINTAXIS")
        print("\033[39m")
        glob_flag = False
        exit()

    return c

#posftijo -> infijo_postfijo
def term_v2(c, cadena):
    global glob_flag
    if(cadena[c].isdigit()):
        t = cadena[c]
        c = coincidir(cadena[c], c)
        print(t, end="")
    else:
        print("\033[31m" + "\nERROR DE SINTAXIS")
        print("\033[39m")
        glob_flag = False
        exit()

        c = -1

    return c

def coincidir(symbol, c):
    global glob_flag
    line = "0123456789+-"
    f = False

    for l in line:
        if symbol == l:
            res = c + len(symbol)
            f = True

    if f == False:
        print("\033[31m" + "\nSimbolo no reconocido(1)")
        print("\033[39m")
        glob_flag = False
        exit()

    return res

# infijo -> postfijo
def resto(c, cadena, contador):
    global glob_flag
    if c < contador:
        if(cadena[c] == '+'):
            c = coincidir('+', c)
            c = term(c, cadena)

            print('+', end='')
            c = resto(c, cadena, contador)

            return c
        elif(cadena[c] == '-'):
            c = coincidir('-', c)
            c = term(c, cadena)

            print('-', end='')
            c = resto(c, cadena, contador)


            return c
        else:
            glob_flag = False
            print("\033[31m" + "\nSimbolo no reconocido")
            print("\033[39m")
            exit()

#postfijo -> infijo
def resto_v2(c, cadena, contador):
    global glob_flag
    global vueltas
    vueltas = vueltas + 1
    if c < contador:
        if vueltas == 1:
            if(c != contador - 1):
                if(cadena[c + 1] == '+'):
                    c = coincidir('+', c)
                    print('+', end="")
                    c = term_v2(c - 1, cadena)
                    c = resto_v2(c, cadena, contador)

                    return c
                elif(cadena[c + 1] == '-'):
                    c = coincidir('-', c)
                    print('-', end="")
                    c = term_v2(c - 1 , cadena)
                    c = resto_v2(c, cadena, contador)

                    return c
                else:
                    glob_flag = False
                    print("\033[31m" + "\nSimbolo no reconocido(2)")
                    print("\033[39m")
                    exit()
        else:
            if (c != contador - 1):
                if(cadena[c + 2] == '+'):
                    c = coincidir('+', c)
                    print('+', end="")
                    c = term_v2(c, cadena)
                    c = resto_v2(c, cadena, contador)

                    return c
                elif(cadena[c + 2] == '-'):
                    c = coincidir('-', c)
                    print('-', end="")
                    c = term_v2(c, cadena)
                    c = resto_v2(c, cadena, contador)

                    return c
                else:
                    glob_flag = False
                    print("\033[31m" + "\nSimbolo no reconocido(2)")
                    print("\033[39m")
                    exit()


menu()
