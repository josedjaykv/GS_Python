# Ventana de inicio de sesión

import tkinter as tk
from tkinter import messagebox
from logic.user_manager import login_user

def launch_login():
    def iniciar_sesion():
        username = entry_usuario.get()
        password = entry_password.get()

        if login_user(username, password):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            root.destroy()  # Cerrar login y abrir la ventana principal
            from ui.semesters_window import launch_semesters
            launch_semesters()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    root = tk.Tk()
    root.title("Inicio de Sesión")

    tk.Label(root, text="Usuario:").pack(pady=5)
    entry_usuario = tk.Entry(root)
    entry_usuario.pack(pady=5)

    tk.Label(root, text="Contraseña:").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=10)
    tk.Button(root, text="Registrarse", command=lambda: print("Ir a registro")).pack()

    root.mainloop()
