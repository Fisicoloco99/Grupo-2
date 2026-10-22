import sqlite3
conexion = sqlite3.connect("Calificaciones.db")
cursor = conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("""
CREATE TABLE IF NOT EXISTS calificaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calificacion INTEGER
)
""")
conexion.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    estudiante_id INTEGER,
    FOREIGN KEY (estudiante_id) REFERENCES calificaciones(id)
)
""")
def vaciar_y_crear_tablas():
    print('Ha escogido VACIAR Y CREAR NUEVA BASE')
    cursor.execute("DROP TABLE estudiantes")
    conexion.commit()
    cursor.execute("DROP TABLE calificaciones")
    conexion.commit()
    print("CREANDO NUEVA BASE DE DATOS")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calificaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        calificacion INTEGER)""")
    conexion.commit()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        estudiante_id INTEGER,
        FOREIGN KEY (estudiante_id) REFERENCES calificaciones(id))""")
    conexion.commit()
    print("BASE DE DATOS CREADOS!")
def añadir_califaciones_estudiantes():
    print("Ha seleccionado AÑADIR CALIFICIONES")
    print("Escriba los datos que desea insertar")
    calificacion = int(input("Escriba de forma numerica una calificacion"))
    cursor.execute("INSERT INTO calificaciones (calificacion) VALUES (?)",(calificacion,)    )
    id_estudiante = cursor.lastrowid
    nombre = input('Escriba el nombre del estudiante')
    estudiante_id = int(input("Escriba el ID del estudiante"))
    cursor.execute("INSERT INTO estudiantes (nombre, estudiante_id) VALUES (?, ?)",(nombre, estudiante_id,))
    print("Estudiante agregado")
    conexion.commit()
    cursor.execute("""
    SELECT estudiantes.nombre, calificaciones.calificacion
    FROM estudiantes
    INNER JOIN calificaciones
    ON estudiantes.estudiante_id = calificaciones.id
    """)
    for estudiante, calificacion in cursor.fetchall():
        print(f"Estudiantes: {estudiante} | Calificaciones: {calificacion}")
    conexion.close()
def mostrar_estudiante_calicaciones():
    print('Ha escogido MOSTRAR CALIFICACIONES')
    conexion_temp = sqlite3.connect("Calificaciones.db")
    cursor_temp = conexion_temp.cursor()
    cursor_temp.execute("SELECT * FROM estudiantes")
    estudiantes = cursor_temp.fetchall()
    conexion_temp.close()
    if not estudiantes:
        print("No hay estudiantes")
        return
    texto = "--- ESTUDIANTES ---\n"
    for i in estudiantes:
        texto += f"Nombre: {i[1]} | Id_Calificación: {i[2]}\n"
    print(texto)
def vaciar_archivos_estudiantes():
    print('Ha escogido VACIAR EXPEDIENTES DE ESTUDIANTES')
    cursor.execute("DROP TABLE estudiantes")
    conexion.commit()
    print("Todos los archivos de estudiantes fueron eliminados")
def menu():
    print("*"*30)
    print("MENU")
    print("0.VACIAR Y CREAR TABLAS")
    print("1.MOSTRAR ESTUDIANTE Y CALIFICACIONES")
    print("2.VACIAR ESTUDIANTES")
    print("3.AÑADIR NUEVO ESTUDIANTE")
    print("4.SALIR")
    print("*"*30)

while True:
    menu()
    op = int(input('Escriba la operacion mostrada en el menu'))
    if op == 0:
        vaciar_y_crear_tablas()
    elif op ==1:
        mostrar_estudiante_calicaciones()
    elif op ==2:
        vaciar_archivos_estudiantes()
    elif op ==3:
        añadir_califaciones_estudiantes()
    elif op ==4:
        print("Adios!")
        break
    else:
        print("Opcion incorrecta! Escriba alguna opcion invalida")