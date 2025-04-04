import tkinter as tk
from tkinter import ttk, messagebox
from controllers.contrato_controller import (
    obtener_personas_para_contrato,
    insertar_contrato,
    obtener_contratos,
    actualizar_contrato,
    eliminar_contrato
)

def abrir_formulario_contrato():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Contratos")
    ventana.geometry("800x500")

    # Campos
    tk.Label(ventana, text="Persona").grid(row=0, column=0, padx=5, pady=5)
    personas_combo = ttk.Combobox(ventana, state="readonly", width=40)
    personas_combo.grid(row=0, column=1, padx=5)

    tk.Label(ventana, text="Fecha Contrato").grid(row=1, column=0, padx=5, pady=5)
    entry_fecha = tk.Entry(ventana, width=40)
    entry_fecha.grid(row=1, column=1)

    tk.Label(ventana, text="Número Contrato").grid(row=2, column=0, padx=5, pady=5)
    entry_numero = tk.Entry(ventana, width=40)
    entry_numero.grid(row=2, column=1)

    tk.Label(ventana, text="Dependencia").grid(row=3, column=0, padx=5, pady=5)
    entry_dependencia = tk.Entry(ventana, width=40)
    entry_dependencia.grid(row=3, column=1)

    tk.Label(ventana, text="Tipo").grid(row=4, column=0, padx=5, pady=5)
    tipo_combo = ttk.Combobox(ventana, state="readonly", values=["TECNICOS", "PROFESIONALES"], width=37)
    tipo_combo.grid(row=4, column=1)

    btn_guardar = tk.Button(ventana, text="Guardar", width=20)
    btn_guardar.grid(row=5, column=1, pady=10)

    id_actual = None
    personas_dict = {}

    # Tabla
    tree = ttk.Treeview(ventana, columns=("ID", "Persona", "Fecha", "Numero", "Dependencia", "Tipo"), show="headings")
    tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    for col in tree["columns"]:
        tree.heading(col, text=col)

    def cargar_personas():
        personas = obtener_personas_para_contrato()
        nombres = []
        for pid, nombre in personas:
            nombres.append(nombre)
            personas_dict[nombre] = pid
        personas_combo["values"] = nombres

    def cargar_contratos():
        for item in tree.get_children():
            tree.delete(item)
        contratos = obtener_contratos()
        for contrato in contratos:
            tree.insert("", "end", values=contrato)

    def guardar():
        nonlocal id_actual
        persona_nombre = personas_combo.get()
        persona_id = personas_dict.get(persona_nombre)
        fecha = entry_fecha.get()
        numero = entry_numero.get()
        dependencia = entry_dependencia.get()
        tipo = tipo_combo.get()

        if not persona_id:
            messagebox.showerror("Error", "Debe seleccionar una persona")
            return

        if id_actual:
            ok = actualizar_contrato(id_actual, persona_id, fecha, numero, dependencia, tipo)
        else:
            ok = insertar_contrato(persona_id, fecha, numero, dependencia, tipo)

        if ok:
            messagebox.showinfo("Éxito", "Contrato guardado correctamente")
            limpiar()
            cargar_contratos()
        else:
            messagebox.showerror("Error", "No se pudo guardar el contrato")

    def limpiar():
        nonlocal id_actual
        entry_fecha.delete(0, tk.END)
        entry_numero.delete(0, tk.END)
        entry_dependencia.delete(0, tk.END)
        tipo_combo.set("")
        personas_combo.set("")
        id_actual = None
        btn_guardar.config(text="Guardar")

    def seleccionar(event):
        nonlocal id_actual
        item = tree.selection()
        if item:
            valores = tree.item(item)["values"]
            id_actual = valores[0]
            personas_combo.set(valores[1])
            entry_fecha.delete(0, tk.END)
            entry_fecha.insert(0, valores[2])
            entry_numero.delete(0, tk.END)
            entry_numero.insert(0, valores[3])
            entry_dependencia.delete(0, tk.END)
            entry_dependencia.insert(0, valores[4])
            tipo_combo.set(valores[5])
            btn_guardar.config(text="Actualizar")

    def eliminar_seleccionado():
        item = tree.selection()
        if not item:
            messagebox.showwarning("Aviso", "Seleccione un contrato para eliminar")
            return
        valores = tree.item(item)["values"]
        if messagebox.askyesno("Confirmar", f"¿Eliminar contrato {valores[3]}?"):
            if eliminar_contrato(valores[0]):
                messagebox.showinfo("Eliminado", "Contrato eliminado")
                cargar_contratos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar")

    tree.bind("<<TreeviewSelect>>", seleccionar)
    btn_guardar.config(command=guardar)

    btn_eliminar = tk.Button(ventana, text="Eliminar contrato", command=eliminar_seleccionado)
    btn_eliminar.grid(row=7, column=0, columnspan=2, pady=10)

    cargar_personas()
    cargar_contratos()
