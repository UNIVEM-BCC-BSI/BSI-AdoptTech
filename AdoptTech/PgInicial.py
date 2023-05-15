import tkinter as tk
from tkinter import ttk, messagebox

def cadastrar():
    nome = nome_entry.get()
    idade = idade_entry.get()
    genero = genero_entry.get()
    criancas_disponiveis.append((nome, idade, genero))
    messagebox.showinfo('Cadastro', f'{nome} foi cadastrada com sucesso para adoção!')

def consultar():
    if len(criancas_disponiveis) == 0:
        messagebox.showinfo('Consulta', 'Não há crianças cadastradas para adoção.')
    else:
        info = 'As seguintes crianças estão disponíveis para adoção:\n'
        for nome, idade, genero in criancas_disponiveis:
            info += f'- {nome}, {idade} anos, {genero}\n'
        messagebox.showinfo('Consulta', info)

def sobre():
    messagebox.showinfo('Sobre', 'O AdoptTech tem como objetivo ajudar a encontrar lares para crianças.')

def sair():
    window.destroy()

def abrir_aba_cadastro():
    notebook.select(1)

def realizar_cadastro():
    nome = nome_entry.get()
    idade = idade_entry.get()
    genero = genero_entry.get()
    criancas_disponiveis.append((nome, idade, genero))
    messagebox.showinfo('Cadastro', f'{nome} foi cadastrada com sucesso para adoção!')

criancas_disponiveis = []

window = tk.Tk()
window.title('AdoptTech')
window.geometry('400x300')

titulo_label = tk.Label(window, text='Bem-vindo ao AdoptTech!', font=('Arial', 16))
titulo_label.pack(pady=10)

notebook = ttk.Notebook(window)
notebook.pack()

opcao_frame = tk.Frame(notebook)
cadastro_frame = tk.Frame(notebook)

notebook.add(opcao_frame, text='Opções')
notebook.add(cadastro_frame, text='Cadastro')

escolha_label = tk.Label(opcao_frame, text='Escolha uma opção:')
escolha_label.pack(pady=5)

cadastro_button = tk.Button(opcao_frame, text='Cadastrar', command=abrir_aba_cadastro)
cadastro_button.pack(pady=5)

consulta_button = tk.Button(opcao_frame, text='Consultar', command=consultar)
consulta_button.pack(pady=5)

sobre_button = tk.Button(opcao_frame, text='Sobre', command=sobre)
sobre_button.pack(pady=5)

sair_button = tk.Button(opcao_frame, text='Sair', command=sair)
sair_button.pack(pady=5)

nome_label = tk.Label(cadastro_frame, text='Nome:')
nome_label.pack(pady=5)

nome_entry = tk.Entry(cadastro_frame)
nome_entry.pack(pady=5)

idade_label = tk.Label(cadastro_frame, text='Idade:')
idade_label.pack(pady=5)

idade_entry = tk.Entry(cadastro_frame)
idade_entry.pack(pady=5)

genero_label = tk.Label(cadastro_frame, text='Gênero:')
genero_label.pack(pady=5)

genero_entry = tk.Entry(cadastro_frame)
genero_entry.pack(pady=5)

realizar_button = tk.Button(cadastro_frame, text='Realizar Cadastro', command=realizar_cadastro)
realizar_button.pack(pady=5)

window.mainloop()