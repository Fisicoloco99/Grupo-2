#C.R.U.D Vincular las sucursales a las tablas de empleados, se genera una tabla de tablas. La sucursal tiene su tabla mas la de empleados y ambas tienen funcionjes CRUD
import sqlite3
conexion=sqlite3.connect("Tabla_sucursales.db")
cursor=conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute(""" CREATE TABLE IF NOT EXISTS sucursales(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
direccion TEXT NOT NULL
)
""")
conexion.commit()

class Sucursal:
    def __init__(self,nombre,direccion):
        self.nombre   = nombre
        self.direccion = direccion
    def mostrar_datos(self):
        return f"La sucursal es {self.nombre} ubicada en {self.direccion}."

def mostrar_lista():
    cursor.execute("SELECT * FROM sucursales")
    sucursales= cursor.fetchall()
    if not sucursales:
        print("No hay sucursales")
        return
    texto = "--- sucursales ---\n"
    for sucursal in sucursales:
        # sucursal = (id, nombre, sucursal)
        texto += f"ID: {sucursal[0]} "+f" Nombre: {sucursal[1]} " +f" Direccion: {sucursal[2]} "
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

def modificar_sucursal(id_sucursal):
    cursor.execute("SELECT * FROM sucursales WHERE id = ?", (id_sucursal,))
    sucursal = cursor.fetchone()
    if not sucursal:
        print("No se encontró ninguna sucursal con ese ID.")
        return
    while True:
        print("Seleccione los datos a modificar (seleccione el dato usando un numero)")
        print("1. Nombre\n2. Direccion\n0. Salir")
        select = input()
        if select == "0":
            break
        elif select == "1":
            nuevo_nombre = input("Nuevo dato: ")
            cursor.execute("UPDATE sucursales SET nombre = ? WHERE id = ?", (nuevo_nombre, id_sucursal))
            conexion.commit()
            nombre = nuevo_nombre
            print("Sucursal modificada correctamente")
        elif select == "2":
            nueva_direccion = int(input("Nuevo dato: "))
            cursor.execute("UPDATE sucursales SET direccion = ? WHERE id = ?", (nueva_direccion, id_sucursal))
            conexion.commit()
            print("Sucursal modificada correctamente")
        else:
            print("Error, intente devuelta")

def eliminar_sucursal(id_sucursal):
    cursor.execute("SELECT * FROM sucursales WHERE id = ?", (id_sucursal,))
    if not cursor.fetchone():
        print("No hay registro para esa sucursal")
        return
    cursor.execute("DELETE FROM sucursales WHERE id = ?", (id_sucursal,))
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
        mostrar_lista()
        id_modificado = input("Ingrese el ID de la sucursal a modificar: ")
        if id_modificado.isdigit():
            modificar_sucursal(int(id_modificado))
        else:
            print("ID invalido")
    elif op=="4":
        mostrar_lista()
        id_eliminado = input("Ingrese el ID de la sucursal a eliminar: ")
        if id_eliminado.isdigit():
            eliminar_sucursal(int(id_eliminado))
        else:
            print("ID invalido")
    else:
        print("opcion invalida")