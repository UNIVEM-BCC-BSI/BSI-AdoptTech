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


        image = Image.open('AdoptTech.png')
        photo = ImageTk.PhotoImage(image)
        titulo_label = tk.Label(self, image=photo, bg="#6598e4")
        titulo_label.image = photo
        titulo_label.pack(pady=0)

        opcao_frame = tk.Frame(self, bg="#6598e4")
        opcao_frame.pack(pady=10)

        escolha_label = tk.Label(opcao_frame, text='Escolha uma opção:', bg="#6598e4", font=('Quicksand', 20))
        escolha_label.pack()

        image = Image.open('CADASTRO.png')
        photo = ImageTk.PhotoImage(image)
        cadastro_button = tk.Button(opcao_frame, image=photo, command=self.abrir_janela_cadastro, bg="#6598e4")
        cadastro_button.image = photo
        cadastro_button.pack(pady=12)

        image = Image.open('CONSULTA.png')
        photo = ImageTk.PhotoImage(image)
        consulta_button = tk.Button(opcao_frame, image=photo, command=self.consultar, bg="#6598e4")
        consulta_button.image = photo
        consulta_button.pack(pady=12)

        image = Image.open('SOBRE.png')
        photo = ImageTk.PhotoImage(image)
        sobre_button = tk.Button(opcao_frame, image=photo, command=self.sobre, bg="#6598e4")
        sobre_button.image = photo
        sobre_button.pack(pady=12)

        image = Image.open('SAIR.png')
        photo = ImageTk.PhotoImage(image)
        sair_button = tk.Button(opcao_frame, image=photo, command=self.sair, bg="#6598e4")
        sair_button.image = photo
        sair_button.pack(pady=12)

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


        self.cursor.execute('''  
           CREATE TABLE IF NOT EXISTS Adocao (
            IDAdocao INTEGER PRIMARY KEY AUTOINCREMENT,
            Data	DATE NOT NULL,
            Observacoes	VARCHAR(75),
            Crianca_ID	INTEGER NOT NULL,
            Familia_adotiva_ID	INTEGER NOT NULL, 
            FOREIGN KEY(Familia_adotiva_ID) REFERENCES Familia_adotiva(IDFamilia_adotiva),
            FOREIGN KEY(Crianca_ID) REFERENCES Crianca(IDCrianca)
            );
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Familia_adotiva (
            IDFamilia_adotiva	INTEGER PRIMARY KEY AUTOINCREMENT,
            Ficha_crim	VARCHAR(80) NOT NULL,
            Estado_ci	VARCHAR(10),
            Membros	VARCHAR(45),
            Respon1	VARCHAR(60) NOT NULL,
            CPFResp1	CHAR(11) NOT NULL,
            Respon2	VARCHAR(60) NOT NULL,
            CPFResp2	CHAR(11) NOT NULL,
            Contato	VARCHAR(45) NOT NULL
            );                
            
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Familia_biologica (
            IDFamilia_biologica	INTEGER PRIMARY KEY AUTOINCREMENT,
            Contato	VARCHAR(45) NOT NULL,
            Respon1	VARCHAR(60) NOT NULL,
            CPFRespon1	CHAR(11) NOT NULL,
            Respon2	VARCHAR(60) NOT NULL,
            CPFRespon2	CHAR(11) NOT NULL,
            Rua	VARCHAR(40) NOT NULL,
            Bairro	VARCHAR(40) NOT NULL,
            Numero	VARCHAR(4) NOT NULL
        );

            
        ''')
        self.conn.commit()



        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Abandono (
            IDAbandono	INTEGER PRIMARY KEY AUTOINCREMENT,
            Data	DATE NOT NULL,
            Observacoes	VARCHAR(75),
            Crianca_ID	INTEGER NOT NULL,
            Familia_biologica_ID	INTEGER NOT NULL,
            FOREIGN KEY(Crianca_ID) REFERENCES Crianca(IDCrianca),
            FOREIGN KEY(Familia_biologica_ID) REFERENCES Familia_biologica(IDFamilia_biologica)
            );
        
        ''')
        self.conn.commit()


    def abrir_janela_cadastro(self):
        self.janela_cadastro = tk.Toplevel(self)
        self.janela_cadastro.title('Cadastro')
        self.janela_cadastro.geometry('1024x768')
        self.janela_cadastro.configure(bg="#6598e4")

        cadastrar_crianca_button = tk.Button(self.janela_cadastro, text='Cadastrar Criança', command=self.abrir_janela_crianca)
        cadastrar_crianca_button.pack(pady=10)

        cadastrar_adocao_button = tk.Button(self.janela_cadastro, text='Cadastrar Adocao', command=self.abrir_janela_adocao)
        cadastrar_adocao_button.pack(pady=10)

        cadastrar_familiaadot_button = tk.Button(self.janela_cadastro, text='Cadastrar Familia Adotiva', command=self.abrir_janela_familiaadot)
        cadastrar_familiaadot_button.pack(pady=10)

        cadastrar_abandono_button = tk.Button(self.janela_cadastro, text='Cadastrar Abandono', command=self.abrir_janela_abandono)
        cadastrar_abandono_button.pack(pady=10)

        cadastrar_familiabio_button = tk.Button(self.janela_cadastro, text='Cadastrar Familia Biologica', command=self.abrir_janela_familiabio)
        cadastrar_familiabio_button.pack(pady=10)

    def abrir_janela_familiabio(self):
        self.janela_familiabio = tk.Toplevel(self)
        self.janela_familiabio.title('Cadastrar Família Biológica')
        self.janela_familiabio.geometry('1024x768')
        self.janela_familiabio.configure(bg='#6598e4')

        contact_label = tk.Label(self.janela_familiabio, text='Contato', bg='#6598e4', font=('Quicksand', 20))
        contact_label.pack(pady=5)

        self.contact_entry = tk.Entry(self.janela_familiabio, width=40)
        self.contact_entry.pack(pady=5)

        respons1_label = tk.Label(self.janela_familiabio, text='Responsável 1', bg='#6598e4', font=('Quicksand', 20))
        respons1_label.pack(pady=5)

        self.respons1_entry = tk.Entry(self.janela_familiabio, width=40)
        self.respons1_entry.pack(pady=5)

        cpfrs1_label = tk.Label(self.janela_familiabio, text='CPF Responsável 1', bg='#6598e4', font=('Quicksand', 20))
        cpfrs1_label.pack(pady=5)

        self.cpfrs1_entry = tk.Entry(self.janela_familiabio, width=40)
        self.cpfrs1_entry.pack(pady=5)

        respons2_label = tk.Label(self.janela_familiabio, text='Responsável 2', bg='#6598e4', font=('Quicksand', 20))
        respons2_label.pack(pady=5)

        self.respons2_entry = tk.Entry(self.janela_familiabio, width=40)
        self.respons2_entry.pack(pady=5)

        cpfrs2_label = tk.Label(self.janela_familiabio, text='CPF Responsável 2', bg='#6598e4', font=('Quicksand', 20))
        cpfrs2_label.pack(pady=5)

        self.cpfrs2_entry = tk.Entry(self.janela_familiabio, width=40)
        self.cpfrs2_entry.pack(pady=5)

        rua_label = tk.Label(self.janela_familiabio, text='Rua', bg='#6598e4', font=('Quicksand', 20))
        rua_label.pack(pady=5)

        self.rua_entry = tk.Entry(self.janela_familiabio, width=40)
        self.rua_entry.pack(pady=5)

        bairro_label = tk.Label(self.janela_familiabio, text='Bairro', bg='#6598e4', font=('Quicksand', 20))
        bairro_label.pack(pady=5)

        self.bairro_entry = tk.Entry(self.janela_familiabio, width=40)
        self.bairro_entry.pack(pady=5)

        numero_label = tk.Label(self.janela_familiabio, text='Número', bg='#6598e4', font=('Quicksand', 20))
        numero_label.pack(pady=5)

        self.numero_entry = tk.Entry(self.janela_familiabio, width=40)
        self.numero_entry.pack(pady=5)

    def abrir_janela_adocao(self):
        self.janela_adocao = tk.Toplevel(self)
        self.janela_adocao.title('Cadastrar Adoção')
        self.janela_adocao.geometry('1024x768')
        self.janela_adocao.configure(bg="#6598e4")

        data_label = tk.Label(self.janela_adocao, text="Data", bg='#6598e4', font=('Quicksand', 20))
        data_label.pack(pady=15)

        self.data_entry = tk.Entry(self.janela_adocao, width=40)
        self.data_entry.pack(pady=15)

        obsv_label = tk.Label(self.janela_adocao, text="Observações", bg='#6598e4', font=('Quicksand', 20))
        obsv_label.pack(pady=15)

        self.obsv_entry = tk.Entry(self.janela_adocao, width=40)
        self.obsv_entry.pack(pady=15)

        crianca_id_label = tk.Label(self.janela_adocao, text="ID da Criança", bg="#6598e4", font=('Quicksand', 20))
        crianca_id_label.pack(pady=15)

        self.crianca_id_entry = tk.Entry(self.janela_adocao, width=40)
        self.crianca_id_entry.pack(pady=15)

        famiadot_id_label = tk.Label(self.janela_adocao, text="ID da Familia Adotiva", bg="#6598e4", font=('Quicksand', 20))
        famiadot_id_label.pack(pady=15)

        self.familiaadot_id_entry = tk.Entry(self.janela_adocao, width=40)
        self.familiaadot_id_entry.pack(pady=15)

        #image = Image.open('CADASTRO.png')
        #photo = ImageTk.PhotoImage(image)
        #realizar_button = tk.Button(self.janela_adocao, command=self.cadastrar_adocao, image=photo)
        #realizar_button.image = photo
        #realizar_button.pack(pady=10)

        #self.janela_adocao.bind('<Return>', lambda event: realizar_button.invoke())

    def abrir_janela_crianca(self):
        self.janela_crianca = tk.Toplevel(self)
        self.janela_crianca.title('Cadastrar Criança')
        self.janela_crianca.geometry('1024x768')
        self.janela_crianca.configure(bg='#6598e4')

        nome_crianca_label = tk.Label(self.janela_crianca, text='Nome:', bg="#6598e4", font=('Quicksand', 20))
        nome_crianca_label.pack(pady=7)

        self.nome_crianca_entry = tk.Entry(self.janela_crianca, width=40)
        self.nome_crianca_entry.pack(pady=7)

        cpf_label = tk.Label(self.janela_crianca, text='CPF:', bg="#6598e4", font=('Quicksand', 20))
        cpf_label.pack(pady=7)

        self.cpf_entry = tk.Entry(self.janela_crianca, width=40)
        self.cpf_entry.pack(pady=7)

        rg_label = tk.Label(self.janela_crianca, text='RG:', bg="#6598e4", font=('Quicksand', 20))
        rg_label.pack(pady=7)

        self.rg_entry = tk.Entry(self.janela_crianca, width=40)
        self.rg_entry.pack(pady=7)

        hs_label = tk.Label(self.janela_crianca, text='Hist. Saúde:', bg="#6598e4", font=('Quicksand', 20))
        hs_label.pack(pady=7)

        self.hs_entry = tk.Entry(self.janela_crianca, width=40)
        self.hs_entry.pack(pady=7)

        pcd_label = tk.Label(self.janela_crianca, text='PCD:', bg="#6598e4" ,font=('Quicksand', 20))
        pcd_label.pack(pady=7)

        self.pcd_entry = tk.Entry(self.janela_crianca, width=40)
        self.pcd_entry.pack(pady=7)

        dn_label = tk.Label(self.janela_crianca, text='Data de Nascimento:', bg="#6598e4", font=('Quicksand', 20))
        dn_label.pack(pady=7)

        self.dn_entry = tk.Entry(self.janela_crianca, width=40)
        self.dn_entry.pack(pady=7)

        de_label = tk.Label(self.janela_crianca, text='Data de Entrada:', bg="#6598e4", font=('Quicksand', 20))
        de_label.pack(pady=7)

        self.de_entry = tk.Entry(self.janela_crianca, width=40)
        self.de_entry.pack(pady=7)

        image = Image.open('CADASTRO.png')
        photo = ImageTk.PhotoImage(image)
        realizar_button = tk.Button(self.janela_crianca, command=self.cadastrar_criança, image=photo)
        realizar_button.image = photo
        realizar_button.pack(pady=10)

        self.janela_crianca.bind('<Return>', lambda event: realizar_button.invoke())

    def abrir_janela_abandono(self):
        self.janela_abandono = tk.Toplevel(self)
        self.janela_abandono.title('Cadastrar Abandono')
        self.janela_abandono.geometry('1024x768')
        self.janela_abandono.configure(bg='#6598e4')

        data_label = tk.Label(self.janela_abandono, text='Data:', bg='#6598e4', font=('Quicksand', 20))
        data_label.pack(pady=7)

        self.data_entry = tk.Entry(self.janela_abandono, width=40)
        self.data_entry.pack(pady=7)

        observacoes_label = tk.Label(self.janela_abandono, text='Observações:', bg='#6598e4', font=('Quicksand', 20))
        observacoes_label.pack(pady=7)

        self.observacoes_entry = tk.Entry(self.janela_abandono, width=40)
        self.observacoes_entry.pack(pady=7)

        crianc_id_label = tk.Label(self.janela_abandono, text='ID da Criança', bg='#6598e4', font=('Quicksand', 20))
        crianc_id_label.pack(pady=7)

        self.crianc_id_entry = tk.Entry(self.janela_abandono, width=40)
        self.crianc_id_entry.pack(pady=7)

        familiabio_id_label = tk.Label(self.janela_abandono, text='ID da Familia Biológica', bg='#6598e4', font=('Quicksand', 20))
        familiabio_id_label.pack(pady=7)

        self.familiabio_id_entry = tk.Entry(self.janela_abandono, width=40)
        self.familiabio_id_entry.pack(pady=7)


    def abrir_janela_familiaadot(self):
        self.janela_familiaadot = tk.Toplevel(self)
        self.janela_familiaadot.title('Cadastrar Familia Adotiva')
        self.janela_familiaadot.geometry('1024x768')
        self.janela_familiaadot.configure(bg='#6598e4')

        ficha_crim_label = tk.Label(self.janela_familiaadot, text="Ficha Criminal", bg='#6598e4', font=('Quicksand', 20))
        ficha_crim_label.pack(pady=5)

        self.ficha_crim_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.ficha_crim_entry.pack(pady=5)

        estado_civil_label = tk.Label(self.janela_familiaadot, text="Estado Civil", bg='#6598e4', font=('Quicksand', 20))
        estado_civil_label.pack(pady=5)

        self.estado_civil_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.estado_civil_entry.pack(pady=5)

        membros_label = tk.Label(self.janela_familiaadot, text="Membros", bg='#6598e4', font=('Quicksand', 20))
        membros_label.pack(pady=5)

        self.membros_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.membros_entry.pack(pady=5)

        respon1_label = tk.Label(self.janela_familiaadot, text="Responsável 1", bg='#6598e4', font=('Quicksand', 20))
        respon1_label.pack(pady=5)

        self.respon1_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.respon1_entry.pack(pady=5)


        cpfr1_label = tk.Label(self.janela_familiaadot, text="CPF Responsável 1", bg='#6598e4', font=('Quicksand', 20))
        cpfr1_label.pack(pady=5)

        self.cpfr1_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.cpfr1_entry.pack(pady=5)

        respon2_label = tk.Label(self.janela_familiaadot, text="Responsável 2", bg='#6598e4', font=('Quicksand', 20))
        respon2_label.pack(pady=5)

        self.respon2_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.respon2_entry.pack(pady=5)

        cpfr2_label = tk.Label(self.janela_familiaadot, text="CPF Responsável 2", bg='#6598e4', font=('Quicksand', 20))
        cpfr2_label.pack(pady=5)

        self.cpfr2_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.cpfr2_entry.pack(pady=5)

        contato_label = tk.Label(self.janela_familiaadot, text='Contato', bg='#6598e4', font=('Quicksand', 20))
        contato_label.pack(pady=5)

        self.contato_entry = tk.Entry(self.janela_familiaadot, width=40)
        self.contato_entry.pack(pady=5)

    def cadastrar_criança(self):
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
        self.janela_crianca.destroy()

    def cadastrar_abandono(self):
        data = self.data.entry.get()
        observacoes = self.observacoes.entry.get()
        crianca_id = self.crianca_id_entry.get()
        familia_biologica_id = self.familia_biologica_id_entry.get()

        self.cursor.execute("INSERT INTO Abandono(Data,Observacoes,Crianca_ID,Familia_biologica_ID) VALUES (?,?,?,?)", (data,observacoes,crianca_id,familia_biologica_id))
        self.conn.commit()

        messagebox.showinfo('O registro de abandono foi feito com sucesso')
        self.janela_abandono.destroy()

    def cadastrar_familia_biologica(self):
        IDfamilia_biologica = self.IDfamilia_biologica.entry.get()
        contato = self.contato.entry.get()
        respon1 = self.respon1_entry.get()
        cpfrespon1 = self.cpfrespon1.entry.get()
        respon2 = self.respon1_entry.get()
        cpfrespon2 = self.cpfrespon2.entry.get()
        rua = self.rua_entry.get()
        bairro = self.bairro_entry.get()
        numero = self.numero_entry.get()

        self.cursor.execute("INSERT INTO Familia_biologica(IDFamilia_biologica, Contato, Respon1, CPFRespon1, Respon2, CPFRespon2, Rua, Bairro, Numero) VALUES (?,?,?,?,?,?,?,?)", (IDfamilia_biologica,contato,respon1,cpfrespon1,respon2,cpfrespon2,rua,bairro,numero))
        self.conn.commit()

        messagebox.showinfo('A fámilia foi cadastrada com sucesso!')
        self.janela_familia_biologica.destroy()

    def cadastrar_familia_adotiva(self):
        IDfamilia_adotiva = self.IDfamilia_adotiva.entry.get()
        ficha_crim = self.ficha_crim_entry.get()
        estado_ci = self.estado_civil_entry.get()
        membros = self.membros_entry.get()
        respon1 = self.respon1.entry.get()
        cpfResp1 = self.cpfresp1.entry.get()
        respon2 = self.respon2.entry.get()
        cpfResp2 = self.cpfrespo2.entry.get()
        contato = self.contato.entry.get()

        self.cursor.execute(("INSERT INTO Familia_adotiva(IDFamilia_adotiva, Ficha_crim, Estado_ci, Membros, Respon1, CPFResp1, Respon2, CPFResp2, Contato) VALUES (?,?,?,?,?,?,?,?,?)", (IDfamilia_adotiva,ficha_crim,estado_ci,membros,respon1,cpfResp1,respon2,cpfResp2,contato)))
        self.conn.commit()

        messagebox.showinfo('A familia foi cadastrada com sucesso !')
        self.janela.familia_adotiva.destroy()

    def cadastrar_adocao(self):
        idadocao = self.idadocao.entry.get()
        data = self.data.entry.get()
        observacoes = self.obsv_entry.get()
        crianca_id = self.crianca_id_entry.get()
        familia_adotiva_id= self.familiaadot_id_entry.get()


        self.cursor.execute(("INSERT INTO Adocao(IDAdocao,data,observacoes,crianca_id,familia_adotiva_id) VALUES(?,?,?,?,?)", (idadocao,data,observacoes,crianca_id,familia_adotiva_id)))
    def consultar(self):
        self.cursor.execute("SELECT Nome_Crianca, CPF, RG, IDCrianca FROM Crianca")
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
