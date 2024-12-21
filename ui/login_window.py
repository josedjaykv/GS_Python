# Ventana de inicio de sesión

import tkinter as tk
from tkinter import messagebox
from logic.user_manager import login_user
from logic.utils import go_to

def launch_login():
    def iniciar_sesion():
        # Obtener los valores de los campos de texto del formulario
        username = entry_usuario.get()
        password = entry_password.get()

        if login_user(username, password):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            root.destroy()  # Cerrar login y abrir la ventana principal
            from ui.semesters_window import launch_semesters
            launch_semesters()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    root = tk.Tk() # Crear la ventana principal del login
    root.title("Inicio de Sesión")

    tk.Label(root, text="Usuario:").pack(pady=5, padx=5)
    entry_usuario = tk.Entry(root) # Crear un campo de texto para el usuario, root es el parametro que indica en que ventana se va a mostrar
    entry_usuario.pack(pady=5, padx=5)

    tk.Label(root, text="Contraseña:").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=(10,5))
    from ui.register_window import launch_register
    tk.Button(root, text="¿Aún no te has registrado?", command=lambda:go_to(root, launch_register)).pack(pady=(5,10))

    root.mainloop() # Inicia el bucle principal de Tkinter, que mantiene la ventana abierta y responde a las interacciones del usuario.
