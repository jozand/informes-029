import tkinter as tk
from tkinter import messagebox
from gui.persona_form import abrir_formulario_persona
from gui.contrato_form import abrir_formulario_contrato
from gui.informe_form import abrir_formulario_informe

def mostrar_menu_principal():
    ventana = tk.Tk()
    ventana.title("Sistema de Actividades")
    ventana.geometry("400x300")

    titulo = tk.Label(ventana, text="Menú Principal", font=("Arial", 16))
    titulo.pack(pady=20)

    btn_personas = tk.Button(
        ventana,
        text="Administrar Personas",
        width=30,
        command=abrir_formulario_persona
    )
    btn_personas.pack(pady=10)

    btn_contratos = tk.Button(
        ventana,
        text="Registrar Contratos",
        width=30,
        command=abrir_formulario_contrato
    )
    btn_contratos.pack(pady=10)

    btn_informes = tk.Button(
        ventana,
        text="Ingresar Informes",
        width=30,
        command=abrir_formulario_informe
    )
    btn_informes.pack(pady=10)

    ventana.mainloop()
