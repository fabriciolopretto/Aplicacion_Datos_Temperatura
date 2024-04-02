"""Este archivo constituye el MODELO de la aplicacion."""

# Se importan las librerias necesarias.
import matplotlib.pyplot as plt
import os
import re
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import glob
from peewee import SqliteDatabase, Model, IntegerField, FloatField
from datetime import datetime


"""
Se indican variables globales.

:var ruta: Indica la ruta de "modelo.py".
:var ruta_marcha: Indica la ruta de "marcha.png".
:var ruta_base: Indica la ruta de "mibase.db".
:var ruta_log: Umdica la ruta de "log.txt".
:var hora_r: Indica la fecha y hora actual.
:var db: Apunta a la Base de Datos.

Describe las rutas del grafico, de la base de datos y registro de errores.
"""
global ruta, ruta_marcha, ruta_base, ruta_log, hora_r, db
ruta = os.path.dirname((os.path.abspath(__file__)))
ruta_marcha = os.path.join(ruta,
                        "marcha.png")
ruta_base = os.path.join(ruta,
                        "mibase.db")
ruta_log = os.path.join(ruta,
                        "log.txt")
hora_r = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
db = SqliteDatabase(ruta_base)


class BaseModel(Model):
    """Se crea la Base de Datos."""

    class Meta:
        """
        Se realiza la asignacion de la Base de Datos.
        
        :var database: Orientada a la Base de Datos.
        """
        database = db


class Database(BaseModel):
    """
    Se genera la tabla con sus campos y restricciones.
    
    :var hora: Guarda la hora en el campo homonimo de la tabla.
    :var temperatura: Guarda la temperatura en el campo homonimo de la tabla.
    """

    hora = IntegerField(unique=True)
    temperatura = FloatField()


def conexion():
    """
    Se verifica en el directorio si la base ya está creada o si hay que crearla.

    :var files: busca en el directorio archivos con terminacion ".db".

    Se conecta/crea la base de datos y la tabla.
    """
    files = glob.glob(ruta + '/*.db')
    if files == []:
        db.connect()
        db.create_tables([Database])
    else:
        db.connect()


