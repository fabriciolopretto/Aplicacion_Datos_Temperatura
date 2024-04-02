"""
Este archivo es el CONTROLADOR de la aplicacion.

Se importan funciones y clases desde "modelo.py" y "vista.py".
Se ejecutan en orden funciones de estos modulos y objetos
de diferentes clases.
"""

# Se importan las librerias necesarias.
import tkinter as tk
from vista import Menu, Ventana
from modelo import conexion

# Se declaran los objetos.
if __name__ == "__main__":
    conexion()
    des = Menu().referencias()
    root_tk = tk.Tk()
    app = Ventana().interface(root_tk)
    root_tk.mainloop()
