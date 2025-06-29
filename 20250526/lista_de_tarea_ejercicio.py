import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title('Lista de tareas')
ventana.geometry('300x300')

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

frame = tk.Frame(ventana, padx=20, pady=20)
frame.grid(row=0, column=0, sticky="nsew")

ingreso_tarea = tk.Entry(frame, width=40)
ingreso_tarea.grid(row=0, column=0, padx=5, pady=5)

def agregar_tarea():
    tarea = ingreso_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        ingreso_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        for i in sorted(seleccion, reverse=True):
            lista_tareas.delete(i)
    else:
        messagebox.showwarning("Advertencia", "Selecciona al menos una tarea para eliminar.")

lista_tareas = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=40, height=10)
lista_tareas.grid(row=2, column=0, padx=5, pady=5)

boton_agregar = tk.Button(frame, text='Agregar tarea', command=agregar_tarea)
boton_agregar.grid(row=1, column=0, padx=5, pady=5)

boton_eliminar = tk.Button(frame, text='Eliminar tarea', command=eliminar_tarea)
boton_eliminar.grid(row=3, column=0, padx=5, pady=5)

ventana.mainloop()