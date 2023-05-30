import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.criancas_disponiveis = []
        self.title('AdoptTech')
        self.geometry('1180x610')
        self.resizable(width=False, height=False)
        self.configure(bg="#6598e4")


        #image = Image.open('images/AdoptTech.png')
        #photo = ImageTk.PhotoImage(image)
        titulo_label = tk.Label(self, text='A', bg="#6598e4")
        #titulo_label.image = photo
        #titulo_label.pack(pady=0)

        opcao_frame = tk.Frame(self, bg="#6598e4")
        opcao_frame.pack(pady=10)

        escolha_label = tk.Label(opcao_frame, text='Escolha uma opção:', bg="#6598e4", font=('Quicksand', 20))
        escolha_label.pack(pady=10)

        image = Image.open('images/CADASTRO.png')
        photo = ImageTk.PhotoImage(image)
        cadastro_button = tk.Button(image=photo, command=self.abrir_janela_cadastro, bg="#6598e4")
        cadastro_button.image = photo
        cadastro_button.pack(pady=20)
        cadastro_button.place(x=200, y=140)

        image = Image.open('images/CONSULTA.png')
        photo = ImageTk.PhotoImage(image)
        consulta_button = tk.Button(image=photo, command=self.abrir_janela_consulta, bg="#6598e4")
        consulta_button.image = photo
        consulta_button.pack(pady=10)
        consulta_button.place(x=200, y=350)

        image = Image.open('images/SOBRE.png')
        photo = ImageTk.PhotoImage(image)
        sobre_button = tk.Button(image=photo, command=self.sobre, bg="#6598e4")
        sobre_button.image = photo
        sobre_button.pack(pady=10)
        sobre_button.place(x=700, y=140)

        image = Image.open('images/SAIR.png')
        photo = ImageTk.PhotoImage(image)
        sair_button = tk.Button(image=photo, command=self.sair, bg="#6598e4")
        sair_button.image = photo
        sair_button.pack(pady=10)
        sair_button.place(x=700, y=350)


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

    def abrir_janela_consulta(self):
        self.janela_consulta = tk.Toplevel(self)
        self.janela_consulta.title('Consulta')
        self.janela_consulta.geometry('1180x550')
        self.janela_consulta.resizable(width=False, height=False)
        self.janela_consulta.configure(bg='#6598e4')

        image = Image.open('images/CRIANÇA.png')
        photo = ImageTk.PhotoImage(image)
        consultar_crianca_button = tk.Button(self.janela_consulta, image=photo, command=self.consultar_crianca)
        consultar_crianca_button.image = photo
        consultar_crianca_button.pack(pady=20)
        consultar_crianca_button.place(x=432, y=320)


        image = Image.open('images/ADOÇÃO.png')
        photo = ImageTk.PhotoImage(image)
        consultar_adocao_button = tk.Button(self.janela_consulta, image=photo, command=self.consultar_adocao)
        consultar_adocao_button.image = photo
        consultar_adocao_button.pack(pady=10)
        consultar_adocao_button.place(x=120, y=210)

        image = Image.open('images/FAMÍLIAS ADOTIVAS.png')
        photo = ImageTk.PhotoImage(image)
        consultar_familiaadot_button = tk.Button(self.janela_consulta, image=photo, command=self.consultar_familiaadotiva)
        consultar_familiaadot_button.image = photo
        consultar_familiaadot_button.pack(pady=10)
        consultar_familiaadot_button.place(x=740, y=80)

        image = Image.open('images/FAMÍLIAS BIOLOGICAS.png')
        photo = ImageTk.PhotoImage(image)
        consultar_familiabio_button = tk.Button(self.janela_consulta, image = photo,command=self.consultar_familiabio)
        consultar_familiabio_button.image =photo
        consultar_familiabio_button.pack(pady=10)
        consultar_familiabio_button.place(x=740, y=210)

        image = Image.open('images/ABANDONO.png')
        photo = ImageTk.PhotoImage(image)
        consultar_abandono_button = tk.Button(self.janela_consulta, image=photo, command=self.consultar_abandono)
        consultar_abandono_button.image = photo
        consultar_abandono_button.pack(pady=10)
        consultar_abandono_button.place(x=120, y=80)

        voltar_button = tk.Button(self.janela_consulta, text='Voltar para a página anterior', command=self.janela_consulta.destroy)
        voltar_button.pack(pady=10)
        voltar_button.place(x=510, y=450)

    def abrir_janela_cadastro(self):
        self.janela_cadastro = tk.Toplevel(self)
        self.janela_cadastro.title('Cadastro')
        self.janela_cadastro.geometry('1180x550')
        self.janela_cadastro.resizable(width=False, height=False)
        self.janela_cadastro.configure(bg="#6598e4")


        image = Image.open('images/CADASTRO CRIANÇA.png')
        photo = ImageTk.PhotoImage(image)
        cadastrar_crianca_button = tk.Button(self.janela_cadastro, image=photo, command=self.abrir_janela_crianca)
        cadastrar_crianca_button.image = photo
        cadastrar_crianca_button.pack(pady=25, fill='y')
        cadastrar_crianca_button.place(x=432, y=320)

        image = Image.open('images/CADASTRAR ADOÇÃO.png')
        photo = ImageTk.PhotoImage(image)
        cadastrar_adocao_button = tk.Button(self.janela_cadastro, image=photo, command=self.abrir_janela_adocao)
        cadastrar_adocao_button.image = photo
        cadastrar_adocao_button.pack(pady=25, fill='y')
        cadastrar_adocao_button.place(x=120, y=210)

        image = Image.open('images/FAMILIA ADOTIVA.png')
        photo = ImageTk.PhotoImage(image)
        cadastrar_familiaadot_button = tk.Button(self.janela_cadastro, image=photo, command=self.abrir_janela_familiaadot)
        cadastrar_familiaadot_button.image = photo
        cadastrar_familiaadot_button.pack(pady=25, fill='y')
        cadastrar_familiaadot_button.place(x=740, y=80)

        image = Image.open('images/FAMILIA BIOLOGICA.png')
        photo = ImageTk.PhotoImage(image)
        cadastrar_familiabio_button = tk.Button(self.janela_cadastro, image=photo, command=self.abrir_janela_familiabio)
        cadastrar_familiabio_button.image = photo
        cadastrar_familiabio_button.pack(pady=25, fill='y')
        cadastrar_familiabio_button.place(x=740, y=210)

        image = Image.open('images/CADASTRO ABANDONO.png')
        photo = ImageTk.PhotoImage(image)
        cadastrar_abandono_button = tk.Button(self.janela_cadastro, image=photo, command=self.abrir_janela_abandono)
        cadastrar_abandono_button.image = photo
        cadastrar_abandono_button.pack(pady=25, fill='y')
        cadastrar_abandono_button.place(x=120, y=80)

        voltar_button = tk.Button(self.janela_cadastro, text='Voltar para a página anterior', command=self.janela_cadastro.destroy)
        voltar_button.pack(pady=10)
        voltar_button.place(x=510, y=450)
    def abrir_janela_familiabio(self):
        self.janela_familiabio = tk.Toplevel(self)
        self.janela_familiabio.title('Cadastrar Família Biológica')
        self.janela_familiabio.geometry('1280x610')
        self.janela_familiabio.resizable(width=False, height=False)
        self.janela_familiabio.configure(bg='#6598e4')

        contact_label = tk.Label(self.janela_familiabio, text='Contato', bg='#6598e4', font=('Roboto', 17))
        contact_label.pack(pady=5)
        contact_label.place(x=80, y=35)

        self.contact_entry = tk.Entry(self.janela_familiabio, width=30)
        self.contact_entry.pack(pady=5)
        self.contact_entry.place(x=80, y=70)

        respons1_label = tk.Label(self.janela_familiabio, text='Responsável 1', bg='#6598e4', font=('Roboto', 17))
        respons1_label.pack(pady=5)
        respons1_label.place(x=80, y=150)


        self.respons1_entry = tk.Entry(self.janela_familiabio, width=30)
        self.respons1_entry.pack(pady=5)
        self.respons1_entry.place(x=80, y=185)



        cpfrs1_label = tk.Label(self.janela_familiabio, text='CPF Responsável 1', bg='#6598e4', font=('Roboto', 17))
        cpfrs1_label.pack(pady=5)
        cpfrs1_label.place(x=370, y=150)

        self.cpfrs1_entry = tk.Entry(self.janela_familiabio, width=30)
        self.cpfrs1_entry.pack(pady=5)
        self.cpfrs1_entry.place(x=370, y=185)

        respons2_label = tk.Label(self.janela_familiabio, text='Responsável 2', bg='#6598e4', font=('Roboto', 17))
        respons2_label.pack(pady=5)
        respons2_label.place(x=610, y=150)

        self.respons2_entry = tk.Entry(self.janela_familiabio, width=30)
        self.respons2_entry.pack(pady=5)
        self.respons2_entry.place(x=610, y=185)

        cpfrs2_label = tk.Label(self.janela_familiabio, text='CPF Responsável 2', bg='#6598e4', font=('Roboto', 17))
        cpfrs2_label.pack(pady=5)
        cpfrs2_label.place(x=930, y=150)

        self.cpfrs2_entry = tk.Entry(self.janela_familiabio, width=30)
        self.cpfrs2_entry.pack(pady=5)
        self.cpfrs2_entry.place(x=930, y=185)

        rua_label = tk.Label(self.janela_familiabio, text='Rua', bg='#6598e4', font=('Roboto', 17))
        rua_label.pack(pady=5)
        rua_label.place(x=370, y=35)


        self.rua_entry = tk.Entry(self.janela_familiabio, width=30)
        self.rua_entry.pack(pady=5)
        self.rua_entry.place(x=370, y=70)

        bairro_label = tk.Label(self.janela_familiabio, text='Bairro', bg='#6598e4', font=('Roboto', 17))
        bairro_label.pack(pady=5)
        bairro_label.place(x=610, y=35)

        self.bairro_entry = tk.Entry(self.janela_familiabio, width=30)
        self.bairro_entry.pack(pady=5)
        self.bairro_entry.place(x=610, y=70)

        numero_label = tk.Label(self.janela_familiabio, text='Número', bg='#6598e4', font=('Roboto', 17))
        numero_label.pack(pady=5)
        numero_label.place(x=930, y=35)

        self.numero_entry = tk.Entry(self.janela_familiabio, width=30)
        self.numero_entry.pack(pady=5)
        self.numero_entry.place(x=930, y=70)

        image = Image.open('images/REALIZAR CADASTRO(VERDE).png')
        photo = ImageTk.PhotoImage(image)
        realizar_button = tk.Button(self.janela_familiabio, command=self.cadastrar_familia_biologica, image=photo, bg='#6598e4')
        realizar_button.image = photo
        realizar_button.pack(pady=10)
        realizar_button.place(x=480, y=300)

        #remover_button = tk.Button(self.janela_familiabio, command=self.deletar_familiabio, text='Deletar Familia Biologica', font=('Quicksand', 30), bg='#6598e4')
        #remover_button.pack(pady=10, side='bottom')

        voltar_button = tk.Button(self.janela_familiabio, text='Voltar para a página anterior', command=self.janela_familiabio.destroy)
        voltar_button.pack(pady=10)
        voltar_button.place(x=550, y=400)

        self.janela_familiabio.bind('<Return>', lambda event: realizar_button.invoke())

    def abrir_janela_adocao(self):
        self.janela_adocao = tk.Toplevel(self)
        self.janela_adocao.title('Cadastrar Adoção')
        self.janela_adocao.geometry('1280x960')
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

        image = Image.open('images/REALIZAR CADASTRO(VERDE).png')
        photo = ImageTk.PhotoImage(image)
        realizar_button = tk.Button(self.janela_adocao, command=self.cadastrar_adocao, image=photo, bg='#6598e4')
        realizar_button.image = photo
        realizar_button.pack(pady=10)

        remover_button = tk.Button(self.janela_adocao, command=self.deletar_adocao, text='Deletar Adoção', font=('Quicksand', 30), bg='#6598e4')
        remover_button.pack(pady=10, side='bottom')

        voltar_button = tk.Button(self.janela_adocao, text='Voltar para a página anterior', command=self.janela_adocao.destroy)
        voltar_button.pack(pady=10)

        self.janela_adocao.bind('<Return>', lambda event: realizar_button.invoke())

    def abrir_janela_crianca(self):
        self.janela_crianca = tk.Toplevel(self)
        self.janela_crianca.title('Cadastrar Criança')
        self.janela_crianca.geometry('1280x960')
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

        image = Image.open('images/REALIZAR CADASTRO(VERDE).png')
        photo = ImageTk.PhotoImage(image)
        realizar_button = tk.Button(self.janela_crianca, command=self.cadastrar_criança, image=photo, bg='#6598e4')
        realizar_button.image = photo
        realizar_button.pack(pady=15)

        remover_button = tk.Button(self.janela_crianca, command=self.deletar_crianca, text='Deletar Criança', font=('Quicksand', 30), bg='#6598e4')
        remover_button.pack(pady=10, side='bottom')

        voltar_button = tk.Button(self.janela_crianca, text='Voltar para a página anterior', command=self.janela_crianca.destroy)
        voltar_button.pack(pady=10)

        self.janela_crianca.bind('<Return>', lambda event: realizar_button.invoke())

    def abrir_janela_abandono(self):
        self.janela_abandono = tk.Toplevel(self)
        self.janela_abandono.title('Cadastrar Abandono')
        self.janela_abandono.geometry('1280x960')
        self.janela_abandono.configure(bg='#6598e4')

        data_label = tk.Label(self.janela_abandono, text='Data:', bg='#6598e4', font=('Roboto', 17))
        data_label.pack(pady=7)
        data_label.place(x=200, y=35)

        self.data_entry = tk.Entry(self.janela_abandono, width=40)
        self.data_entry.pack(pady=7)
        self.data_entry.place(x=200, y=70)

        observacoes_label = tk.Label(self.janela_abandono, text='Observações:', bg='#6598e4', font=('Roboto', 17))
        observacoes_label.pack(pady=7)
        observacoes_label.place(x=800, y=35)

        self.observacoes_entry = tk.Entry(self.janela_abandono, width=40)
        self.observacoes_entry.pack(pady=7)
        self.observacoes_entry.place(x=800, y=70)

        crianc_id_label = tk.Label(self.janela_abandono, text='ID da Criança', bg='#6598e4', font=('Roboto', 17))
        crianc_id_label.pack(pady=7)

        self.crianc_id_entry = tk.Entry(self.janela_abandono, width=40)
        self.crianc_id_entry.pack(pady=7)

        familiabio_id_label = tk.Label(self.janela_abandono, text='ID da Familia Biológica', bg='#6598e4', font=('Quicksand', 20))
        familiabio_id_label.pack(pady=7)

        self.familiabio_id_entry = tk.Entry(self.janela_abandono, width=40)
        self.familiabio_id_entry.pack(pady=7)

        image = Image.open('images/REALIZAR CADASTRO(VERDE).png')
        photo = ImageTk.PhotoImage(image)
        realizar_button = tk.Button(self.janela_abandono, command=self.cadastrar_abandono, image=photo, bg='#6598e4')
        realizar_button.image = photo
        realizar_button.pack(pady=10)

        remover_button = tk.Button(self.janela_abandono, command=self.deletar_abandono, text='Deletar Abandono', font=('Quicksand', 30), bg='#6598e4')
        remover_button.pack(pady=10, side='bottom')

        voltar_button = tk.Button(self.janela_abandono, text='Voltar para a página anterior', command=self.janela_abandono.destroy)
        voltar_button.pack(pady=10)


        self.janela_abandono.bind('<Return>', lambda event: realizar_button.invoke())



    def abrir_janela_familiaadot(self):
        self.janela_familiaadot = tk.Toplevel(self)
        self.janela_familiaadot.title('Cadastrar Familia Adotiva')
        self.janela_familiaadot.geometry('1280x610')
        self.janela_familiaadot.resizable(width=False, height=False)
        self.janela_familiaadot.configure(bg='#6598e4')

        ficha_crim_label = tk.Label(self.janela_familiaadot, text="Ficha Criminal", bg='#6598e4', font=('Roboto', 17))
        ficha_crim_label.pack(pady=5)
        ficha_crim_label.place(x=80, y=35)

        self.ficha_crim_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.ficha_crim_entry.pack(pady=5)
        self.ficha_crim_entry.place(x=80, y=70)

        estado_civil_label = tk.Label(self.janela_familiaadot, text="Estado Civil", bg='#6598e4', font=('Roboto', 17))
        estado_civil_label.pack(pady=5)
        estado_civil_label.place(x=370, y=35)

        self.estado_civil_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.estado_civil_entry.pack(pady=5)
        self.estado_civil_entry.place(x=370, y=70)

        membros_label = tk.Label(self.janela_familiaadot, text="Membros", bg='#6598e4', font=('Roboto', 17))
        membros_label.pack(pady=5)
        membros_label.place(x=610, y=35)

        self.membros_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.membros_entry.pack(pady=5)
        self.membros_entry.place(x=610, y=70)

        respon1_label = tk.Label(self.janela_familiaadot, text="Responsável 1", bg='#6598e4', font=('Roboto', 17))
        respon1_label.pack(pady=5)
        respon1_label.place(x=930, y=35)

        self.respon1_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.respon1_entry.pack(pady=5)
        self.respon1_entry.place(x=930, y=70)


        cpfr1_label = tk.Label(self.janela_familiaadot, text="CPF Responsável 1", bg='#6598e4', font=('Roboto', 17))
        cpfr1_label.pack(pady=5)
        cpfr1_label.place(x=80, y=150)

        self.cpfr1_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.cpfr1_entry.pack(pady=5)
        self.cpfr1_entry.place(x=80, y=185)

        respon2_label = tk.Label(self.janela_familiaadot, text="Responsável 2", bg='#6598e4', font=('Roboto', 17))
        respon2_label.pack(pady=5)
        respon2_label.place(x=370, y=150)

        self.respon2_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.respon2_entry.pack(pady=5)
        self.respon2_entry.place(x=370, y=185)

        cpfr2_label = tk.Label(self.janela_familiaadot, text="CPF Responsável 2", bg='#6598e4', font=('Roboto', 17))
        cpfr2_label.pack(pady=5)
        cpfr2_label.place(x=610, y=150)

        self.cpfr2_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.cpfr2_entry.pack(pady=5)
        self.cpfr2_entry.place(x=610, y=185)

        contato_label = tk.Label(self.janela_familiaadot, text='Contato', bg='#6598e4', font=('Roboto', 17))
        contato_label.pack(pady=5)
        contato_label.place(x=930, y=150)

        self.contato_entry = tk.Entry(self.janela_familiaadot, width=30)
        self.contato_entry.pack(pady=5)
        self.contato_entry.place(x=930, y=185)

        image = Image.open('images/REALIZAR CADASTRO(VERDE).png')
        photo = ImageTk.PhotoImage(image)
        realizar_button = tk.Button(self.janela_familiaadot, command=self.cadastrar_familia_adotiva, image=photo, bg='#6598e4')
        realizar_button.image = photo
        realizar_button.pack(pady=10)
        realizar_button.place(x=480, y=300)

        #remover_button = tk.Button(self.janela_familiaadot, command=self.deletar_familiaadot, text='Deletar Familia Adotiva', font=('Quicksand', 30), bg='#6598e4')
        #remover_button.pack(pady=10, side='bottom')

        voltar_button = tk.Button(self.janela_familiaadot, text='Voltar para a página anterior', command=self.janela_familiaadot.destroy)
        voltar_button.pack(pady=10)
        voltar_button.place(x=550, y=400)

        self.janela_familiaadot.bind('<Return>', lambda event: realizar_button.invoke())

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

        messagebox.showinfo('O registro de Abandono foi feito com sucesso!')
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

        messagebox.showinfo('A família foi cadastrada com sucesso!')
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

        messagebox.showinfo('A familia foi cadastrada com sucesso!')
        self.janela_familia_adotiva.destroy()

    def cadastrar_adocao(self):
        idadocao = self.idadocao.entry.get()
        data = self.data.entry.get()
        observacoes = self.obsv_entry.get()
        crianca_id = self.crianca_id_entry.get()
        familia_adotiva_id= self.familiaadot_id_entry.get()


        self.cursor.execute(("INSERT INTO Adocao(IDAdocao,data,observacoes,crianca_id,familia_adotiva_id) VALUES(?,?,?,?,?)", (idadocao,data,observacoes,crianca_id,familia_adotiva_id)))
        self.conn.commit()

        messagebox.showinfo('O registro de Adoção foi realizado com sucesso!')
        self.janela_cadastrar_adocao.destroy()


    def consultar_abandono(self):
        self.cursor.execute("SELECT Data,Observacoes,Crianca_ID,Familia_biologica_ID FROM Abandono ")
        resu = self.cursor.fetchall()

        if len(resu) == 0:
            messagebox.showinfo('Consulta', 'Não existem abandonos cadastrados.')
        else:
            janela_consulta_abandono = tk.Toplevel()
            janela_consulta_abandono.title('Consulta')
            janela_consulta_abandono.geometry('300x200')

            lis_label = tk.Label(janela_consulta_abandono, text='Abandonos cadastrados')
            lis_label.pack(pady=5)

            lis_text = tk.Text(janela_consulta_abandono)
            lis_text.pack()

            for data,observacoes,crianca_id,familia_biologica_id in sorted(resu):
                lis_text.insert(tk.END, f'Data {data}\nObservações {observacoes}\nID da Criança {crianca_id}\nID da Familia Biológica {familia_biologica_id}\n\n')
            janela_consulta_abandono.mainloop()

    def consultar_familiaadotiva(self):
        self.cursor.execute("SELECT IDFamilia_adotiva, Ficha_crim, Estado_ci, Membros, Respon1, CPFResp1, Respon2, CPFResp2, Contato FROM Familia_adotiva")
        resular = self.cursor.fetchall()

        if len(resular) == 0:
            messagebox.showinfo('Consulta', 'Não existem famílias adotivas cadastradas')
        else:
            janela_consulta_familiadotiva = tk.Toplevel()
            janela_consulta_familiadotiva.title('Consulta - Família Adotiva')
            janela_consulta_familiadotiva.geometry('400x300')

            lit_label = tk.Label(janela_consulta_familiadotiva, text='Familias Adotivas cadastradas: ')
            lit_label.pack(pady=5)

            lit_text = tk.Text(janela_consulta_familiadotiva)
            lit_text.pack()

            for IDfamilia_adotiva,ficha_crim,estado_ci,membros,respon1,cpfResp1,respon2,cpfResp2,contato in sorted(resular):
                lit_text.insert(tk.END, f'ID Familia Adotiva {IDfamilia_adotiva}\nFicha Criminal {ficha_crim}\nEstado Civil {estado_ci}\nMembros {membros}\nResponsável 1 {respon1}\nCPF Responsável 1 {cpfResp1}\nResponsável 2 {respon2}\nCPF Responsável 2 {cpfResp2}\nContato {contato}\n\n')
            janela_consulta_familiadotiva.mainloop()

    def consultar_adocao(self):
        self.cursor.execute("SELECT Data, Observacoes, Crianca_ID, Familia_adotiva_ID FROM Adocao")
        result = self.cursor.fetchall()

        if len(result) == 0:
            messagebox.showinfo('Consulta', 'Não existem adoções cadastradas.')
        else:
            janela_consulta_adocao = tk.Toplevel()
            janela_consulta_adocao.title('Consulta')
            janela_consulta_adocao.geometry('300x200')

            list_label = tk.Label(janela_consulta_adocao, text='Adoções cadastradas')
            list_label.pack(pady=5)

            list_text = tk.Text(janela_consulta_adocao)
            list_text.pack()

            for idadocao, data, observacoes, crianca_id, familia_adotiva_id in sorted(result):
                list_text.insert(tk.END, f'ID Adoção {idadocao}\nData {data}\nObservações {observacoes}\nID Criança {crianca_id}\nID Familia Adotiva {familia_adotiva_id}\n\n')

            janela_consulta_adocao.mainloop()

    def consultar_familiabio(self):
        self.cursor.execute("SELECT IDFamilia_biologica, Contato, Respon1, CPFRespon1, Respon2, CPFRespon2, Rua, Bairro, Numero FROM Familia_biologica")
        resul = self.cursor.fetchall()

        if len(resul) == 0:
            messagebox.showinfo('Consulta', 'Não há famílias biologicas cadastradas')
        else:
            janela_consulta_familiabio = tk.Toplevel()
            janela_consulta_familiabio.title('Consulta - Família Biológica')
            janela_consulta_familiabio.geometry('400x300')

            lsita_label = tk.Label(janela_consulta_familiabio, text='Famílias biolgoicas')
            lsita_label.pack(pady=5)

            lsita_text = tk.Text(janela_consulta_familiabio)
            lsita_text.pack()

            for IDfamilia_biologica, contato, respon1, cpfrespon1, respon2, cpfrespon2, rua, bairro, numero in sorted(resul):
                lsita_text.insert(tk.END, f'ID Familia Biologica {IDfamilia_biologica}\nContato {contato}\nResponsável 1 {respon1}\nCPF Responsável 1 {cpfrespon1}\nResponsável 2 {respon2}\nCPF Responsável 2 {cpfrespon2}\nRua {rua}\nBairro {bairro}\nNúmero {numero}\n\n')

            janela_consulta_familiabio.mainloop()

    def consultar_crianca(self):
        self.cursor.execute("SELECT Nome_Crianca, CPF, RG, IDCrianca FROM Crianca")
        resultados = self.cursor.fetchall()

        if len(resultados) == 0:
            messagebox.showinfo('Consulta', 'Não há crianças cadastradas para adoção.')
        else:
            janela_consulta_crianca = tk.Toplevel()
            janela_consulta_crianca.title('Consulta')
            janela_consulta_crianca.geometry('300x200')

            lista_label = tk.Label(janela_consulta_crianca, text='Crianças cadastradas:')
            lista_label.pack(pady=5)

            lista_text = tk.Text(janela_consulta_crianca)
            lista_text.pack()

            for nome_crianca, cpf, rg, id_crianca in sorted(resultados):
                lista_text.insert(tk.END, f'Nome: {nome_crianca}\nCPF: {cpf}\nRG: {rg}\nID: {id_crianca}\n\n')

            janela_consulta_crianca.mainloop()

    def deletar_abandono(self):
        self.janela_deletar_abandono = tk.Toplevel(self)
        self.janela_deletar_abandono.title('Deletar registro de Abandono')
        self.janela_deletar_abandono.geometry('1024x768')
        self.janela_deletar_abandono.configure(bg='#6598e4')

        id_label = tk.Label(self.janela_deletar_abandono, text='ID do Abandono:', bg='#6598e4', font=('Quicksand', 20))
        id_label.pack(pady=7)

        self.id_entry = tk.Entry(self.janela_deletar_abandono, width=40)
        self.id_entry.pack(pady=7)

        deletar_button = tk.Button(self.janela_deletar_abandono, text='Deletar', command=self.confirmar_deletar_abandono)
        deletar_button.pack(pady=10)

    def confirmar_deletar_abandono(self):
        idabandono = self.id_entry.get()

        if idabandono == '':
            messagebox.showerror('Erro', 'Por favor, insira o ID do Abandono.')
        else:
            confirmar = messagebox.askyesno('Confirmar Deleção', 'Tem certeza que deseja deletar esse registro de Abandono?')

            if confirmar:
                try:
                    self.cursor.execute('DELETE FROM Abandono WHERE IDAbandono = ?', (idabandono,))
                    self.conn.commit()
                    messagebox.showinfo('Sucesso', 'Abandono deletado com sucesso.')
                except sqlite3.Error as e:
                    messagebox.showerror('Erro', 'Ocorreu um erro ao deletar o registro: ' + str(e))
            else:
                messagebox.showinfo('Cancelado', 'Deleção cancelada.')

        self.janela_deletar_abandono.destroy()



    def deletar_adocao(self):
        self.janela_deletar_adocao = tk.Toplevel(self)
        self.janela_deletar_adocao.title('Deletar registro de Adoção')
        self.janela_deletar_adocao.geometry('1024x768')
        self.janela_deletar_adocao.configure(bg='#6598e4')

        id_label = tk.Label(self.janela_deletar_adocao, text='ID da Adoção:', bg='#6598e4', font=('Quicksand', 20))
        id_label.pack(pady=7)

        self.id_entry = tk.Entry(self.janela_deletar_adocao, width=40)
        self.id_entry.pack(pady=7)

        deletar_button = tk.Button(self.janela_deletar_adocao, text='Deletar', command=self.confirmar_deletar_adocao)
        deletar_button.pack(pady=10)

    def confirmar_deletar_adocao(self):
        idadocao = self.id_entry.get()

        if idadocao == '':
            messagebox.showerror('Erro', 'Por favor, insira o ID da Adoção.')
        else:
            confirmar = messagebox.askyesno('Confirmar Deleção', 'Tem certeza que deseja deletar esse registro de Adoção?')

            if confirmar:
                try:
                    self.cursor.execute('DELETE FROM Adocao WHERE idadocao = ?', (idadocao,))
                    self.conn.commit()
                    messagebox.showinfo('Sucesso', 'Adoção deletada com sucesso.')
                except sqlite3.Error as e:
                    messagebox.showerror('Erro', 'Ocorreu um erro ao deletar o registro: ' + str(e))
            else:
                messagebox.showinfo('Cancelado', 'Deleção cancelada.')

        self.janela_deletar_adocao.destroy()
    def deletar_familiabio(self):
        self.janela_deletar_familiabio = tk.Toplevel(self)
        self.janela_deletar_familiabio.title('Deletar Familia Biológica')
        self.janela_deletar_familiabio.geometry('1024x768')
        self.janela_deletar_familiabio.configure(bg='#6598e4')

        id_label = tk.Label(self.janela_deletar_familiabio, text='ID da Familia Biologica:', bg='#6598e4', font=('Quicksand', 20))
        id_label.pack(pady=7)

        self.id_entry = tk.Entry(self.janela_deletar_familiabio, width=40)
        self.id_entry.pack(pady=7)

        deletar_button = tk.Button(self.janela_deletar_familiabio, text='Deletar', command=self.confirmar_deletar_familiabio)
        deletar_button.pack(pady=10)

    def confirmar_deletar_familiabio(self):
        IDfamilia_biologica = self.id_entry.get()

        if IDfamilia_biologica == '':
            messagebox.showerror('Erro', 'Por favor, insira o ID da Familia.')
        else:
            confirmar = messagebox.askyesno('Confirmar Deleção', 'Tem certeza que deseja deletar essa Familia?')

            if confirmar:
                try:
                    self.cursor.execute('DELETE FROM Familia_biologica WHERE IDFamilia_biologica = ?', (IDfamilia_biologica,))
                    self.conn.commit()
                    messagebox.showinfo('Sucesso', 'Familia adotiva deletada com sucesso.')
                except sqlite3.Error as e:
                    messagebox.showerror('Erro', 'Ocorreu um erro ao deletar a Familia: ' + str(e))
            else:
                messagebox.showinfo('Cancelado', 'Deleção cancelada.')

        self.janela_deletar_familiabio.destroy()
    def deletar_familiaadot(self):
        self.janela_deletar_familiaadot = tk.Toplevel(self)
        self.janela_deletar_familiaadot.title('Deletar Familia Adotiva')
        self.janela_deletar_familiaadot.geometry('1024x768')
        self.janela_deletar_familiaadot.configure(bg='#6598e4')

        id_label = tk.Label(self.janela_deletar_familiaadot, text='ID da Familia Adotiva:', bg='#6598e4', font=('Quicksand', 20))
        id_label.pack(pady=7)

        self.id_entry = tk.Entry(self.janela_deletar_familiaadot, width=40)
        self.id_entry.pack(pady=7)

        deletar_button = tk.Button(self.janela_deletar_familiaadot, text='Deletar', command=self.confirmar_deletar_familiaadot)
        deletar_button.pack(pady=10)

    def confirmar_deletar_familiaadot(self):
        IDfamilia_adotiva = self.id_entry.get()

        if IDfamilia_adotiva == '':
            messagebox.showerror('Erro', 'Por favor, insira o ID da Familia.')
        else:
            confirmar = messagebox.askyesno('Confirmar Deleção', 'Tem certeza que deseja deletar essa Familia?')

            if confirmar:
                try:
                    self.cursor.execute('DELETE FROM Familia_adotiva WHERE IDFamilia_adotiva = ?', (IDfamilia_adotiva,))
                    self.conn.commit()
                    messagebox.showinfo('Sucesso', 'Familia adotiva deletada com sucesso.')
                except sqlite3.Error as e:
                    messagebox.showerror('Erro', 'Ocorreu um erro ao deletar a Familia: ' + str(e))
            else:
                messagebox.showinfo('Cancelado', 'Deleção cancelada.')

        self.janela_deletar_familiaadot.destroy()

    def deletar_crianca(self):
        self.janela_deletar_crianca = tk.Toplevel(self)
        self.janela_deletar_crianca.title('Deletar Criança')
        self.janela_deletar_crianca.geometry('1024x768')
        self.janela_deletar_crianca.configure(bg='#6598e4')

        id_label = tk.Label(self.janela_deletar_crianca, text='ID da Criança:', bg='#6598e4', font=('Quicksand', 20))
        id_label.pack(pady=7)

        self.id_entry = tk.Entry(self.janela_deletar_crianca, width=40)
        self.id_entry.pack(pady=7)

        deletar_button = tk.Button(self.janela_deletar_crianca, text='Deletar', command=self.confirmar_deletar_crianca)
        deletar_button.pack(pady=10)

    def confirmar_deletar_crianca(self):
        id_crianca = self.id_entry.get()

        if id_crianca == '':
            messagebox.showerror('Erro', 'Por favor, insira o ID da criança.')
        else:
            confirmar = messagebox.askyesno('Confirmar Deleção', 'Tem certeza que deseja deletar essa criança?')

            if confirmar:
                try:
                    self.cursor.execute('DELETE FROM Crianca WHERE IDCrianca = ?', (id_crianca,))
                    self.conn.commit()
                    messagebox.showinfo('Sucesso', 'Criança deletada com sucesso.')
                except sqlite3.Error as e:
                    messagebox.showerror('Erro', 'Ocorreu um erro ao deletar a criança: ' + str(e))
            else:
                messagebox.showinfo('Cancelado', 'Deleção cancelada.')

        self.janela_deletar_crianca.destroy()

    def sobre(self):
        messagebox.showinfo('Sobre', 'O AdoptTech tem como objetivo ajudar a encontrar lares para crianças.')


    def sair(self):
        self.conn.close()
        self.destroy()

if __name__ == '__main__':
    app = Application()
app.mainloop()
