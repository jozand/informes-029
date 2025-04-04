import sqlite3

def insertar_persona(nombre, nit, profesion, correo):
    try:
        conn = sqlite3.connect("actividades.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO persona (nombre, nit, profesion, correo)
            VALUES (?, ?, ?, ?)
        """, (nombre, nit, profesion, correo))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al insertar persona: {e}")
        return False

def obtener_personas():
    conn = sqlite3.connect("actividades.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM persona")
    filas = cursor.fetchall()
    conn.close()
    return filas

def actualizar_persona(id, nombre, nit, profesion, correo):
    try:
        conn = sqlite3.connect("actividades.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE persona
            SET nombre=?, nit=?, profesion=?, correo=?
            WHERE id=?
        """, (nombre, nit, profesion, correo, id))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al actualizar persona: {e}")
        return False

def eliminar_persona(id):
    try:
        conn = sqlite3.connect("actividades.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM persona WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al eliminar persona: {e}")
        return False
