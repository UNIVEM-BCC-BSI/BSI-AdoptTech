import tkinter as tk
import sqlite3
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image

class tela_cadastro(tk.Tk):
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect('AdoptTech_SQLite.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
        user	INTEGER NOT NULL,
        senha	NUMERIC NOT NULL
        
        )
        ''')
        self.title('CADASTRO')
        self.geometry('800x600')
        self.configure(bg='#6598e4')

        user_label = tk.Label(self, text="Usuário", bg="#6598e4")
        user_label.pack(pady=10)

        self.user_entry = tk.Entry(self)
        self.user_entry.pack(pady=10)

        senha_label = tk.Label(self, text='Senha:', bg='#6598e4')
        senha_label.pack()

        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack(pady=10)

        cadastrar_button = tk.Button(self, text='Realizar Cadastro', command=self.realizar_cadastro)
        cadastrar_button.pack(pady=10)

    def realizar_cadastro(self):
        user = self.user_entry.get()
        senha = self.senha_entry.get()

        self.cursor.execute("INSERT INTO usuarios (user, senha) VALUES (?, ?)", (user, senha))
        if self.cursor.rowcount > 0:
            messagebox.showinfo("Cadastro", "Cadastro bem-sucedido!")
            self.conn.commit()
            subprocess.Popen(["python3", "PgLogin.py"])
            self.conn.close()
            self.destroy()
        else:
            messagebox.showerror("Cadastro", "Credenciais inválidas.")

if __name__ == "__main__":
    tela = tela_cadastro()
    tela.mainloop()

