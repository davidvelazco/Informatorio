import tkinter as tk
import datetime

def saludar():
    print('Holaaaa!')

def hora():
   print(f"{datetime.datetime.now()}")

# clase(molde, formato) ==instanciar/crear==> objeto

# clases: tienen atributos y funciones/metodos

ventana = tk.Tk()
ventana.title("Mi primera ventana con Tkinter")
ventana.geometry("800x600")

texto = tk.Label(ventana, text='Hola desde Tkinter!', font=('Arial', 20))
texto.pack()

boton = tk.Button(ventana, text='Saludar', font=('Arial', 20), command=saludar)
boton.pack()

boton2 = tk.Button(ventana, text='Hora', font=('Arial', 20), command=hora)
boton2.pack()

ventana.mainloop()
