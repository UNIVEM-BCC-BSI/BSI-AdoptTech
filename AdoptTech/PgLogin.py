import tkinter as tk
import sqlite3
from tkinter import messagebox
import subprocess

def login():
    user = username_entry.get()
    senha = password_entry.get()

    conn = sqlite3.connect('AdoptTech_SQLite.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE user=? AND senha=?", (user, senha))

    if cursor.fetchone() is not None:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        subprocess.Popen(["python", "PgInicial.py"])  # Abre o arquivo PgInicial.py
    else:
        messagebox.showerror("Login", "Credenciais inválidas.")

    conn.close()

window = tk.Tk()
window.title("Tela de Login")
window.configure(bg='#E8E8E8')

username_label = tk.Label(window, text="Usuário:", bg='#E8E8E8')
username_label.pack()

password_label = tk.Label(window, text="Senha:", bg='#E8E8E8')
password_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_entry = tk.Entry(window, show='*')
password_entry.pack()

login_button = tk.Button(window, text="Login", command=login, bg='#4CAF50', fg='white')
login_button.pack()

window.mainloop()
