import json

AGENDA = {}


def mostrar_contato():
    print('')
    if AGENDA:
        print('>>>>>>>>>>>> Contatos em agenda.')
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>>>>>>>>>> Não existe nenhum contato na agenda.\n')


def buscar_contato(contato):
    print('')
    if contato in AGENDA:
        nome_contato = AGENDA[contato]
        print(f'Nome: {contato.title()}')
        print(f'Telefone: {nome_contato["telefone"]}\n'
              f'Email: {nome_contato["email"]}\n'
              f'Endereço: {nome_contato["endereco"]}\n'
              f'\n --------------------------------------------------')
    else:
        print(f'Contato "{contato.title()}" não existe.')


def incluir_editar_contato(contato, telefone, email, endereco, verifica = '1'):
    if verifica:
        if contato in AGENDA:
            print(f'>>>>>>>>>> Contato "{contato}" editado com sucesso.')
        else:
            print(f'>>>>>>>>>> Contato "{contato}" adicionado com sucesso.')
    else:
        print(f'>>>>>>>>>> Contato "{contato}" Importado com sucesso.')
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print('')


def excluir_contato(contato):
    if contato in AGENDA:
        del AGENDA[contato]
        print(f'>>>>>>> Contato "{contato}" excluido com sucesso.\n')
        salvar()
    else:
        print(f'>>>>>>> Contato "{contato}" n existe.')


def imprimir_menu():
    print('1- Mostrar todos contatos')
    print('2- Buscar contato')
    print('3- Incluir contato')
    print('4- Editar contato')
    print('5- Deletar contato')
    print('6- Exportar Agenda para json')
    print('7- Importar Contatos para json')
    print('0- Fechar agenda\n')


def coletar_dados():
    #Solicita informação do contato
    try:
        telefone = int(input('Digite o telefone: '))
        email = input('Digite o email: ')
        endereco = input('Digite o endereço:')
        return telefone, email, endereco
    except:
        print('Digite telefone corretamente.\n')


def verificador_de_dados():
    #Verificar se os dados do contato estão corretos
    try:
        if dados[1] and dados[2]:
            incluir_editar_contato(contato, dados[0], dados[1], dados[2])
        else:
            print('Informar todos os dados corretamente.\n')
    except:
        print('Informe os dados corretamente\n')


def exportar_agenda(arquivo):
    if arquivo == 'database':
        imprimir = f'Salvando contatos.\nContatos salvos: {len(AGENDA)}'
    else:
        imprimir = f'Agenda exportada com sucesso\nContatos exportado: {len(AGENDA)}'
    arquivo_exportar = f'{arquivo}.json'
    try:
        with open(arquivo_exportar, 'w') as a_obj:
            json.dump(AGENDA, a_obj)
            print(imprimir)
    except Exception as e:
        print('Algum erro ocorreu.')
        print(f'{e}\n')

def importar_contatos(arquivo):
    arquivo_importar = f'{arquivo}.json'
    try:
        with open(arquivo_importar) as a_obj:
            contatos = json.load(a_obj)
            if contatos:
                if contatos == AGENDA:
                    print(f'Agenda ja importada.')
                else:
                    print('Importando contatos.')
                    print(f'Contatos importado: {len(contatos)}')
                    for contato in contatos:
                        informacao_contato = contatos[contato]
                        incluir_editar_contato(contato,
                                               informacao_contato["telefone"],
                                               informacao_contato["email"],
                                               informacao_contato["endereco"],
                                               '')
            else:
                print('Arquivo vazio.\n')
    except FileNotFoundError:
        print('Arquivo não encontrado\n')
    except Exception as e:
        print('Algum erro inesperado ocorreu.')
        print(f'{e}\n')


def salvar():
    exportar_agenda('database')


def carregar():
    arquivo_importar = 'database.json'
    try:
        with open(arquivo_importar) as a_obj:
            contatos = json.load(a_obj)
            if contatos:
                for contato in contatos:
                    informacao_contato = contatos[contato]
                    AGENDA[contato] = {
                        'telefone': informacao_contato["telefone"],
                        'email': informacao_contato["email"],
                        'endereco': informacao_contato["endereco"]
                   }
            else:
                print('Database vazio.\n')
        print(f'Database carregado com sucesso.\nContatos carregado: {len(AGENDA)}')
    except FileNotFoundError:
        print('Arquivo não encontrado\n')
    except Exception as e:
        print('Algum erro inesperado ocorreu.')
        print(f'{e}\n')


carregar()
while True:
    imprimir_menu()
    opcao = input('Digite uma das opçôes: ')

    if opcao == '1':
        mostrar_contato()
    elif opcao == '2':
        contato = input('Digite nome do contato: ').title()
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite nome do contato que deseja adicionar: ').title()
        if contato in AGENDA:
            print(f'Contato "{contato.title()}" ja existente.\n')
        else:
            print(f'Adicionando contato {contato.title()}')
            dados = coletar_dados()
            if dados:
                verificador_de_dados()
    elif opcao == '4':
        contato = input('Digite nome do contato que deseja editar: ').title()
        if contato in AGENDA:
            print(f'Editando contato {contato.title()}.')
            dados = coletar_dados()
            if dados:
                verificador_de_dados()
        else:
            print(f'Contato "{contato.title()}" não existe.\n')
    elif opcao == '5':
        contato = input('Digite nome do contato que deseja deletar: ').title()
        excluir_contato(contato)
    elif opcao == '6':
        arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_agenda(arquivo)
    elif opcao == '7':
        arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(arquivo)
    elif opcao == '0':
        print('Saindo....')
        break
    else:
        print('Opção invalida\n')

