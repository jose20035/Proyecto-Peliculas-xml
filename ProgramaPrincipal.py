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
        pais=input("Introduce el nombre de un pais:> ")
        print("Las peliculas rodadas en %s son:" % pais)
        for pelis in ListarPelis_por_pais(datos,pais):
            print(pelis)
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "4":
        director=input("Introduce el primer nombre de un director:> ")
        print("Las peliculas de %s son:" % director)
        for pelicula in ListarPeliculasyActores_por_Director(datos,director):
            print("Peli: %s" % pelicula.get("titulo")[0])
            print("En la que aparecen:")
            for i in pelicula.get("actores"):
                print(i)
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "5":
        añoini=input("Introduce el año de inicio a buscar directores:> ")
        añofin=input("Introduce el año de fin de la busqueda de directores:> ")
        print("Los direcotres que nacieron Entre %s y el %s son: " % (añoini,añofin))
        for directores in ListarDirecetoresyPeliculasEntreDosAños(datos,añoini,añofin):
            print("Director: %s" % directores.get("directores"))
            print("Que dirigio: ")
            for i in directores.get("pelis"):
                print(i)
        print("Pulsa enter para continuar")
        a=input()
        os.system("clear")
    elif opcion == "0":
        break