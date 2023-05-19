import tkinter as tk
from tkinter import messagebox
import sqlite3


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
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

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Menina (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomemenina TEXT,
                CPF CHAR (11),
                RG CHAR (9),
                Hist_saude VARCHAR(75),
                PCD INTEGER,
                Data_nasc CHAR(8),
                Data_entrada CHAR(8)                
            )
        ''')
        self.conn.commit()

    def abrir_janela_cadastro(self):
        self.janela_cadastro = tk.Toplevel(self)
        self.janela_cadastro.title('Cadastro')
        self.janela_cadastro.geometry('600x500')

        nomemenina_label = tk.Label(self.janela_cadastro, text='Nome:')
        nomemenina_label.pack(pady=5)

        self.nomemenina_entry = tk.Entry(self.janela_cadastro)
        self.nomemenina_entry.pack(pady=5)

        cpf_label = tk.Label(self.janela_cadastro, text='CPF:')
        cpf_label.pack(pady=5)

        self.cpf_entry = tk.Entry(self.janela_cadastro)
        self.cpf_entry.pack(pady=5)

        rg_label = tk.Label(self.janela_cadastro, text='RG:')
        rg_label.pack(pady=5)

        self.rg_entry = tk.Entry(self.janela_cadastro)
        self.rg_entry.pack(pady=5)

        hs_label = tk.Label(self.janela_cadastro, text='Hist. Saúde:')
        hs_label.pack(pady=5)

        self.hs_entry = tk.Entry(self.janela_cadastro)
        self.hs_entry.pack(pady=5)

        pcd_label = tk.Label(self.janela_cadastro, text='PCD:')
        pcd_label.pack(pady=5)

        self.pcd_entry = tk.Entry(self.janela_cadastro)
        self.pcd_entry.pack(pady=5)

        dn_label = tk.Label(self.janela_cadastro, text='Data de Nascimento:')
        dn_label.pack(pady=5)

        self.dn_entry = tk.Entry(self.janela_cadastro)
        self.dn_entry.pack(pady=5)

        de_label = tk.Label(self.janela_cadastro, text='Data de Entrada:')
        de_label.pack(pady=5)

        self.de_entry = tk.Entry(self.janela_cadastro)
        self.de_entry.pack(pady=5)

        realizar_button = tk.Button(self.janela_cadastro, text='Realizar Cadastro', command=self.cadastrar)
        realizar_button.pack(pady=10)

        self.janela_cadastro.bind('<Return>', lambda event: realizar_button.invoke())

    def cadastrar(self):
        nomemenina = self.nomemenina_entry.get()
        rg = self.rg_entry.get()
        cpf = self.cpf_entry.get()
        de = self.de_entry.get()

        self.cursor.execute("INSERT INTO Menina (nomemenina, RG, CPF, Data_entrada) VALUES (?, ?, ?, ?)",
                            (nomemenina, rg, cpf, de))
        self.conn.commit()

        messagebox.showinfo('Cadastro', f'{nomemenina} foi cadastrado com sucesso para adoção!')
        self.janela_cadastro.destroy()

    def consultar(self):
        self.cursor.execute("SELECT nomemenina, RG, CPF, Data_entrada FROM Menina")
        resultados = self.cursor.fetchall()

        if len(resultados) == 0:
            messagebox.showinfo('Consulta', 'Não há meninas cadastradas para adoção.')
        else:
            janela_consulta = tk.Toplevel()
            janela_consulta.title('Consulta')
            janela_consulta.geometry('300x200')

            lista_label = tk.Label(janela_consulta, text='Meninas cadastradas:')
            lista_label.pack(pady=5)

            lista_text = tk.Text(janela_consulta)
            lista_text.pack()

            for nomemenina, rg, cpf, _ in sorted(resultados):
                lista_text.insert(tk.END, f'Nome: {nomemenina}\nRG: {rg}\nCPF: {cpf}\n\n')

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
