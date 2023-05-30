import tkinter as tk
from tkinter import messagebox
import subprocess
import sqlite3

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('FAÇA LOGIN')
        self.geometry('800x600')
        self.configure(bg='#6598e4')

        username_label = tk.Label(self, text="Usuário:", bg='#6598e4')
        username_label.pack(pady=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=10)

        password_label = tk.Label(self, text="Senha:", bg='#6598e4')
        password_label.pack()

        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=10)

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=20)

        cadastro_button = tk.Button(self, text="Cadastrar")
        cadastro_button.pack(pady=2)


        self.bind('<Return>', self.handle_enter)

    def login(self):
        user = self.username_entry.get()
        senha = self.password_entry.get()

        conn = sqlite3.connect('AdoptTech_SQLite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE user=? AND senha=?", (user, senha))

        if cursor.fetchone() is not None:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            subprocess.Popen(["python3", "PgInicial.py"])
            self.destroy()
        else:
            messagebox.showerror("Login", "Credenciais inválidas.")

        conn.close()

    def handle_enter(self, event):
        self.login()

if __name__ == "__main__":
    window = LoginWindow()
    window.mainloop()
