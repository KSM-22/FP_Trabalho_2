'''
1. Cadastro de Alunos
Descrição: Criar um programa que armazene e gerencie o cadastro de alunos,
incluindo nome, idade e nota final.
Estruturas utilizadas:
• Dicionário: Para armazenar os dados de cada aluno, onde a chave é o nome
e o valor é uma tupla contendo idade e nota final.
• Lista: Para armazenar todos os dicionários dos alunos.
• Laço while: Para permitir o cadastro de múltiplos alunos até que o usuário
decida parar.
• Condicionais (if, elif, else): Para verificar se o aluno já está cadastrado ou se
os dados foram inseridos corretamente.
'''

import random  # Importa o módulo para gerar números e escolhas aleatórias

# ——— UTILITÁRIOS ———

def cor_verde(texto: str) -> str:
    '''Aplica cor verde ao texto para destacar no terminal'''
    return f'\033[32m{texto}\033[0m'

def mostrar_nome_da_variavel(**kwargs) -> str:
    '''Retorna o nome da primeira chave passada como argumento nomeado'''
    return next(iter(kwargs))

def verificar_int(contador, **kwargs) -> dict:
    '''Valida se a entrada é um número inteiro. Continua pedindo até ser válido'''
    while True:
        try:
            nome = mostrar_nome_da_variavel(**kwargs)
            valor = int(input(f'Digite a {cor_verde(nome)} do {contador}º aluno: '))
            return {nome: valor}
        except ValueError:
            print(f'{nome} inválida.\n')

def limpar(texto: str) -> str:
    '''Remove colchetes e aspas simples da string'''
    return texto.replace('[', '').replace(']', '').replace("'", '')

def nome_ja_cadastrado(nome: str, cadastros: list) -> bool:
    '''Verifica se o nome já existe nos cadastros'''
    return any(aluno['nome'] == nome.title() for aluno in cadastros)

# ——— MENU ———

def exibir_menu():
    '''Exibe o menu principal de opções e retorna a escolha'''
    print('—' * 60)
    print(f'1. {cor_verde('Adicionar')} aluno')
    print(f'2. {cor_verde('Listar')} alunos')
    print(f'3. {cor_verde('Editar')} aluno')
    print(f'4. {cor_verde('Deletar')} aluno')
    print(f'5. {cor_verde('Gerar')} aluno aleatório')
    print(f'6. {cor_verde('Sair')}')
    print('—' * 60)
    return input('Escolha uma opção: ').strip()

# ——— CADASTRO ———

def adicionar_aluno(cadastro_alunos):
    '''Adiciona um novo aluno após validações'''
    contador = len(cadastro_alunos) + 1

    # Nome
    while True:
        nome = input(f'Digite o {cor_verde('nome')} do {contador}º aluno: ').strip()
        if not nome or not nome.replace(' ', '').isalpha():
            print('Nome inválido!\n')
            continue
        if len(nome.split()) < 2 or nome_ja_cadastrado(nome, cadastro_alunos):
            print('Nome inválido ou já cadastrado!\n')
            continue
        break

    # Idade
    while True:
        idade = verificar_int(contador, idade=None)['idade']
        if 0 < idade <= 123:
            break
        print('Idade inválida!\n')

    # Nota
    while True:
        nota = verificar_int(contador, nota=None)['nota']
        if 0 <= nota <= 10:
            break
        print('Nota inválida!\n')

    # Série
    SERIES = {i: f'{i}º ano' for i in range(1, 10)}
    while True:
        try:
            serie = int(input('Digite a série do aluno (1-9): '))
            if 1 <= serie <= 9:
                break
            print('Série inválida!\n')
        except ValueError:
            print('Entrada inválida!\n')

    # Status de formação
    formado = False
    if serie == 9:
        while True:
            status = input('O aluno já concluiu o 9º ano? (S/N): ').upper()
            if status in ['S', 'N']:
                formado = (status == 'S')
                break
            print('Resposta inválida!')

    aluno = {
        'nome': nome.title(),
        'idade': idade,
        'nota final': nota,
        'serie': SERIES[serie],
        'formado': formado
    }

    cadastro_alunos.append(aluno)

    print(f'\nStatus: {'Formado' if formado else 'Em curso'}')
    print('\n' + '—' * 60)
    print(f'Aluno {cor_verde('Adicionado')} com Sucesso!')

# ——— LISTAGEM ———

