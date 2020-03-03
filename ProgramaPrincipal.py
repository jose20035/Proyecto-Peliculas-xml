import os
from lxml import etree
from Funciones import *

ndatos=input("Introduce la el nombre del documento xml:> ")
os.system("clear")

datos=etree.parse(ndatos)
while True:
    print("Bienvenido.")
    print()
    print("1. Lista el nombre de las peliculas, el año y el genero.")
    print("2. Contar peluculas entre dos años.")
    print("3. Lispar peliculas de rodadas en un pais.")
    print("4. Peliculas y actores que realizan dicha pelicula de un direcotor en concreto.")
    print("5. Nombre de directores y peliculas entre dos años.")
    print("0. Salir")
    print()
    opcion=input(":> ")
    while opcion not in ("0","1","2","3","4","5"):
        print("Error opción no correcta.")
        opcion=input(":> ")
    if opcion == "1":
        print("Peliculas:")
        print("--------------------------")
        for peliculas in ListarPelis(datos):
            print("Titulo: %s año: %s genero: %s" % (peliculas.get("titulo"),peliculas.get("año")[0],peliculas.get("genero")[0]))
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "2":
        añoini=input("Introduce el año de inicio de la busqueda:> ")
        añofin=input("Introduce el año de fin de la busqueda:> ")
        print("Se han realizado %s peliculas" % NPeliculas_por_año(datos,añoini,añofin))
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "3":
        
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "4":
        carretera=input("Introduce una carretera que quieras mostrar las provincias por las que pasa: ")
        print("Las provincias en las que pasas la carretera son:")
        for i in buscar_radare_carreteras(doc,carretera).get("Provincias"):
            print(i, end=" ")
        print()
        print("El numero de radares que tiene hay son: %s" % buscar_radare_carreteras(doc,carretera).get("nºradar"))
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "5":
        carretera=input("Introduce una carretera que quieras mostrar la ubicación de sus radares: ")
        print("La ubicación de los radares son las siguientes:")
        for url in codenada_radar_carretera(doc,carretera).get("url"):
            print(url)
        print("El numero de radares que tiene hay son: %s" % codenada_radar_carretera(doc,carretera).get("nºradar"))
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "0":
        break