#como tabla con todo botones, y su funcion (Crud)
#nombres de empleados, años trabajando, dni, y asistencias mensuales. bonificaciones, y asistencias justificadas y ambas estan relacionadas.

import tkinter as tk
from tkinter import ttk

SUELDO_BASE = 500000

AZUL_PETROLEO = "#006080"
BLANCO_HUESO = "#F5F5DC"
VERDE_AZULADO = "#008080"
VERDE_TERMINAL = "#00FF00"

def calcular_bonificacion(asistencias, justificadas):
    try:
        asist_totales = int(asistencias) + int(justificadas)
        if asist_totales >= 24:
            return f"${int(SUELDO_BASE * 0.10)}"
        return "$0"
    except ValueError:
        return "$0"

def agregar_empleado():
    nombre = entrada_nombre.get().strip()
    anios = entrada_anios.get().strip()
    dni = entrada_dni.get().strip()
    asistencias = entrada_asistencias.get().strip()
    justificadas = entrada_justificadas.get().strip()
    
    if nombre and anios and dni and asistencias and justificadas:
        bono = calcular_bonificacion(asistencias, justificadas)
        

        registro = (f"Nombre: {nombre} | Años: {anios} | DNI: {dni} | "
                    f"Asist: {asistencias} | Justif: {justificadas} | Bono: {bono}")
        
        lista_empleados.insert(tk.END, registro)
        limpiar_formulario()


def eliminar_empleado():
    try:
        indice_seleccionado = lista_empleados.curselection()[0]
        lista_empleados.delete(indice_seleccionado)
    except IndexError:
        pass


def cargar_empleado_a_editar():
    global indice_edicion
    try:
       
        indice_edicion = lista_empleados.curselection()[0]
        texto_registro = lista_empleados.get(indice_edicion)
        
     
        limpiar_formulario()
        
       
        partes = [p.split(": ")[1] for p in texto_registro.split(" | ")]
        
       
        entrada_nombre.insert(0, partes[0])
        entrada_anios.insert(0, partes[1])
        entrada_dni.insert(0, partes[2])
        entrada_asistencias.insert(0, partes[3])
        entrada_justificadas.insert(0, partes[4])
    except IndexError:
        pass 


def guardar_edicion():
    global indice_edicion
    if indice_edicion is not None:
        nombre = entrada_nombre.get().strip()
        anios = entrada_anios.get().strip()
        dni = entrada_dni.get().strip()
        asistencias = entrada_asistencias.get().strip()
        justificadas = entrada_justificadas.get().strip()
        
        if nombre and anios and dni and asistencias and justificadas:
            bono = calcular_bonificacion(asistencias, justificadas)
            
            registro_actualizado = (f"Nombre: {nombre} | Años: {anios} | DNI: {dni} | "
                                    f"Asist: {asistencias} | Justif: {justificadas} | Bono: {bono}")
            

            lista_empleados.delete(indice_edicion)
            lista_empleados.insert(indice_edicion, registro_actualizado)
            
            indice_edicion = None
            limpiar_formulario()


def limpiar_formulario():
    entrada_nombre.delete(0, tk.END)
    entrada_anios.delete(0, tk.END)
    entrada_dni.delete(0, tk.END)
    entrada_asistencias.delete(0, tk.END)
    entrada_justificadas.delete(0, tk.END)



indice_edicion = None


ventana = tk.Tk()
ventana.title("Empleados data")
ventana.geometry("920x880") 
ventana.configure(bg=VERDE_AZULADO)


encabezado = tk.Frame(ventana, height=105, bg=AZUL_PETROLEO)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)

tk.Label(
    encabezado,
    text="base de datos",
    font=("Consolas", 25, "bold"),
    bg=AZUL_PETROLEO,
    fg="black",
).pack(anchor="center", pady=(28, 0))

marco_titulo = tk.Frame(ventana, bg=BLANCO_HUESO, height=20)
marco_titulo.pack(fill="x", side="top")

estilo = ttk.Style()
estilo.theme_use("clam")


