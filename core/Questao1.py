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

def mostrar_nome_da_variavel(**kwargs):
    for nome in kwargs:
        return nome

def Verificar_int(**kwargs):
    while True:
        try:
            nome = mostrar_nome_da_variavel(**kwargs)
            arg = int(input(f'Digite a {nome} do {contador}º aluno: '))
            return {nome: arg}
        except ValueError:
            print(f'{nome} inválida.\n')

def Limpar(*arg):
    texto = str(arg[0])
    return f'{texto.replace("[", "").replace("]", "").replace("\'", "")}'

def nome_ja_cadastrado(nome, cadastros):
    return any(aluno['nome'] == nome.title() for aluno in cadastros)

cadastro_alunos = []
contador = 1

while True:
    while True:
        nome = input(f'Digite o nome do {contador}º aluno: ')
        if not nome.replace(' ', '').isalpha():
            print('Nome inválido!\n')
            continue

        nome_completo = nome.split(' ')
        if len(nome_completo) < 2 or len(nome) < 3 or nome_ja_cadastrado(nome, cadastro_alunos):
            print('Nome inválido!\n')
            continue
        else:
            break

    while True:
        idade_dict = Verificar_int(idade=None)
        idade = idade_dict['idade']

        if idade < 0 or idade > 123:
            print('Idade inválida!\n')
            continue
        else:
            break

    while True:
        nota_dict = Verificar_int(nota=None)
        nota = nota_dict['nota']
        if nota < 0 or nota > 10:
            print('Nota inválida!\n')
            continue
        else:
            break

    aluno = {'nome': nome.title(), 'idade': idade, 'nota final': nota}
    cadastro_alunos.append(aluno)
    mostrar_cadastro = str(cadastro_alunos)
    print(f'\nCadastro até agora: {Limpar(mostrar_cadastro)}\n')

    contador += 1

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break
