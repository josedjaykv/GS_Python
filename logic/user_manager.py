# Lógica de autenticación y gestión de usuarios

from database.db_manager import DB_PATH
import sqlite3
import hashlib

def register_user(username, password, nombre, apellido):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    # .encode() convierte el texto a bytes, necesario para el hash.
    # .hexdigest() convierte el hash binario en una cadena hexadecimal.

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuario (username, password_hash, nombre, apellido) VALUES (?, ?, ?, ?)", (username, password_hash, nombre, apellido))
        # Los ? se llaman marcadores de posición y se reemplazan por los valores en el segundo argumento de execute
        conn.commit() # Guarda los cambios realizados en la base de datos.
        conn.close() # Cierra la conexión con la base de datos.
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE username = ? AND password_hash = ?", (username, password_hash))
    user = cursor.fetchone() # Obtiene el primer resultado de la consulta (o None si no hay coincidencia).
    conn.close()

    return user is not None
    # Devuelve True si encontró un usuario (el inicio de sesión es válido), o False si no lo encontró.