import sqlite3

def obtener_personas_para_contrato():
    conn = sqlite3.connect("actividades.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM persona")
    personas = cursor.fetchall()
    conn.close()
    return personas

def insertar_contrato(persona_id, fecha_contrato, numero_contrato, dependencia, tipo):
    try:
        conn = sqlite3.connect("actividades.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contrato (persona_id, fecha_contrato, numero_contrato, dependencia, tipo)
            VALUES (?, ?, ?, ?, ?)
        """, (persona_id, fecha_contrato, numero_contrato, dependencia, tipo))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al insertar contrato: {e}")
        return False

def obtener_contratos():
    conn = sqlite3.connect("actividades.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT contrato.id, persona.nombre, fecha_contrato, numero_contrato, dependencia, tipo
        FROM contrato
        INNER JOIN persona ON contrato.persona_id = persona.id
    """)
    contratos = cursor.fetchall()
    conn.close()
    return contratos

def actualizar_contrato(id, persona_id, fecha_contrato, numero_contrato, dependencia, tipo):
    try:
        conn = sqlite3.connect("actividades.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE contrato
            SET persona_id=?, fecha_contrato=?, numero_contrato=?, dependencia=?, tipo=?
            WHERE id=?
        """, (persona_id, fecha_contrato, numero_contrato, dependencia, tipo, id))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al actualizar contrato: {e}")
        return False

def eliminar_contrato(id):
    try:
        conn = sqlite3.connect("actividades.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contrato WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al eliminar contrato: {e}")
        return False
