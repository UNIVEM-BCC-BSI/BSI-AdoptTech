import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.criancas_disponiveis = []
        self.title('AdoptTech')
        self.geometry('1024x768')

        self.configure(bg="#6598e4")

        titulo_label = tk.Label(self, text='ADOPTTECH', font=('Quicksand', 30), bg="#6598e4")
        titulo_label.pack(pady=0)

        opcao_frame = tk.Frame(self, bg="#6598e4")
        opcao_frame.pack(pady=15)

        escolha_label = tk.Label(opcao_frame, text='Escolha uma opção:', font=('Quicksand', 15), bg="#6598e4")
        escolha_label.pack()

        image = Image.open('CADASTRO.png')
        photo = ImageTk.PhotoImage(image)
        cadastro_button = tk.Button(opcao_frame, image=photo, command=self.abrir_janela_cadastro, bg="#6598e4")
        cadastro_button.image = photo
        cadastro_button.pack(pady=15)


        image = Image.open('CONSULTA.png')
        photo = ImageTk.PhotoImage(image)
        consulta_button = tk.Button(opcao_frame, image=photo, command=self.consultar, bg="#6598e4")
        consulta_button.image = photo
        consulta_button.pack(pady=15)

        image = Image.open('SOBRE.png')
        photo = ImageTk.PhotoImage(image)
        sobre_button = tk.Button(opcao_frame, image=photo, command=self.sobre, bg="#6598e4")
        sobre_button.image = photo
        sobre_button.pack(pady=15)

        image = Image.open('SAIR.png')
        photo = ImageTk.PhotoImage(image)
        sair_button = tk.Button(opcao_frame, image=photo, command=self.sair, bg="#6598e4")
        sair_button.image = photo
        sair_button.pack(pady=15)

        self.conn = sqlite3.connect('AdoptTech_SQLite.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Crianca (
                IDCrianca INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome_Crianca TEXT,
                CPF CHAR(11),
                RG CHAR(9),
                Hist_saude REAL,
                PCD REAL,
                Data_nasc CHAR(8),
                Data_entrada CHAR(8)
                
            )
        ''')
        self.conn.commit()

    def abrir_janela_cadastro(self):
        self.janela_cadastro = tk.Toplevel(self)
        self.janela_cadastro.title('Cadastro')
        self.janela_cadastro.geometry('1024x768')

        self.janela_cadastro.configure(bg="#6598e4")

        nome_crianca_label = tk.Label(self.janela_cadastro, text='Nome:', bg="#6598e4", font=('Quicksand', 20))
        nome_crianca_label.pack(pady=7)

        self.nome_crianca_entry = tk.Entry(self.janela_cadastro, width=40)
        self.nome_crianca_entry.pack(pady=7)

        cpf_label = tk.Label(self.janela_cadastro, text='CPF:', bg="#6598e4", font=('Quicksand', 20))
        cpf_label.pack(pady=7)

        self.cpf_entry = tk.Entry(self.janela_cadastro, width=40)
        self.cpf_entry.pack(pady=7)

        rg_label = tk.Label(self.janela_cadastro, text='RG:', bg="#6598e4", font=('Quicksand', 20))
        rg_label.pack(pady=7)

        self.rg_entry = tk.Entry(self.janela_cadastro, width=40)
        self.rg_entry.pack(pady=7)

        hs_label = tk.Label(self.janela_cadastro, text='Hist. Saúde:', bg="#6598e4", font=('Quicksand', 20))
        hs_label.pack(pady=7)

        self.hs_entry = tk.Entry(self.janela_cadastro, width=40)
        self.hs_entry.pack(pady=7)

        pcd_label = tk.Label(self.janela_cadastro, text='PCD:', bg="#6598e4" ,font=('Quicksand', 20))
        pcd_label.pack(pady=7)

        self.pcd_entry = tk.Entry(self.janela_cadastro, width=40)
        self.pcd_entry.pack(pady=7)

        dn_label = tk.Label(self.janela_cadastro, text='Data de Nascimento:', bg="#6598e4", font=('Quicksand', 20))
        dn_label.pack(pady=7)

        self.dn_entry = tk.Entry(self.janela_cadastro, width=40)
        self.dn_entry.pack(pady=7)

        de_label = tk.Label(self.janela_cadastro, text='Data de Entrada:', bg="#6598e4", font=('Quicksand', 20))
        de_label.pack(pady=7)

        self.de_entry = tk.Entry(self.janela_cadastro, width=40)
        self.de_entry.pack(pady=7)

        image = Image.open('CADASTRO.png')
        photo = ImageTk.PhotoImage(image)
        realizar_button = tk.Button(self.janela_cadastro, command=self.cadastrar, image=photo)
        realizar_button.image = photo
        realizar_button.pack(pady=10)

        self.janela_cadastro.bind('<Return>', lambda event: realizar_button.invoke())

    def cadastrar(self):
        nome_crianca = self.nome_crianca_entry.get()
        cpf = self.cpf_entry.get()
        rg = self.rg_entry.get()
        hs = self.hs_entry.get()
        pcd = self.pcd_entry.get()
        dn = self.dn_entry.get()
        de = self.de_entry.get()

        self.cursor.execute("INSERT INTO Crianca (Nome_Crianca, CPF, RG, Hist_saude, PCD, Data_nasc, Data_entrada) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome_crianca, cpf, rg, hs, pcd, dn, de))
        self.conn.commit()

        messagebox.showinfo('Cadastro', f'{nome_crianca} foi cadastrado com sucesso para adoção!')
        self.janela_cadastro.destroy()

    def consultar(self):
        self.cursor.execute("SELECT Nome_Crianca, CPF, RG FROM Crianca")
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

            for nome_crianca, cpf, rg in sorted(resultados):
                lista_text.insert(tk.END, f'Nome: {nome_crianca}\nCPF: {cpf}\nRG: {rg}\n\n')

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