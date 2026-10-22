#C.R.U.D Vincular las sucursales a las tablas de empleados, se genera una tabla de tablas. La sucursal tiene su tabla mas la de empleados y ambas tienen funcionjes CRUD
import sqlite3
conexion=sqlite3.connect("Tabla_sucursales.db")
cursor=conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute(""" CREATE TABLE IF NOT EXISTS sucursales(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
direccion TEXT NOT NULL,
empleados_id INTEGER,
FOREIGN KEY (empleados_id) REFERENCES empleados (empleados_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
""")
conexion.commit()

class Sucursal:
    def __init__(self,nombre,direccion):
        self.nombre   = nombre
        self.direccion = direccion
    def mostrar_datos(self):
        return f"La sucursal es {self.nombre} ubicada en {self.direccion}. Contiene {self.asistencias_mensuales} empleados."

def mostrar_lista():
    cursor.execute("SELECT * FROM sucursales")
    sucursales= cursor.fetchall()
    if not sucursales:
        print("No hay sucursales")
        return
    texto = "--- sucursales ---\n"
    for sucursal in sucursales:
        # sucursal = (id, nombre, sucursal)
        texto += f"ID: {sucursal[0]} "+f" Nombre: {sucursal[1]} " +f" Direccion: {sucursal[2]} " + f" Numero de empleados: {sucursal[4]} "
        print(texto)

def agregar_nueva_sucursal(nombre,direccion):
    # Valido que no esten vacios
    if nombre == "" or direccion == "":
        print("Complete todos los campos")
        return
    direccion = int(direccion)
    sucursal = Sucursal(nombre,direccion)
    cursor.execute("INSERT INTO sucursales(nombre,direccion) VALUES (?,?)",(sucursal.nombre,sucursal.direccion))
    conexion.commit()
    print(f"Sucursal agregado: {sucursal.mostrar_datos()}")

def modificar_sucursal(nombre, direccion):
    if nombre == "" or direccion == "":
        print("Complete todos los campos")
        return
    cursor.execute("SELECT * FROM sucursales WHERE nombre = ? AND direccion = ?", (nombre, direccion))
    sucursal = cursor.fetchall()
    while True:
        print("Seleccione los datos a modificar (seleccione el dato usando un numero)")
        print("1. Nombre\n2. Direccion\n3. Numero de empleados\n0. Salir")
        select = input()
        if select == "0":
            break
        elif select == "1":
            nuevo_nombre = input("Nuevo dato: ")
            cursor.execute("UPDATE sucursales SET nombre = ? WHERE nombre = ? AND direccion = ?", (nuevo_nombre, nombre, direccion))
            conexion.commit()
            nombre = nuevo_nombre
            print("Sucursal modificada correctamente")
        elif select == "2":
            nueva_direccion = int(input("Nuevo dato: "))
            cursor.execute("UPDATE sucursales SET direccion = ? WHERE nombre = ? AND direccion = ?", (nueva_direccion, nombre, direccion))
            conexion.commit()
            print("Sucursal modificada correctamente")
        elif select == "3":
            nuevo_id = int(input("Nuevo dato: "))
            cursor.execute("UPDATE id SET dni = ? WHERE nombre = ? AND direccion = ?", (nuevo_id, nombre, id))
            conexion.commit()
            id = id
            print("Sucursal modificada correctamente")
        else:
            print("Error, intente devuelta")

def eliminar_sucursal(nombre,direccion):
    if nombre == "" or direccion == "":
        print("Campo vacio. Escriba un nombre y direccion de sucursal")
        return
    nombre = nombre
    direccion = direccion
    cursor.execute("SELECT * FROM sucursales WHERE nombre = ?, direccion = ?",(nombre,direccion))
    sucursal = cursor.fetchmany()

    if not sucursal:
        print("No hay registro para esa sucursal")
        return
    cursor.execute("DELETE FROM sucursales WHERE nombre = ?, direccion = ?",(nombre,direccion))
    conexion.commit()
    print("Sucursal eliminada correctamente")

#Prueba interna- Puede eliminarse luego
while True:
    print("MENU")
    print("1. Mostrar lista")
    print("2. Agregar")
    print("3. Modificar")
    print("4. Eliminar")
    print("0. Salir")
    op=input("Seleccione opcion\n")
    if op=="0":
        conexion.close()
        break
    elif op=="1":
        mostrar_lista()
    elif op=="2":
        print("Ingrese los datos de su sucursal")
        nombre=input("Nombre de la sucursal\n")
        direccion=int(input("Direccion\n"))
        agregar_nueva_sucursal(nombre,direccion)
    elif op=="3":
        print("Ingrese los datos de su sucursal")
        nombre=input("Nombre de la sucursal\n")
        direccion=input("Direccion\n")
        modificar_sucursal(nombre,direccion)
    elif op=="4":
        print("Ingrese los datos de su direccion")
        nombre=input("Nombre de la sucursal\n")
        direccion=input("Direccion\n")
        eliminar_sucursal(nombre,direccion)
    else:
        print("opcion invalida")