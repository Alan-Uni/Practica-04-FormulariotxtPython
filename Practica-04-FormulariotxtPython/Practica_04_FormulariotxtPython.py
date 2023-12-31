
import tkinter as tk
from tkinter import messagebox
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_campos():
    limpiar_campos()

def guardar_datos():
    nombre = entry_nombre.get()
    apellidos=entry_apellidos.get()
    edad= entry_edad.get()
    estatura=entry_estatura.get()
    telefono=entry_telefono.get()
    genero=""
    if var_genero.get()==1:
       genero="Hombre"
    elif var_genero.get()==2:
       genero="Mujer"

    datos= f"Nombres: {nombre}\nApellidos: {apellidos}\nEdad:  {edad} años\nEstatura: {estatura}cm\nTelefono:  {telefono}\nGenero: {genero}"

    with open("datos99.txt","a") as archivo:
       archivo.write(datos+ "\n\n")


    
    messagebox.showinfo("Informacion","Datos guardados con exito\n\n" + datos)

    entry_nombre.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0)



formulario = tk.Tk()
formulario.title("Formulario")

var_genero = tk.IntVar()

label_nombre= tk.Label(formulario, text="Nombres:")
label_nombre.pack()
entry_nombre = tk.Entry(formulario)
entry_nombre.pack()

label_apellidos = tk.Label(formulario, text= "Apellidos:")
label_apellidos.pack()
entry_apellidos = tk.Entry(formulario)
entry_apellidos.pack()

label_edad = tk.Label(formulario, text= "Edad:")
label_edad.pack()
entry_edad = tk.Entry(formulario)
entry_edad.pack()

label_estatura = tk.Label(formulario, text= "Estatura:(cm)")
label_estatura.pack()
entry_estatura = tk.Entry(formulario)
entry_estatura.pack()

label_telefono = tk.Label(formulario, text= "Telefono:")
label_telefono.pack()
entry_telefono = tk.Entry(formulario)
entry_telefono.pack()

label_genero = tk.Label(formulario, text="Género:")
label_genero.pack()

rb_hombre = tk.Radiobutton(formulario, text="Hombre", variable=var_genero, value=1)
rb_hombre.pack()

rb_hombre = tk.Radiobutton(formulario, text="Mujer", variable=var_genero, value=2)
rb_hombre.pack()

btn_guardar = tk.Button(formulario, text= "Guardar", command=guardar_datos)
btn_guardar.pack()

btn_borrar = tk.Button(formulario, text= "Borrar campos", command=borrar_campos)
btn_borrar.pack()

formulario.mainloop()