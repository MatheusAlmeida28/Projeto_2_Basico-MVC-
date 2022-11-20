from controller import Controller_cadastro, Controller_login
while True:
    print("========== [MENU] ==========")
    decidir = int(input('Digite 1 para cadastrar\nDigite 2 para Logar\nDigite 3 para sair\n'))

    if decidir == 1:
        nome = input('Digite seu nome: ').strip()
        email = input('Digite seu email: ').strip()
        senha = input('Digite sua senha: ').strip()
        resultado = Controller_cadastro.cadastrar(nome, email, senha)

        if resultado == 2:
            print("Tamanho do nome digitado inválido")
        elif resultado == 3:
            print("Email maior que 200 caracteres")
        elif resultado == 4:
            print("Senha Fraca.Digite uma senha maior que 6 digitos")
        elif resultado == 5:
            print("Email já cadastrado")
        elif resultado == 6:
            print("Erro interno do sistema")
        elif resultado == 1:
            print("Cadastro realizado com sucesso")
    elif decidir == 2:
        email = input('Digite seu email: ').strip()
        senha = input('Digite sua senha: ').strip()
        resultado = Controller_login.login(email, senha)
        if not resultado:
            print("Email ou senha inválidos")
        else:
            print(resultado)
    else:
        break