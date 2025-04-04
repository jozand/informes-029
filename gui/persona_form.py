import tkinter as tk
from tkinter import ttk, messagebox
from controllers.persona_controller import (
    insertar_persona,
    obtener_personas,
    actualizar_persona,
    eliminar_persona
)

def abrir_formulario_persona():
    ventana = tk.Toplevel()
    ventana.title("Administrar Personas")
    ventana.geometry("700x500")

    # Formulario
    tk.Label(ventana, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(ventana, width=40)
    entry_nombre.grid(row=0, column=1, padx=10)

    tk.Label(ventana, text="NIT").grid(row=1, column=0, padx=10, pady=5)
    entry_nit = tk.Entry(ventana, width=40)
    entry_nit.grid(row=1, column=1, padx=10)

    tk.Label(ventana, text="Profesión").grid(row=2, column=0, padx=10, pady=5)
    entry_profesion = tk.Entry(ventana, width=40)
    entry_profesion.grid(row=2, column=1, padx=10)

    tk.Label(ventana, text="Correo").grid(row=3, column=0, padx=10, pady=5)
    entry_correo = tk.Entry(ventana, width=40)
    entry_correo.grid(row=3, column=1, padx=10)

    btn_guardar = tk.Button(ventana, text="Guardar", width=20)
    btn_guardar.grid(row=4, column=1, pady=10)

    id_actual = None  # Para edición

    # Tabla
    tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "NIT", "Profesion", "Correo"), show="headings")
    tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    for col in tree["columns"]:
        tree.heading(col, text=col)

    def cargar_personas():
        for fila in tree.get_children():
            tree.delete(fila)
        personas = obtener_personas()
        for persona in personas:
            tree.insert("", "end", values=persona)

    def guardar():
        nonlocal id_actual
        nombre = entry_nombre.get()
        nit = entry_nit.get()
        profesion = entry_profesion.get()
        correo = entry_correo.get()

        if nombre == "":
            messagebox.showerror("Error", "Nombre obligatorio")
            return

        if id_actual:
            ok = actualizar_persona(id_actual, nombre, nit, profesion, correo)
        else:
            ok = insertar_persona(nombre, nit, profesion, correo)

        if ok:
            messagebox.showinfo("Éxito", "Guardado correctamente")
            limpiar()
            cargar_personas()
        else:
            messagebox.showerror("Error", "No se pudo guardar")

    def limpiar():
        nonlocal id_actual
        entry_nombre.delete(0, tk.END)
        entry_nit.delete(0, tk.END)
        entry_profesion.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        id_actual = None
        btn_guardar.config(text="Guardar")

    def seleccionar(event):
        nonlocal id_actual
        item = tree.selection()
        if item:
            valores = tree.item(item)["values"]
            id_actual = valores[0]
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, valores[1])
            entry_nit.delete(0, tk.END)
            entry_nit.insert(0, valores[2])
            entry_profesion.delete(0, tk.END)
            entry_profesion.insert(0, valores[3])
            entry_correo.delete(0, tk.END)
            entry_correo.insert(0, valores[4])
            btn_guardar.config(text="Actualizar")

    def eliminar_seleccionado():
        item = tree.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecciona una persona para eliminar")
            return
        valores = tree.item(item)["values"]
        if messagebox.askyesno("Confirmar", f"¿Eliminar a {valores[1]}?"):
            if eliminar_persona(valores[0]):
                messagebox.showinfo("Eliminado", "Persona eliminada")
                cargar_personas()
            else:
                messagebox.showerror("Error", "No se pudo eliminar")

    tree.bind("<<TreeviewSelect>>", seleccionar)

    btn_eliminar = tk.Button(ventana, text="Eliminar seleccionada", command=eliminar_seleccionado)
    btn_eliminar.grid(row=6, column=0, columnspan=2, pady=10)

    btn_guardar.config(command=guardar)

    cargar_personas()
