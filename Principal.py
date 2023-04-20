#!/usr/bin/env python3

import json
from os import system
from Funciones import*

with open("Farmacia.json") as f:
    farmacias = json.load(f)

while True:
    system("clear")
    print ("Menu principal")
    print ("-"*55)
    print ("1. Listar informacíon.")
    print ("2. Contar Información.")
    print ("3. Buscar o filtrar información.")
    print ("4. Buscar informacion relacionada.")
    print ("5. Ejercicio libre.")
    print ("6. Ejercicio libre 2.")
    print ("7. Salir del programa.")
    opcion=int(input("Opcion: "))
    if opcion == 1:
        system("clear")
        print ("Muestra una lista de los propietarios de cada farmacia.")
        print ("-"*55)
        count=1
        for x in ListarInformacion(farmacias):
            print ("Propietario %i: %s." %(count,x.get("propietario")))
            count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 2:
        system("clear")
        print ("Contar el total de farmacias que pertenecen a un codigo postal")
        print ("-"*55)
        cad=input("Introduce un codigo postal> ")
        print ("Hay un total de %i farmacias con ese codigo postal." %(ContarInformacion(farmacias,cad)))
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 3:
        system("clear")
        print ("Mostrar propietario y descripcion de las farmacias que pertezcan a un codigo postal.")
        print ("-"*55)
        count=1
        cad=input("Introduce un codigo postal> ")
        for x in FiltrarInformacion(farmacias,cad):
            print ("Farmacia %i: %s." %(count,x.get("propietario")))
            print ("Descripcion: %s." %(x.get("descripcion")))
            print ()
            count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 4:
        system("clear")
        print ("Se va a buscar en la descripcion de las farmacias que existan las dos palabras introducida.")
        print ("-"*55)
        count=1
        cad=input("Introduce la primera palabra> ")
        cad1=input("Introduce la segundo palabra> ")
        for x in InformacionRelacionada(farmacias,cad,cad1):
            print ("Direccion %i: %s." %(count,x))
            count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 5:
        system("clear")
        print ("Mostrar direccion y telefono de las farmacias abiertas en un rango de hora.")
        print ("-"*55)
        count=1
        print ("Debes introducir dos horas con el formato HH:MM incluyendo el 0 delante de los numeros menores de 10.")
        cad=input("Introduce la primera hora> ")
        cad1=input("Introduce la segunda hora> ")
        for x in EjercicioLibre(farmacias,cad,cad1):
            print ("Farmacia %i".center(50, "=")%(count))
            print ("Direccion: %s." %(x.get("direccion")))
            print ("Telefono: %s." %(x.get("telefono")))
            count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 6:
        system("clear")
        print ("Mostrar direccion y telefono de las farmacias abiertas en la hora de introducida.")
        print ("-"*55)
        count=1
        print ("Debes introducir una hora con el formato HH:MM incluyendo el 0 delante de los numeros menores de 10.")
        cad=input("Introduce la hora> ")
        for x in EjercicioLibre2(farmacias,cad):
            print ("Farmacia %i".center(50, "=")%(count))
            print ("Direccion: %s." %(x.get("direccion")))
            print ("Telefono: %s." %(x.get("telefono")))
            count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 7:
        system("clear")
        break
    else:
        system("clear")
print ("Fin del programa")