def listar_alunos(cadastro_alunos):
    '''Lista os alunos, com opções de ordenação ou filtragem'''
    if not cadastro_alunos:
        print('Nenhum aluno cadastrado!')
        return

    campo, ordem = menu_ordenacao()
    if not campo:
        return

    campo_map = {
        '1': 'nome',
        '2': 'idade',
        '3': 'nota final',
        '4': 'serie',
        '5': 'formado'
    }

    chave = campo_map[campo]
    reverse = ordem == '2'

    if campo == '5':
        status = ordem == '1'
        alunos_filtrados = [aluno for aluno in cadastro_alunos if aluno['formado'] == status]
    else:
        alunos_filtrados = sorted(cadastro_alunos, key=lambda x: x[chave], reverse=reverse)

    for aluno in alunos_filtrados:
        print('—' * 20)
        print(f'{cor_verde('Nome')}: {aluno['nome']}')
        print(f'{cor_verde('Idade')}: {aluno['idade']}')
        print(f'{cor_verde('Nota')}: {aluno['nota final']}')
        print(f'{cor_verde('Série')}: {aluno['serie']}')
        print(f'{cor_verde('Status')}: {'Formado' if aluno['formado'] else 'Em curso'}')

def menu_ordenacao():
    '''Exibe o menu de ordenação e retorna os critérios'''
    while True:
        print('—' * 60)
        print(f'1. {cor_verde('Nome')}')
        print(f'2. {cor_verde('Idade')}')
        print(f'3. {cor_verde('Nota')}')
        print(f'4. {cor_verde('Série')}')
        print(f'5. {cor_verde('Status de Formação')}')
        print('—' * 60)

        campo = input('Escolha um campo para ordenação: ').strip()

        if campo not in ['1', '2', '3', '4', '5']:
            print('\nOpção inválida! Por favor, escolha um número entre 1 e 5.')
            continue

        if campo == '5':
            print('\n' + '—' * 60)
            print(f'1. {cor_verde('Formados')}')
            print(f'2. {cor_verde('Em curso')}')
            print('—' * 60)
            ordem = input('Escolha o status: ').strip()

            if ordem not in ['1', '2']:
                print('\nOpção inválida! Por favor, escolha 1 ou 2.')
                continue
            return campo, ordem

        else:
            print('\n' + '—' * 60)
            print(f'1. {cor_verde('Crescente')}')
            print(f'2. {cor_verde('Decrescente')}')
            print('—' * 60)
            ordem = input('Escolha a ordem: ').strip()

            if ordem not in ['1', '2']:
                print('\nOpção inválida! Por favor, escolha 1 ou 2.')
                continue
            return campo, ordem

# ——— EDIÇÃO ———

def editar_aluno(cadastro_alunos):
    '''Permite editar os dados de um aluno existente'''
    if not cadastro_alunos:
        print('—' * 60 + '\nNenhum aluno cadastrado!')
        return

    nome = input('Nome do aluno a editar: ').title()
    aluno = next((a for a in cadastro_alunos if a['nome'] == nome), None)

    if not aluno:
        print('—' * 60 + '\nAluno não encontrado!')
        return

    while True:
        print('\nEditando:', aluno['nome'])
        print(f'1. {cor_verde('Nome')}\n2. {cor_verde('Idade')}\n3. {cor_verde('Nota')}\n4. {cor_verde('Série')}\n5. {cor_verde('Status de Formação')}\n6. {cor_verde('Voltar')}')
        escolha = input('Escolha a opção: ')

        if escolha == '1':
            novo_nome = input('Novo nome: ').strip()
            if novo_nome and len(novo_nome.split()) >= 2:
                aluno['nome'] = novo_nome.title()
        elif escolha == '2':
            idade = verificar_int(0, idade=None)['idade']
            aluno['idade'] = idade
        elif escolha == '3':
            nota = verificar_int(0, nota=None)['nota']
            aluno['nota final'] = nota
        elif escolha == '4':
            nova_serie = int(input('Nova série (1-9): '))
            aluno['serie'] = f'{nova_serie}º ano'
            if nova_serie != 9:
                aluno['formado'] = False
        elif escolha == '5':
            if aluno['serie'] == '9º ano':
                status = input('Concluiu o 9º ano? (S/N): ').upper()
                aluno['formado'] = (status == 'S')
            else:
                print('Somente para alunos do 9º ano.')
        elif escolha == '6':
            break
        else:
            print('—' * 60 + '\nOpção inválida.')

# ——— DELETAR ———

def deletar_aluno(cadastro_alunos):
    '''Remove um aluno da lista de cadastro'''
    if not cadastro_alunos:
        print('—' * 60 + '\nNenhum aluno cadastrado!')
        return

    nome = input('Digite o nome do aluno para excluir: ').title()
    for aluno in cadastro_alunos:
        if aluno['nome'] == nome:
            cadastro_alunos.remove(aluno)
            print('—' * 60 + f'\nAluno {cor_verde('removido')} com sucesso!')
            return

    print('—' * 60 + '\nAluno não encontrado!')