marco_lista = tk.Frame(ventana, bg=AZUL_PETROLEO)
marco_lista.pack(pady=20, fill="both", expand=True, padx=50)

scrollbar = tk.Scrollbar(marco_lista, orient="vertical")
scrollbar.pack(side="right", fill="y")

lista_empleados = tk.Listbox(
    marco_lista, 
    font=("Consolas", 10), 
    bg="#1a1a1a", 
    fg="white", 
    selectbackground="#fffefe", 
    selectforeground="black",
    yscrollcommand=scrollbar.set
)
lista_empleados.pack(side="left", fill="both", expand=True)
scrollbar.config(command=lista_empleados.yview)




tk.Label(ventana, text="Nombre del Empleado:", font=("Consolas", 11, "bold"), bg=VERDE_AZULADO, fg="white").pack(pady=(5, 0))
entrada_nombre = tk.Entry(ventana, font=("Consolas", 11), width=45)
entrada_nombre.pack(pady=3)

tk.Label(ventana, text="Años Trabajando:", font=("Consolas", 11, "bold"), bg=VERDE_AZULADO, fg="white").pack(pady=(5, 0))
entrada_anios = tk.Entry(ventana, font=("Consolas", 11), width=45)
entrada_anios.pack(pady=3)

tk.Label(ventana, text="DNI:", font=("Consolas", 11, "bold"), bg=VERDE_AZULADO, fg="white").pack(pady=(5, 0))
entrada_dni = tk.Entry(ventana, font=("Consolas", 11), width=45)
entrada_dni.pack(pady=3)

tk.Label(ventana, text="Asistencias Mensuales:", font=("Consolas", 11, "bold"), bg=VERDE_AZULADO, fg="white").pack(pady=(5, 0))
entrada_asistencias = tk.Entry(ventana, font=("Consolas", 11), width=45)
entrada_asistencias.pack(pady=3)

tk.Label(ventana, text="Asistencias Justificadas (Faltas con Justificativo):", font=("Consolas", 11, "bold"), bg=VERDE_AZULADO, fg="white").pack(pady=(5, 0))
entrada_justificadas = tk.Entry(ventana, font=("Consolas", 11), width=45)
entrada_justificadas.pack(pady=3)


marco_botones = tk.Frame(ventana, bg=VERDE_AZULADO)
marco_botones.pack(pady=15)

boton_crear = tk.Button(
    marco_botones, text="Contratar empleado", font=("Consolas", 11, "bold"),
    bg="#000000", fg="white", command=agregar_empleado, padx=8, pady=4
)
boton_crear.pack(side="left", padx=5)


boton_cargar = tk.Button(
    marco_botones, text="Seleccionar para editar", font=("Consolas", 11, "bold"),
    bg="#000000", fg="white", command=cargar_empleado_a_editar, padx=8, pady=4
)
boton_cargar.pack(side="left", padx=5)

boton_actualizar = tk.Button(
    marco_botones, text="Confirmar edicion de cambios", font=("Consolas", 11, "bold"),
    bg="#000000", fg="white", command=guardar_edicion, padx=8, pady=4
)
boton_actualizar.pack(side="left", padx=5)

boton_eliminar = tk.Button(
    marco_botones, text="Despedir empleado", font=("Consolas", 11, "bold"),
    bg="#000000", fg="white", command=eliminar_empleado, padx=8, pady=4
)
boton_eliminar.pack(side="left", padx=5)

empleados_iniciales = [
    ("Kenny Galindo", "3", "44555666", "20", "2"),
    ("Juancho Tazo", "5", "11222333", "22", "3"),
    ("Solomeo Paredes", "2", "77888999", "24", "0")
]

for nombre, anios, dni, asistencias, justificadas in empleados_iniciales:
    bono = calcular_bonificacion(asistencias, justificadas)
    registro = (f"Nombre: {nombre} | Años: {anios} | DNI: {dni} | "
                f"Asist: {asistencias} | Justif: {justificadas} | Bono: {bono}")
    lista_empleados.insert(tk.END, registro)

ventana.mainloop()



