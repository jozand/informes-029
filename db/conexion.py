import sqlite3
import os

def inicializar_base_datos():
    # Solo crea si no existe
    if not os.path.exists("actividades.db"):
        conn = sqlite3.connect("actividades.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS persona (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nit TEXT,
            profesion TEXT,
            correo TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contrato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona_id INTEGER,
            fecha_contrato TEXT,
            numero_contrato TEXT,
            dependencia TEXT,
            tipo TEXT CHECK(tipo IN ('TECNICOS', 'PROFESIONALES')),
            FOREIGN KEY (persona_id) REFERENCES persona(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS informe_encabezado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contrato_id INTEGER,
            fecha_del TEXT,
            fecha_al TEXT,
            FOREIGN KEY (contrato_id) REFERENCES contrato(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS informe_detalle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encabezado_id INTEGER,
            numero_actividad INTEGER,
            descripcion_actividad TEXT,
            FOREIGN KEY (encabezado_id) REFERENCES informe_encabezado(id)
        );   
        """)


        conn.commit()
        conn.close()
        print("Base de datos creada exitosamente.")
    else:
        print("Base de datos ya existe.")
