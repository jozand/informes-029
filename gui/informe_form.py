import tkinter as tk
from tkinter import ttk, messagebox
from controllers.informe_controller import (
    obtener_contratos_para_informe,
    insertar_encabezado,
    insertar_actividad
)

def abrir_formulario_informe():
    ventana = tk.Toplevel()
    ventana.title("Ingreso de Informes")
    ventana.geometry("600x500")

    tk.Label(ventana, text="Contrato").pack()
    combo_contrato = ttk.Combobox(ventana, width=50)
    contratos = obtener_contratos_para_informe()
    combo_contrato["values"] = [f"{id} - {nombre}" for id, nombre in contratos]
    combo_contrato.pack()

    tk.Label(ventana, text="Fecha del (YYYY-MM-DD)").pack()
    entry_del = tk.Entry(ventana)
    entry_del.pack()

    tk.Label(ventana, text="Fecha al (YYYY-MM-DD)").pack()
    entry_al = tk.Entry(ventana)
    entry_al.pack()

    actividades = []

    def agregar_encabezado():
        if not combo_contrato.get() or not entry_del.get() or not entry_al.get():
            messagebox.showerror("Error", "Todos los campos del encabezado son obligatorios")
            return
        contrato_id = int(combo_contrato.get().split(" - ")[0])
        encabezado_id = insertar_encabezado(contrato_id, entry_del.get(), entry_al.get())
        messagebox.showinfo("Éxito", "Encabezado guardado. Ahora puede agregar actividades")
        form_actividad(encabezado_id)

    def form_actividad(encabezado_id):
        frame = tk.Frame(ventana)
        frame.pack(pady=10)
        tk.Label(frame, text="Descripción de Actividad").pack()
        entry_desc = tk.Text(frame, height=4, width=60)
        entry_desc.pack()

        def guardar_actividad():
            descripcion = entry_desc.get("1.0", tk.END).strip()
            if descripcion:
                insertar_actividad(encabezado_id, descripcion)
                messagebox.showinfo("Éxito", "Actividad registrada")
                entry_desc.delete("1.0", tk.END)
            else:
                messagebox.showwarning("Aviso", "La descripción no puede estar vacía")

        tk.Button(frame, text="Guardar Actividad", command=guardar_actividad).pack(pady=5)

    tk.Button(ventana, text="Guardar Encabezado", command=agregar_encabezado).pack(pady=10)
