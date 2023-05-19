import tkinter as tk
from tkinter import messagebox
import sqlite3


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.criancas_disponiveis = []
        self.title('AdoptTech')
        self.geometry('400x300')

        titulo_label = tk.Label(self, text='Bem-vindo ao AdoptTech!', font=('Arial', 16))
        titulo_label.pack(pady=10)

        opcao_frame = tk.Frame(self)
        opcao_frame.pack(pady=20)

        escolha_label = tk.Label(opcao_frame, text='Escolha uma opção:')
        escolha_label.pack()

        cadastro_button = tk.Button(opcao_frame, text='Cadastrar', command=self.abrir_janela_cadastro)
        cadastro_button.pack(pady=5)

        consulta_button = tk.Button(opcao_frame, text='Consultar', command=self.consultar)
        consulta_button.pack(pady=5)

        sobre_button = tk.Button(opcao_frame, text='Sobre', command=self.sobre)
        sobre_button.pack(pady=5)

        sair_button = tk.Button(opcao_frame, text='Sair', command=self.sair)
        sair_button.pack(pady=5)

        self.conn = sqlite3.connect('seu_banco_de_dados.db')
        self.cursor = self.conn.cursor()

        # Criação da tabela criancas, se ela não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS criancas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                genero TEXT
            )
        ''')
        self.conn.commit()

    def abrir_janela_cadastro(self):
        self.janela_cadastro = tk.Toplevel(self)
        self.janela_cadastro.title('Cadastro')
        self.janela_cadastro.geometry('400x300')

        nome_label = tk.Label(self.janela_cadastro, text='Nome:')
        nome_label.pack(pady=5)

        self.nome_entry = tk.Entry(self.janela_cadastro)
        self.nome_entry.pack(pady=5)

        idade_label = tk.Label(self.janela_cadastro, text='Idade:')
        idade_label.pack(pady=5)

        self.idade_entry = tk.Entry(self.janela_cadastro)
        self.idade_entry.pack(pady=5)

        genero_label = tk.Label(self.janela_cadastro, text='Gênero:')
        genero_label.pack(pady=5)

        self.genero_entry = tk.Entry(self.janela_cadastro)
        self.genero_entry.pack(pady=5)

        realizar_button = tk.Button(self.janela_cadastro, text='Realizar Cadastro', command=self.cadastrar)
        realizar_button.pack(pady=10)

        self.janela_cadastro.bind('<Return>', lambda event: realizar_button.invoke())

    def cadastrar(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        genero = self.genero_entry.get()

        self.cursor.execute("INSERT INTO criancas (nome, idade, genero) VALUES (?, ?, ?)", (nome, idade, genero))
        self.conn.commit()

        messagebox.showinfo('Cadastro', f'{nome} foi cadastrado com sucesso para adoção!')
        self.janela_cadastro.destroy()

    def consultar(self):
        self.cursor.execute("SELECT nome, idade, genero FROM criancas")
        resultados = self.cursor.fetchall()

        if len(resultados) == 0:
            messagebox.showinfo('Consulta', 'Não há crianças cadastradas para adoção.')
        else:
            janela_consulta = tk.Toplevel()
            janela_consulta.title('Consulta')
            janela_consulta.geometry('300x200')

            lista_label = tk.Label(janela_consulta, text='Crianças cadastradas:')
            lista_label.pack(pady=5)

            lista_text = tk.Text(janela_consulta)
            lista_text.pack()

            for nome, idade, genero in sorted(resultados):
                lista_text.insert(tk.END, f'Nome: {nome}\nIdade: {idade}\nGênero: {genero}\n\n')

            janela_consulta.bind('<Return>', lambda event: janela_consulta.destroy())

            janela_consulta.mainloop()

    def sobre(self):
        messagebox.showinfo('Sobre', 'O AdoptTech tem como objetivo ajudar a encontrar lares para crianças.')

    def sair(self):
        self.conn.close()
        self.destroy()


if __name__ == '__main__':
    app = Application()
    app.mainloop()
