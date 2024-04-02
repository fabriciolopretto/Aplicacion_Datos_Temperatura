"""Este archivo constituye la VISTA de la aplicacion."""

# Se importan las librerias necesarias.
import tkinter as tk
from PIL import ImageTk, Image
from modelo import Crud
import os


class Menu():
    """Se muestra al usuario las referencias de los datos a ingresar."""

    def referencias(self):
        """
        Se abre una ventana con indicaciones para el usuario.
        
        :var root_m: Ventana interface con el usuario.
        :var tit_h: Indica al usuario el formato de hora.
        :var tit_t1-tit_4: Indican al usuario el formato de temperatura.
        :var tit_5: Indica al usuario como continuar.
        """
        root_m = tk.Tk()
        root_m.geometry("350x200")
        root_m.title("REFERENCIAS")
        tit_h = tk.Label(root_m,
                         text="1 - Hora [UTC]: Ingresar como Nº Natural.",
                         font=10)
        tit_h.place(x=10, y=10)
        tit_t1 = tk.Label(root_m,
                          text='2 - Temperatura [ºC]: Ingresar como Nº Real,',
                          font=10)
        tit_t1.place(x=10, y=50)
        tit_t2 = tk.Label(root_m,
                          text='pudiendo usar punto decimal con la',
                          font=10)
        tit_t2.place(x=30, y=80)
        tit_t3 = tk.Label(root_m,
                          text='cantidad de digitos que necesite,',
                          font=10)
        tit_t3.place(x=30, y=110)
        tit_t4 = tk.Label(root_m,
                          text='y con signo "-" si fuese el caso.',
                          font=10)
        tit_t4.place(x=30, y=110)
        tit_t5 = tk.Label(root_m,
                          text='Cerrar para Continuar.',
                          font=10)
        tit_t5.place(x=70, y=150)
        root_m.mainloop()


