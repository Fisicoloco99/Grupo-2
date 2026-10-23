import sqlite3
import tkinter as tk
from tkinter import Label, Button,Entry, Canvas, Frame,Toplevel
# Aca se crea la conexion
conexion=sqlite3.connect("Tabla_sucursales.db")
cursor=conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute(""" CREATE TABLE IF NOT EXISTS sucursales(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
direccion TEXT NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS empleados(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, año_inicio INTEGER,asistencia INTEGER , dni INTEGER,sucursal_id INTEGER, FOREIGN KEY (sucursal_id) REFERENCES sucursales(id))""")
conexion.commit()
class Sucursal:
    def __init__(self,id_sucursal,nombre,direccion):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.direccion = direccion
    def mostrar_datos(self):
            return f"La sucursal es {self.nombre} ubicada en {self.direccion} y su ID es: {self.id_sucursal}."
    def ver_empleados(self):
        cursor.execute("SELECT nombres FROM empleados WHERE sucursal_id = ?",(self.id_sucursal))
        empleados = cursor.fetchall()
        if not empleados:   
            return 'No hay empleados'
        else:
            texto = f"Empleados en {self.nombre}:\n"
            for empleado in empleados:
                texto +=f"- {empleado[0]}\n"
            return texto
# ======================================= FUNCIONES PARA CADA VENTANA ==========================================================================
# 1.Voy a crear una funcion para que funcione. Esta abre la ventana secundaria con los menus.
def abrir_ventana_sucursales():  # No le paso variables, solo la dejo asi
    # 2.Crear ventana secundaria (hija de la ventana principal)
    ventana_sucursales = Toplevel(ventana)  # aca estaria haciendo que haya una ventana nueva o hija
    ventana_sucursales.title('Gestor de sucursales')  # titulo para la ventana
    ventana_sucursales.geometry('500x500')  # geometria de la ventana, un poco mas grande para que entre todo
    ventana_sucursales.config() # aca seria para "decorar" la vemtana
    # 3.Mensaje para el usuario con la instruccion para que escriba
    Label(ventana_sucursales, text='Ingrese el ID de la sucursal para modificar los datos que desea:').grid()
    # 4.Entry para los datos de las sucursales, nombre, id, direccion
    Label(ventana_sucursales,text="Escriba el ID de la sucursal").grid()
    id_sucursal = Entry(ventana_sucursales)
    id_sucursal.grid()
    Label(ventana_sucursales,text="Escriba el nombre de la sucursal").grid()
    nombre_sucursal = Entry(ventana_sucursales)
    nombre_sucursal.grid()
    Label(ventana_sucursales,text="Escriba la direccion de la sucursal").grid()
    direccion_sucursal = Entry(ventana_sucursales)
    direccion_sucursal.grid()
    # Aca la parte fea y medio dificil , las funciones internas

    def agregar_nueva_sucursal():
        nombre = nombre_sucursal.get()
        direccion = direccion_sucursal.get()
        # Valido que no esten vacios
        if nombre == "" or direccion == "":
            mensaje.config("Complete todos los campos")
            return
        #aca deberia poner eñ nuevo objeto
        nueva_sucursal = Sucursal(None,nombre,direccion)
        cursor.execute("INSERT INTO sucursales(nombre,direccion) VALUES (?,?)",(nueva_sucursal.nombre,nueva_sucursal.direccion))
        conexion.commit()
        mensaje.config(text=f"Sucursal '{nueva_sucursal.nombre}' agregada.", fg="green")
        nombre_sucursal.delete(0, tk.END) # limpia
        direccion_sucursal.delete(0, tk.END) #limpia 
    def eliminar_todas_las_sucursales():
        cursor.execute("DROP TABLE IF EXISTS sucursales")
        conexion.commit()
        mensaje.config(ventana_sucursales,text="Sucursales correctamente eliminadas")
    def crear_nueva_base_de_datos_sucursales():
        cursor.execute(""" CREATE TABLE IF NOT EXISTS sucursales(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,direccion TEXT NOT NULL)""")
        conexion.commit()
        mensaje.config(ventana_sucursales,text="Nueva base de datos de sucursales creada")
    # 5.Boton para la ventana sucursales
    boton_datos = Button(ventana_sucursales,text="Mostrar sucursal",command=Sucursal.mostrar_datos)
    boton_datos.grid()
    boton_nueva_sucursal= Button(ventana_sucursales,text="Modificar sucursal")
    boton_nueva_sucursal.grid()
    boton_eliminar_sucursal = Button(ventana_sucursales,text="Eliminar sucursal")
    boton_eliminar_sucursal.grid()
    boton_cerrar = Button(ventana_sucursales, text='Cerrar', command=ventana_sucursales.destroy)
    boton_cerrar.grid()
    btn_base_de_datos_nueva = Button(ventana_sucursales,text="Crear base de datos nueva",command= crear_nueva_base_de_datos_sucursales)
    btn_base_de_datos_nueva.grid()
    btn_vaciar = Button(ventana_sucursales,text="Vaciar base de datos", command= eliminar_todas_las_sucursales)
    btn_vaciar.grid()
    btn_añadir = Button(ventana_sucursales,text ="Añadir sucursales",command=agregar_nueva_sucursal)
    btn_añadir.grid()
def abrir_ventana_empleados():
    #1.Crear una ventana para empleados
    ventana_empleados = tk.Toplevel(ventana)
    ventana_empleados.title('Gestor de empleados')  # titulo para la ventana
    ventana_empleados.geometry('500x500')  # geometria de la ventana, un poco mas grande para que entre todo
    ventana_empleados.config()
    #2.Creo las entradas para el gestor de empleados
    Label(ventana_empleados,text="Escriba el ID del empleado").grid()
    empleado_id = tk.Entry(ventana_empleados)
    empleado_id.grid()
    Label(ventana_empleados,text="Escriba el nombre del empleado").grid()
    empleado_nombre = tk.Entry(ventana_empleados)
    empleado_nombre.grid()   
    Label(ventana_empleados,text="Escriba el DNI del empleado").grid()
    empleado_DNI = tk.Entry(ventana_empleados)
    empleado_DNI.grid()    
    Label(ventana_empleados,text="Escriba los dias trabajados del empleado").grid()
    empleado_dias_trabajados= tk.Entry(ventana_empleados)
    empleado_dias_trabajados.grid()   
# ===========================================================
# VENTANA PRINCIPAL
# ============================================================
ventana = tk.Tk()
ventana.title("Gestor de sucursales y empleados ROCK STAR")
ventana.geometry("500x400")
mensaje = Label(ventana, text="Gestor de sucursales y empleados", font=("Arial", 16))
mensaje.grid()

#Boton para Ventana principal
btn_metros = Button(ventana, text="SUCURSALES", command=abrir_ventana_sucursales)
btn_metros.grid()
#Boton para Empleados 
btn_tiempo = Button(ventana,text='EMPLEADOS', command=abrir_ventana_empleados)
btn_tiempo.grid()
btn_cerrar = Button(ventana,text="CERRAR",command=ventana.destroy)
btn_cerrar.grid()

# Iniciar el bucle principal
ventana.mainloop()
