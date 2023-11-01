# Data Loading and Manipulation

This code is designed for loading, filtering, and managing data from CSV files using Python. It consists of two classes, `CargaDatos` and `ListaDatos`, that allow you to load and work with data.

## CargaDatos Class

The `CargaDatos` class is responsible for loading and filtering data from a CSV file. It has the following methods:

### 1. `__init__(self, CargaDatos, NombreDatos)`

- Constructor that takes the name of the CSV file and a name for the data being loaded.
- Loads the data from the CSV file into a pandas DataFrame.

### 2. `printDatos(self)`

- Prints the loaded data as a pandas DataFrame.

### 3. `printNombre(self)`

- Prints the name of the data being loaded.

### 4. `filtrar_Datos(self, atributo, valor)`

- Filters the data based on a specified attribute and value and prints the filtered results.

## ListaDatos Class

The `ListaDatos` class is designed to manage a list of data instances created with the `CargaDatos` class. It is a Singleton class, meaning only one instance can exist. It has the following methods:

### 1. `agregar_Dato(self, dato)`

- Adds a data instance to the list.

### 2. `eliminar_Dato(self, indice)`

- Removes a data instance at a specified index in the list.

### 3. `insertar_Dato(self, dato, indice)`

- Inserts a data instance at a specified index in the list.

### 4. `imprimir_Dato(lista)`

- Recursively prints the name and data of each instance in the list.

## Usage

To use this code:

- Create instances of the `CargaDatos` class to load and manipulate data from CSV files.
- Create a list of data instances using the `ListaDatos` class.
- Add, remove, or insert data instances into the list as needed.
- Use the `imprimir_Dato` method to print the name and data of each data instance in the list.

You can customize this code to work with your specific data and CSV files.

## Author

Alejandro Vargas

## Acknowledgments

This code demonstrates how to load and manipulate data from CSV files using pandas and provides a simple structure for managing data instances. You can expand and modify it for your data analysis needs.
