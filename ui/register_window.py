# Ventana de registro

import tkinter as tk
from tkinter import messagebox
from logic.user_manager import register_user
from logic.utils import go_to

def launch_register():
    def register():
        # Obtener los valores de los campos de texto del formulario
        username = entry_usuario.get()
        password = entry_password.get()
        nombre = entry_name.get()
        apellido = entry_lastname.get()


        if register_user(username, password, nombre, apellido):
            messagebox.showinfo("Éxito", "Registro exitoso")
            root.destroy()  # Cerrar login y abrir la ventana principal
            from ui.semesters_window import launch_semesters
            launch_semesters()
        else:
            messagebox.showerror("Error", "Llena los campos correctamente")

    root = tk.Tk() # Crear la ventana principal del login
    root.title("Inicio de Sesión")

    tk.Label(root, text="Nombre:").pack(pady=5, padx=5)
    entry_name = tk.Entry(root) 
    entry_name.pack(pady=5, padx=5)

    tk.Label(root, text="Apellido:").pack(pady=5, padx=5)
    entry_lastname = tk.Entry(root) 
    entry_lastname.pack(pady=5, padx=5)

    tk.Label(root, text="Nombre de Usuario:").pack(pady=5, padx=5)
    entry_usuario = tk.Entry(root) # Crear un campo de texto para el usuario, root es el parametro que indica en que ventana se va a mostrar
    entry_usuario.pack(pady=5, padx=5)

    tk.Label(root, text="Contraseña:").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)


    tk.Button(root, text="Registrarse", command=register).pack(pady=(5,10))
    from ui.login_window import launch_login
    tk.Button(root, text="¿Ya tienes cuenta?", command=lambda: go_to(root, launch_login)).pack(pady=(10,5))

    root.mainloop() # Inicia el bucle principal de Tkinter, que mantiene la ventana abierta y responde a las interacciones del usuario.
