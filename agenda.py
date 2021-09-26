AGENDA = {}

AGENDA['guilherme'] = {
    'telefone' : '992334455',
    'email' : 'guilherme@gmail.com',
    'endereco' : 'Av, 1',
}

AGENDA['maria'] = {
    'telefone' : '992333345',
    'email' : 'maria@gmail.com',
    'endereco' : 'Av, 2',
}

def mostrar_contato():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    if contato in AGENDA:
        nome_contato = AGENDA[contato]
        print(f'Nome: {contato.title()}')
        print(f'Telefone: {nome_contato["telefone"]}\n'
              f'Email: {nome_contato["email"]}\n'
              f'Endereço: {nome_contato["endereco"]}\n'
              f'\n --------------------------------------------------')
    else:
        print(f'Contato "{contato.title()}" não existe.')


def incluir_editar_contato(contato, telefone = '', email = '', endereco = ''):
    if contato in AGENDA:
        print(f'>>>>>>>>>> Contato "{contato.title()}" editado com sucesso.\n')
    else:
        print(f'>>>>>>>>>> Contato "{contato.title()}" adicionado com sucesso.\n')
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }

def excluir_contato(contato):
    if contato in AGENDA:
        del AGENDA[contato]
        print(f'>>>>>>>Contato "{contato.title()}" excluido com sucesso.\n')
    else:
        print(f'>>>>>>>Contato "{contato.title()}" n existe.')


def imprimir_menu():
    print('1- Mostrar todos contatos')
    print('2- Buscar contato')
    print('3- Incluir contato')
    print('4- Editar contato')
    print('5- Deletar contato')
    print('6- Imprimir menu')
    print('0- Fechar agenda\n')


def coletar_dados():
    #Solicita informação do contato
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço:')
    return telefone, email, endereco


imprimir_menu()

while True:
    opcao = input('Digite uma das opçôes: ')

    if opcao == '1':
        mostrar_contato()
    elif opcao == '2':
        contato = input('Digite nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite nome do contato que deseja adicionar: ')
        if contato in AGENDA:
            print(f'Contato "{contato.title()}" ja existente.\n')
        else:
            dados = coletar_dados()
            incluir_editar_contato(contato, dados[0], dados[1], dados[2])
    elif opcao == '4':
        contato = input('Digite nome do contato que deseja editar: ')
        if contato in AGENDA:
            dados = list(coletar_dados())
            incluir_editar_contato(contato, dados[0], dados[1], dados[2])
        else:
            print(f'Contato "{contato.title()}" não existe.\n')
    elif opcao == '5':
        contato = input('Digite nome do contato que deseja deletar: ')
        excluir_contato(contato)
    elif opcao == '6':
        imprimir_menu()
    elif opcao == '0':
        print('Saindo....')
        break
    else:
        print('Opção invalida\n')