class Crud():
    """
    Se realiza la clase y metodos que se utilizan desde Vista.

    Se definen los metodos de alta, modificacion,
    baja y consulta de registro. Además del graficado de los datos.
    """

    def alta(self, master, hora, temperatura):
        """
        Se ingresa con los datos de hora y temperatura.
        
        :param master: Ventana de tkinter.
        :param hora: Numero Natural que indica el horario en hora UTC.
        :param temperatura: Numero Real que indica la tempratura de la hora.

        Luego se verifica el formato,
        se asigna al registro correspondiente,
        y se acusa recibo por pantalla.

        Si el formato no es correcto se informa al usuario por pantalla.
        Si se detecta un error, se toma nota del mismo en un archivo de texto.
        """
        try:
            cadena_h = hora
            cadena_t = temperatura
            # Se define regex numerico,signo "-" y punto decimal "."
            patron = "^[0-9 \. \-]*$"
            if(re.match(patron, cadena_h) and re.match(patron, cadena_t)):
                noti_exi = tk.Label(master,
                                    text="")
                dato = Database()
                dato.hora = int(hora)
                dato.temperatura = float(temperatura)
                dato.save()
                noti_exi = tk.Label(master,
                                    text="Alta "+str(hora)+" HOA: con exito.")
                noti_exi.place(x=20,
                               y=570)
            else:
                print("Error en campo\s hora y\o temperatura")
        except:
            with open(ruta_log, "a") as file:
                file.write(hora_r+". Existe valor de "+str(hora)+" UTC.\n")

    def modificacion(self, master, hora, temperatura):
        """
        Se ingresa con los datos de hora y temperatura.

        :param master: Ventana de tkinter.
        :param hora: Numero Natural que indica el horario en hora UTC.
        :param temperatura: Numero Real que indica la tempratura de la hora.

        Luego se verifica el formato,
        se asigna al registro correspondiente,
        y se acusa recibo por pantalla.

        Si el formato no es correcto se informa al usuario por pantalla.
        Si se detecta un error, se toma nota del mismo en un archivo de texto.
        """
        try:
            cadena_h = hora
            cadena_t = temperatura
            # Se define regex numerico,signo "-" y punto decimal "."
            patron = "^[0-9 \. \-]*$"
            if(re.match(patron, cadena_h) and re.match(patron, cadena_t)):
                noti_exi = tk.Label(master,
                                    text="")
                h = int(hora)
                t = float(temperatura)
                act = Database.update(hora=h,
                                      temperatura=t).where(Database.hora == h)
                act.execute()
                noti_exi = tk.Label(master,
                                    text="Mod. "+str(hora)+" HOA: con exito.")
                noti_exi.place(x=20,
                               y=570)
            else:
                print("Error en campo\s hora y\o temperatura")
        except:
            with open(ruta_log, "a") as file:
                file.write(hora_r+". No existe valor de "+str(hora)+" UTC.\n")

    def baja(self, master, hora):
        """
        Se ingresa con el dato de hora.

        :param master: Ventana de tkinter.
        :param hora: Numero Natural que indica el horario en hora UTC.

        Luego se verifica el formato,
        se asigna al registro correspondiente,
        y se acusa recibo por pantalla.

        Si el formato no es correcto se informa al usuario por pantalla.
        Si se detecta un error, se toma nota del mismo en un archivo de texto.
        """
        try:
            cadena_h = hora
            # Se define regex numerico
            patron = "^[0-9]*$"
            if(re.match(patron, cadena_h)):
                noti_exi = tk.Label(master,
                                    text="")
                hora = int(hora)
                borrar = Database.get(Database.hora == hora)
                borrar.delete_instance()
                noti_exi = tk.Label(master,
                                    text="Baja "+str(hora)+" HOA: con exito.")
                noti_exi.place(x=20,
                               y=570)
            else:
                print("Error en campo de hora")
        except:
            with open(ruta_log, "a") as file:
                file.write(hora_r+". No existe valor de "+str(hora)+" UTC.\n")

    def consulta(self, master, hora):
        """
        Se ingresa con el dato de hora.

        :param master: Ventana de tkinter.
        :param hora: Numero Natural que indica el horario en hora UTC.

        Luego se verifica el formato,
        se asigna al registro correspondiente,
        y se acusa recibo por pantalla.

        Si el formato no es correcto se informa al usuario por pantalla.
        Si se detecta un error, se toma nota del mismo en un archivo de texto.
        """
        try:
            cadena_h = hora
            # Se define regex numerico
            patron = "^[0-9]*$"
            if(re.match(patron, cadena_h)):
                noti_exi = tk.Label(master,
                                    text="")
                hora = int(hora)
                consulta = Database.get(Database.hora == hora)
                texto1 = "La temperatura de las "
                texto2 = " HOA es: "
                texto3 = str(consulta.temperatura)
                texto4 = " ºC."
                texto = texto1+str(hora)+texto2+texto3+texto4
                noti_cons = tk.Label(master,
                                     text=texto)
                noti_cons.place(x=360,
                                y=570)
                noti_exi = tk.Label(master,
                                    text="Con. "+str(hora)+" HOA: con exito.")
                noti_exi.place(x=20,
                               y=570)
            else:
                print("Error en campo de hora")
        except:
            with open(ruta_log, "a") as file:
                file.write(hora_r+". No existe valor de "+str(hora)+" UTC.\n")

    def graficado(self, master):
        """
        Genera (o toma si se encuentra generado) el archivo marcha.png.

        :param master: Ventana de tkinter.

        Si el archivo se genero o no existe el archivo,
        se toma nota del error y se registra en un archivo de texto.
        """
        try:
            global ruta_marcha, image3, image4, marcha_label
            x = list(range(24))
            y = [np.nan]*24
            registros = Database.select()
            # Se vuelcan los valores de temperatura en la lista "y"
            for registro in registros:
                hora = registro.hora
                y[hora] = registro.temperatura
            fig, ax = plt.subplots(1,
                                   1,
                                   figsize=(5.4,
                                            1.5))
            plt.plot(x, y)
            ax.set_xlim(0,
                        23)
            ax.set_ylim(min(y)-2,
                        max(y)+2)
            ax.set_xlabel('Tiempo [horas (HOA)]')
            ax.set_ylabel('Temperatura [ºC]')
            plt.savefig(ruta_marcha,
                        dpi=100,
                        bbox_inches='tight')
            # Se incorpora el grafico en la ventana grafica
            image4 = Image.open(ruta_marcha)
            print(image4)
            image3 = ImageTk.PhotoImage(image4)
            print(image3)
            marcha_label = tk.Label(master, image=image3)
            marcha_label.place(x=38,
                               y=365,
                               relwidth=0.65,
                               relheight=0.30)
            return image3, image4, marcha_label
        except:
            with open(ruta_log, "a") as file:
                file.write(hora_r+'. No existe archivo "marcha.png".\n')
