print('Bem-vindo ao AdoptTech!')

criancas_disponiveis = []
linhas = '=' * 50

while True:
    print(linhas)
    print('Escolha uma opção:')
    print('1 - Cadastrar')
    print('2 - Consultar')
    print('3 - Sobre')
    print('4 - Sair')
    print(linhas)

    opcao = input('Digite o número da opção desejada: ')

    if opcao == '1':
        print(linhas)
        nome = input('Digite o nome da criança: ')
        idade = input('Digite a idade da criança: ')
        genero = input('Digite o gênero da criança (masculino, feminino ou não-binário): ')
        criancas_disponiveis.append((nome, idade, genero))
        print(linhas)
        print(nome + ' foi cadastrada com sucesso para adoção!')
    elif opcao == '2':
        if len(criancas_disponiveis) == 0:
            print(linhas)
            print('Não há crianças cadastradas para adoção.')
        else:
            print(linhas)
            print('As seguintes crianças estão disponíveis para adoção:')
            for nome, idade, genero in criancas_disponiveis:
                print(f'- {nome}, {idade} anos, {genero}')
    elif opcao == '3':
        print(linhas)
        print('O AdoptTech tem como objetivo ajudar a encontrar lares para crianças.')
    elif opcao == '4':
        print(linhas)
        print('Obrigado por usar o AdoptTech. Até a próxima!')
        print(linhas)
        break
    else:
        print('Opção inválida. Tente novamente.')
