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

def Verificar_int(arg):
    while True:
        try:
            arg = int(input(f'ddigite a {mostrar_nome_da_variavel(arg)} do {contador}º aluno: '))
            return arg
        except ValueError:
            print('valor invalido')
        break

def mostrar_nome_da_variavel(arg):
    for var_name, var_value in globals().items():
        if var_value == idade:
            print(f'{var_value}')

cadastro_alunos = []
contador = 1
while True:
    nome = input(f'digite o nome do {contador}º aluno: ')
    if not nome.replace(' ','').isalpha():
        print('Nome invalido!\n')
        continue

    nome_completo = nome.split(' ')
    if len(nome_completo) < 2 or len(nome) < 3 :
        print('Nome invalido!\n')
        continue
    idade = 0
    idade = Verificar_int(idade)

    if idade < 0 or idade > 123:
        print('Idade invalida!\n')

    nota = input(f'digite a nota do {contador}º aluno: ')
    if nota.isdigit() == False:
        print('Nota invalida"\n')
    aluno = {'nome': nome.title(), 'idade': idade, 'nota final': nota}
    contador += 1
    cadastro_alunos.append(aluno)

    print(cadastro_alunos)