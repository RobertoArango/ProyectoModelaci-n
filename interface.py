import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from drawgraph import drawGraph

actividades = []
activityList = []

# Retorna array de vertices para el grafo (Graph)
# Recibe un array de datos, de forma [ID,Nombre,[predecesores], Duracion]
def buildVertexArray(data):
    v = []
    for item in data:
        if len(item[2]) >= 1:
            v.append(Node(item[0], item[1], item[3], []))
        else:
            v.append(Node(item[0], item[1], item[3]))

    for index in range(len(data)):
        for predecesor in data[index][2]:
            for i in range(len(data)):
                if data[i][0] == predecesor:
                    v[index].past.append(v[i])

    return v

def mostrar_actividades():
    ventana_actividades = tk.Toplevel(ventana)
    ventana_actividades.title("Actividades")
    

    if len(actividades) == 0:
        #tamaño de la pantalla 
        ancho_pantalla = ventana_actividades.winfo_screenwidth()
        alto_pantalla = ventana_actividades.winfo_screenheight()

        # Calcular la posición central de la ventana
        posicion_x = int((ancho_pantalla - 400) / 2)
        posicion_y = int((alto_pantalla - 50) / 2)

        # Establecer la posición de la ventana
        ventana_actividades.geometry(f"400x50+{posicion_x}+{posicion_y}")

        nombre_act = tk.Label(ventana_actividades, text=f"Todavía no tienes actividades agregadas", font=("Arial", 16, "bold"), fg="red")
        nombre_act.pack() 
        btn = tk.Button(ventana_actividades, text="Regresar", font=("bold"), command=lambda: regresar( ventana_actividades))
        btn.pack()

    else:
        #tamaño de la pantalla 
        ancho_pantalla = ventana_actividades.winfo_screenwidth()
        alto_pantalla = ventana_actividades.winfo_screenheight()

        # Calcular la posición central de la ventana
        posicion_x = int((ancho_pantalla - 700) / 2)
        posicion_y = int((alto_pantalla - 400) / 2)

        # Establecer la posición de la ventana
        ventana_actividades.geometry(f"700x400+{posicion_x}+{posicion_y}")
        tit = tk.Label(ventana_actividades, text=f"Estas son tus actividades agregadas:", font=("Arial", 16), foreground='darkblue')
        tit.pack()
        lista_act=[] 
        for indice, i in enumerate(actividades, start=1):
            line = tk.Label(ventana_actividades, text=f"----------------------------")
            line.pack()  
            nombre_act = tk.Label(ventana_actividades, text=f"( ACTIVIDAD {indice} ) ID: {i[0]} | Nombre: {i[1]} | Predecesor: {i[2]} | Duración: {i[3]} |")
            nombre_act.pack()
            lista_act.append(indice)

        line = tk.Label(ventana_actividades, text=f"----------------------------")
        line.pack()
        combo1 = ttk.Combobox(ventana_actividades, values=lista_act, width=15, state="readonly")
        combo1.pack()
        
        
        btn = tk.Button(ventana_actividades, text="Eliminar actividad", foreground="red", font=("bold"),command=lambda indice=combo1: eliminar_act(indice, ventana_actividades))
        btn.pack()
        btn = tk.Button(ventana_actividades, text="Regresar", font=("bold"), command=lambda: regresar( ventana_actividades))
        btn.pack()