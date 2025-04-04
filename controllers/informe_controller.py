import sqlite3

def obtener_contratos_para_informe():
    conn = sqlite3.connect("actividades.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT contrato.id, persona.nombre || ' - ' || contrato.numero_contrato
        FROM contrato
        INNER JOIN persona ON persona.id = contrato.persona_id
    """)
    contratos = cursor.fetchall()
    conn.close()
    return contratos

def insertar_encabezado(contrato_id, fecha_del, fecha_al):
    conn = sqlite3.connect("actividades.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO informe_encabezado (contrato_id, fecha_del, fecha_al)
        VALUES (?, ?, ?)
    """, (contrato_id, fecha_del, fecha_al))
    encabezado_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return encabezado_id

def obtener_numero_actividad(encabezado_id):
    conn = sqlite3.connect("actividades.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) FROM informe_detalle WHERE encabezado_id = ?
    """, (encabezado_id,))
    numero = cursor.fetchone()[0] + 1
    conn.close()
    return numero

def insertar_actividad(encabezado_id, descripcion_actividad):
    numero = obtener_numero_actividad(encabezado_id)
    conn = sqlite3.connect("actividades.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO informe_detalle (encabezado_id, numero_actividad, descripcion_actividad)
        VALUES (?, ?, ?)
    """, (encabezado_id, numero, descripcion_actividad))
    conn.commit()
    conn.close()
    return True