class Ventana():
    """Se declara la clase que contiene la interface con el usuario."""

    def interface(self, master):
        """
        Se definen los controles de la ventana.

        Generacion de rutas de imagenes, titulo y el tamaño de la ventana,
        como tambien la interface para la alta, baja consulta, modificacion
        y graficado de datos.

        :param master: Ventana de tkinter.

        :var ruta: Es la ruta de "vista.py".
        :var ruta_fondo: Es la ruta de "fondo.png".
        :var image1, image2, background: Cargan el fondo a la aplicacion.

        Alta de Registro: x=a
        Modificacion de Registro: x=m
        Baja de Registro: x=b
        Consulta de registro: x=c

        :var v_h_x: Se define el tipo de variable de la hora.
        :var v_t_x: Se define el tipo de variable de la temperatura.
        :var titulo_x: Se declara la etiqueta de titulo.
        :var hora_x: Se declara la etiqueta del campo hora.
        :var temperatura_x: Se declara la etiqueta del campo temperatura.
        :var entry_hora_x: Espacio para ingresar la hora.
        :var entry_temperatura_x: Espacio para ingresar la tempratura. 
        :var boton_x: Etiqueta de boton para ejecutar la la accion.
        """
        global ruta_fondo, image1, image2, background_label
        # Fijamos el tamano de la ventana
        master.geometry("750x600")
        # Se declara un título para la ventana de interface
        master.title("Temperatura horaria diaria Estación.")
        # Se asigna la ruta del fondo de la ventana de interface
        ruta = os.path.dirname((os.path.abspath(__file__)))
        ruta_fondo = os.path.join(ruta,
                                  "fondo.png")
        # Se incorpora el fondo de pantalla a la ventana grafica
        image2 = Image.open(ruta_fondo)
        print(image2)
        image1 = ImageTk.PhotoImage(image2)
        print(image1)
        background_label = tk.Label(master,
                                    image=image1)
        background_label.place(x=0,
                               y=0,
                               relwidth=1.0,
                               relheight=1.0)

        # Alta de Datos
        # Se definen las variables
        v_h_a = tk.StringVar()
        v_t_a = tk.StringVar()

        # Se aclaran los datos a ingresar
        titulo_a = tk.Label(master,
                            text="Ingresar dato horario (A)",
                            font=40)
        titulo_a.place(x=50,
                       y=30)

        hora_a = tk.Label(master,
                          text="Hora [HOA]")
        hora_a.place(x=40,
                     y=70)

        temperatura_a = tk.Label(master,
                                 text="Temperatura [ºC]")
        temperatura_a.place(x=40,
                            y=100)

        # Se agrega el espacio para ingresar los datos
        entry_hora_a = tk.Entry(master,
                                textvariable=v_h_a,
                                width=25)
        entry_hora_a.place(x=150,
                           y=70,
                           width=85,
                           height=25)

        entry_temperatura_a = tk.Entry(master,
                                       textvariable=v_t_a,
                                       width=25)
        entry_temperatura_a.place(x=150,
                                  y=100,
                                  width=85,
                                  height=25)

        # Se agregan los botones que disparan la funcion declarada
        boton_a = tk.Button(master,
                            text="Ingresar",
                            command=lambda: Crud().alta(master,
                                                        v_h_a.get(),
                                                        v_t_a.get()))
        boton_a.place(x=158,
                      y=130,
                      width=70,
                      height=30)

        # Modificacion de Datos
        # Se definen las variables
        v_h_m = tk.StringVar()
        v_t_m = tk.StringVar()

        # Se aclaran los datos a ingresar
        titulo_m = tk.Label(master,
                            text="Modificar dato horario (M)",
                            font=40)
        titulo_m.place(x=315,
                       y=30)

        hora_m = tk.Label(master,
                          text="Hora [HOA]")
        hora_m.place(x=305,
                     y=70)

        temperatura_m = tk.Label(master,
                                 text="Temperatura [ºC]")
        temperatura_m.place(x=305,
                            y=100)

        # Se agrega el espacio para ingresar los datos
        entry_hora_m = tk.Entry(master,
                                textvariable=v_h_m,
                                width=25)
        entry_hora_m.place(x=420, y=70, width=85, height=25)

        entry_temperatura_m = tk.Entry(master,
                                       textvariable=v_t_m,
                                       width=25)
        entry_temperatura_m.place(x=420,
                                  y=100,
                                  width=85,
                                  height=25)

        # Se agregan los botones que disparan la funcion declarada
        boton_m = tk.Button(master,
                            text="Modificar",
                            command=lambda: Crud().modificacion(master,
                                                                v_h_m.get(),
                                                                v_t_m.get()))
        boton_m.place(x=428,
                      y=130,
                      width=70,
                      height=30)

        # Eliminacion de Datos
        # Se definen las variables
        v_h_b = tk.StringVar()

        # Se aclaran los datos a ingresar
        titulo_b = tk.Label(master,
                            text="Eliminar dato horario (B)",
                            font=40)
        titulo_b.place(x=50, y=195)

        hora_b = tk.Label(master, text="Hora [HOA]")
        hora_b.place(x=40,
                     y=230)

        # Se agrega el espacio para ingresar los datos
        entry_hora_b = tk.Entry(master,
                                textvariable=v_h_b,
                                width=25)
        entry_hora_b.place(x=150,
                           y=230,
                           width=85,
                           height=25)

        # Se agregan los botones que disparan la funcion declarada
        boton_b = tk.Button(master,
                            text="Eliminar",
                            command=lambda: Crud().baja(master,
                                                        v_h_b.get()))
        boton_b.place(x=158,
                      y=260,
                      width=70,
                      height=30)

        # Consulta de Datos
        # Se definen las variables
        v_h_c = tk.StringVar()

        # Se aclaran los datos a ingresar
        titulo_c = tk.Label(master,
                            text="Consultar dato horario (C)",
                            font=40)
        titulo_c.place(x=315,
                       y=195)

        hora_c = tk.Label(master,
                          text="Hora [HOA]")
        hora_c.place(x=305,
                     y=230)

        # Se agrega el espacio para ingresar los datos
        entry_hora_c = tk.Entry(master,
                                textvariable=v_h_c,
                                width=25)
        entry_hora_c.place(x=420,
                           y=230,
                           width=85,
                           height=25)

        # Se agregan los botones que disparan la funcion declarada
        boton_c = tk.Button(master,
                            text="Consultar",
                            command=lambda: Crud().consulta(master,
                                                            v_h_c.get()))
        boton_c.place(x=428,
                      y=260,
                      width=70,
                      height=30)

        # Graficado de Datos
        # Se aclaran los datos a ingresar
        titulo_g = tk.Label(master,
                            text="Marcha de Temperatura horaria Estación.",
                            font=40)
        titulo_g.place(x=45,
                       y=325)

        # Se agregan los botones que disparan la funcion declarada
        boton_g = tk.Button(master,
                            text="Graficar",
                            command=lambda: Crud().graficado(master))
        boton_g.place(x=440,
                      y=325,
                      width=70,
                      height=30)
