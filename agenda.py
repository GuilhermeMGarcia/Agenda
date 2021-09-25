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
    nome_contato = AGENDA[contato]
    print(f'Nome: {contato.title()}')
    print(f'Telefone: {nome_contato["telefone"]}\n'
          f'Email: {nome_contato["email"]}\n'
          f'Endereço: {nome_contato["endereco"]}\n'
          f'\n --------------------------------------------------')


def incluir_editar_contato(contato, telefone = '', email = '', endereco = ''):
    if contato in AGENDA:
        imprimir = (f'>>>>>>>>>> Contato {contato.title} editado com sucesso.\n')
    else:
        imprimir = (f'>>>>>>>>>> Contato {contato.title} adicionado com sucesso.\n')
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(imprimir)
def excluir_contato(contato):
    if contato in AGENDA:
        del AGENDA[contato]
        print(f'>>>>>>>Contato {contato.title()} excluido com sucesso.\n')
    else:
        print(f'>>>>>>>Contato {contato.title()} n existe.')

excluir_contato('joao')
excluir_contato('guilherme')
mostrar_contato()