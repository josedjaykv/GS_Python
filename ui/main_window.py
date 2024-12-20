import tkinter as tk
from tkinter import messagebox
from database.db_manager import initialize_database, insert_promedio, get_promedios

def guardar_datos(nombre, promedio):
    try:
        promedio = float(promedio)
        insert_promedio(nombre, promedio)
        messagebox.showinfo("Éxito", "Promedio guardado correctamente")
    except ValueError:
        messagebox.showerror("Error", "El promedio debe ser un número")

def mostrar_promedios():
    registros = get_promedios()
    texto = "\n".join([f"{r[1]}: {r[2]}" for r in registros])
    messagebox.showinfo("Promedios", texto)

def launch_app():
    initialize_database()

    root = tk.Tk()
    root.title("Calculadora de Promedios")

    tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Promedio:").grid(row=1, column=0, padx=10, pady=5)
    entry_promedio = tk.Entry(root)
    entry_promedio.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(root, text="Guardar", command=lambda: guardar_datos(entry_nombre.get(), entry_promedio.get())).grid(row=2, column=0, pady=10)
    tk.Button(root, text="Mostrar", command=mostrar_promedios).grid(row=2, column=1, pady=10)

    root.mainloop()
