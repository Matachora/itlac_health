import tkinter as tk
import sqlite3

conn = sqlite3.connect('nombres.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS nombres (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)')

def guardar_nombre():
    nombre = entrada_nombre.get()
    cursor.execute('INSERT INTO nombres (nombre) VALUES (?)', (nombre,))
    conn.commit()
    label_mensaje['text'] = 'Nombre guardado correctamente'

ventana = tk.Tk()
ventana.title("Guardar Nombres")
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()
boton_guardar = tk.Button(ventana, text="Guardar Nombre", command=guardar_nombre)
boton_guardar.pack()
label_mensaje = tk.Label(ventana)
label_mensaje.pack()
ventana.mainloop()
conn.close()