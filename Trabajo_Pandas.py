# Clase:
# Atributo con nombre del dato que se está cargando
# Contruir
# 1er método: Mostrar listado
# 2do método: Mostrar filtrado
# 3er método: Debe mostrar el nombre
# Clase 2:
#Lista = arreglo
# -Datos insidentes 2014 hasta 2021
# Cargar lista creada (debe estar vacía)
# 1er método: Agregar un elemento secuencial
# 2do método: Agregar un elemento al inicio
# 3er método: Agregar un elemento en un posición ubicada
# 4to método: Recorrer la lista (con recursión)
# 5to método: Eliminar un elemento en una posición
import pandas as pd

class CargaDatos:
    NombreDatos = str

    def __init__(self, CargaDatos, NombreDatos):
        self.NombreDatos = NombreDatos
        self.df = pd.read_csv(CargaDatos, sep=",")

    def printDatos(self):
        print(self.df)

    def printNombre(self):
        print(self.NombreDatos)

    def filtrar_Datos(self, atributo, valor):
        print(self.df[self.df[atributo] == valor])


dato = CargaDatos("Accidentalidad_Barbosa_Antioquia_2019-2020-2021.csv", "Datos")
dato.printDatos()
dato.printNombre()

dato.filtrar_Datos("CLASE", "Atropello")


class ListaDatos:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not ListaDatos.__instance:
            ListaDatos.__instance = object.__new__(cls)
            return ListaDatos.__instance
        pass

    def __init__(self, lista):
        self.lista = lista

    def agregar_Dato(self, dato):
        self.lista.append(dato)

    def eliminar_Dato(self, indice):
        self.lista.pop(indice)

    def insertar_Dato(self, dato, indice):
        self.lista.insert(indice, dato)

    @staticmethod
    def imprimir_Dato(lista):

        elemento = lista.pop(0)
        elemento.printNombre()
        elemento.printDatos()

        if len(lista) != 0:
            ListaDatos.imprimir_Dato(lista)


dato2 = CargaDatos("Accidentalidad_Barbosa_Antioquia_2019-2020-2021.csv", "Dato 2")
dato3 = CargaDatos("Accidentalidad_Barbosa_Antioquia_2019-2020-2021.csv", "Dato 3")

Listado = ListaDatos([])
Listado.agregar_Dato(dato)
Listado.agregar_Dato(dato2)
Listado.agregar_Dato(dato3)
# ListaDatos.imprimir_Dato(Listado.Lista)