# ——— GERADOR ———

def gerar_aluno():
    '''Gera automaticamente um aluno com dados aleatórios'''
    # Lista com 50 nomes próprios populares no Brasil
    nomes = [
        "Lucas", "João", "Maria", "Ana", "Pedro", "Gabriel", "Julia", "Beatriz", "Carlos", "Marcos",
        "Fernanda", "Mateus", "Camila", "Rafael", "Larissa", "Bruna", "Gustavo", "Clara", "Vinícius", "Isabela",
        "Eduardo", "Tatiane", "Rodrigo", "Letícia", "André", "Paula", "Bruno", "Amanda", "Thiago", "Jéssica",
        "Felipe", "Vanessa", "Ricardo", "Patrícia", "Leonardo", "Simone", "Daniel", "Aline", "Diego", "Elaine",
        "César", "Kelly", "Igor", "Renata", "Luiz", "Débora", "Henrique", "Natália", "Alex", "Yasmin"
    ]

    # Lista com 50 primeiros sobrenomes comuns
    sobrenomes1 = [
        "da Silva", "dos Santos", "de Oliveira", "de Souza", "Pereira", "Lima", "Carvalho", "Ferreira", "Rodrigues",
        "Almeida",
        "Costa", "Gomes", "Martins", "Araujo", "Barbosa", "Ribeiro", "Dias", "Teixeira", "Fernandes", "Moura",
        "Cavalcante", "Castro", "Rocha", "Rezende", "Melo", "Correia", "Farias", "Monteiro", "Freitas", "Andrade",
        "Nunes", "Machado", "Nascimento", "Pinto", "Batista", "Cardoso", "Campos", "Antunes", "Borges", "Tavares",
        "Cunha", "Moreira", "Morais", "Vieira", "Jesus", "Rezende", "Neves", "Fonseca", "Barros", "Peixoto"
    ]

    # Lista com 50 segundos sobrenomes comuns (pode repetir, ou variar)
    sobrenomes2 = [
        "da Silva", "dos Santos", "Costa", "Pereira", "de Oliveira", "de Souza", "Rodrigues", "Almeida", "Lima",
        "Ferreira",
        "Ribeiro", "Martins", "Gomes", "Araújo", "Barbosa", "Moura", "Teixeira", "Fernandes", "Melo", "Rocha",
        "Monteiro", "Castro", "Carvalho", "Cavalcante", "Dias", "Andrade", "Nascimento", "Machado", "Campos", "Batista",
        "Correia", "Cardoso", "Freitas", "Tavares", "Cunha", "Morais", "Moreira", "Vieira", "Jesus", "Neves",
        "Antunes", "Borges", "Fonseca", "Barros", "Peixoto", "Rezende", "Soares", "Aguiar", "Valente", "Assis"
    ]

    nome = f'{random.choice(nomes)} {random.choice(sobrenomes1)} {random.choice(sobrenomes2)}'
    while nome.split(' ')[1] == nome.split(' ')[2]:
        nome = f'{random.choice(nomes)} {random.choice(sobrenomes1)} {random.choice(sobrenomes2)}'

    serie = random.randint(1, 9)
    idade = serie + 6 + random.choice([0]*8 + [1])
    nota = random.randint(0, 10)
    formado = random.choice([True, False]) if serie == 9 else False

    aluno = {
        'nome': nome,
        'idade': idade,
        'nota final': nota,
        'serie': f'{serie}º ano',
        'formado': formado
    }

    cadastro_alunos.append(aluno)
    print('—' * 60 + f'\nAluno gerado: {aluno['nome']}')

# ——— PROGRAMA PRINCIPAL ———

cadastro_alunos = [
    {'nome': 'João Silva', 'idade': 15, 'nota final': 8, 'serie': '7º ano', 'formado': False},
    {'nome': 'Maria De Souza', 'idade': 18, 'nota final': 9, 'serie': '9º ano', 'formado': True}
]

print('—' * 60)
print(f'''{'SISTEMA DE GESTÃO DE ALUNOS':^60}''')

while True:
    opcao = exibir_menu()

    if opcao == '1':
        adicionar_aluno(cadastro_alunos)
    elif opcao == '2':
        listar_alunos(cadastro_alunos)
    elif opcao == '3':
        editar_aluno(cadastro_alunos)
    elif opcao == '4':
        deletar_aluno(cadastro_alunos)
    elif opcao == '5':
        gerar_aluno()
    elif opcao == '6':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida!')
