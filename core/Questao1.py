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

def adicionar_aluno(cadastro_alunos):
    contador = len(cadastro_alunos) + 1
    # Validação do nome
    while True:
        nome = input(f'Digite o {cor_verde("nome")} do {contador}º aluno: ').strip()
        if not nome or not nome.replace(' ', '').isalpha():
            print('Nome inválido!\n')
            continue

        nome_completo = nome.split(' ')
        if len(nome_completo) < 2 or len(nome) < 3 or nome_ja_cadastrado(nome, cadastro_alunos):
            print('Nome inválido!\n')
            continue
        break

    # Validação da idade
    while True:
        idade_dict = Verificar_int(contador, idade=None)
        idade = idade_dict['idade']
        if idade < 0 or idade > 123:
            print('Idade inválida!\n')
            continue
        break

    # Validação da nota
    while True:
        nota_dict = Verificar_int(contador, nota=None)
        nota = nota_dict['nota']
        if nota < 0 or nota > 10:
            print('Nota inválida!\n')
            continue
        break

    # Validação da série
    SERIES = {
        1: '1º ano',
        2: '2º ano',
        3: '3º ano',
        4: '4º ano',
        5: '5º ano',
        6: '6º ano',
        7: '7º ano',
        8: '8º ano',
        9: '9º ano',
    }

    while True:
        serie = int(input("Digite a série do aluno (1-9): "))
        if 1 <= serie <= 9:
            break
        print("Série inválida!\n")

    # Criação e adição do aluno
    aluno = {'nome': nome.title(), 'idade': idade, 'nota final': nota}
    aluno['serie'] = SERIES[serie]

    if serie == 9:
        while True:
            status = input("O aluno já concluiu o 9º ano? (S/N): ").upper()
            if status in ['S', 'N']:
                break
            print("Resposta inválida! Digite S para Sim ou N para Não.")
        formado = status == 'S'
    else:
        formado = False

    aluno['formado'] = formado
    cadastro_alunos.append(aluno)

    if serie == 9:
        print(f"\nStatus do aluno: {'Já formado' if formado else 'Cursando 9º ano'}")

    mostrar_cadastro = str(cadastro_alunos)
    print('\n' + '—' * 60)
    print(f'\nCadastro até agora: {Limpar(mostrar_cadastro)}\n')

def listar_alunos(cadastro_alunos):
    if not cadastro_alunos:
        print("\nNenhum aluno cadastrado!")
        return

    campo, ordem = menu_ordenacao()
    campo_map = {
        '1': 'nome',
        '2': 'idade',
        '3': 'nota final',
        '4': 'serie',
        '5': 'formado'
    }

    if campo in campo_map:
        campo_ordenacao = campo_map[campo]
        alunos_ordenados = sorted(cadastro_alunos.copy(),
                                  key=lambda x: x[campo_ordenacao],
                                  reverse=(ordem == '2'))

        if campo == '5':
            formados = ordem == '1'
            alunos_filtrados = [aluno for aluno in alunos_ordenados if aluno['formado'] == formados]
        else:
            alunos_filtrados = alunos_ordenados

        for aluno in alunos_filtrados:
            print('—' * 16 + f'{'Informações do Aluno':^28}' + '—' * 16)
            print(f'\n{cor_verde('Nome')}: {aluno['nome']}')
            print(f'{cor_verde('Idade')}: {aluno['idade']}')
            print(f'{cor_verde('Nota')}: {aluno['nota final']}')
            print(f'{cor_verde('Série')}: {aluno['serie']}')
            print(f'{cor_verde('Status')}: {'Formado' if aluno['formado'] else 'Em curso'}\n')

def menu_ordenacao():
    while True:
        print("—" * 60 +
              f'\n1. {cor_verde("Nome")}\n'
              f'2. {cor_verde("Idade")}\n'
              f'3. {cor_verde("Nota")}\n'
              f'4. {cor_verde("Série")}\n'
              f'5. {cor_verde("Status de Formação")}\n'
              + '—' * 60)
        campo = input("Escolha um campo para ordenação: ").strip()
        if campo not in ['1', '2', '3', '4', '5']:
            print("\nOpção inválida! Por favor, escolha um número entre 1 e 5.")
            continue
        if campo == '5':
            print('\n' + '—' * 60)
            print(f'1. {cor_verde('Formados')}')
            print(f'2. {cor_verde('Em curso')}')
            print('—' * 60)
            ordem = input("Escolha o status: ").strip()
            if ordem not in ['1', '2']:
                print("\nOpção inválida! Por favor, escolha 1 ou 2.")
                continue

            return campo, ordem
        else:
            print('\n' + '—' * 60)
            print(f'1. {cor_verde('Crescente')}')
            print(f'2. {cor_verde(f'Decrescente')}')
            print('—' * 60)
            ordem = input("Escolha a ordem: ").strip()
            if ordem not in ['1', '2']:
                print("\nOpção inválida! Por favor, escolha 1 ou 2.")
                continue

            return campo, ordem

def editar_aluno(cadastro_alunos):
    if not cadastro_alunos:
        print("\nNenhum aluno cadastrado!")
        return

    nome = input("Digite o nome do aluno para editar: ").title()
    aluno_encontrado = None

    for aluno in cadastro_alunos:
        if aluno['nome'] == nome:
            aluno_encontrado = aluno
            break

    if not aluno_encontrado:
        print("\nAluno não encontrado!")
        return

    while True:
        print("\n" + "—" * 60)
        print(f"Editando aluno: {aluno_encontrado['nome']}")
        print("1. Nome")
        print("2. Idade")
        print("3. Nota")
        print("4. Série")
        print("5. Status de conclusão (apenas para 9º ano)")
        print("6. Voltar")
        print("—" * 60)

        opcao = input("Escolha o campo para editar: ").strip()

        if opcao == '1':
            while True:
                novo_nome = input("Digite o novo nome: ").strip()
                if not novo_nome or not novo_nome.replace(' ', '').isalpha():
                    print('Nome inválido!\n')
                    continue
                nome_completo = novo_nome.split(' ')
                if len(nome_completo) < 2 or len(novo_nome) < 3:
                    print('Nome inválido!\n')
                    continue
                aluno_encontrado['nome'] = novo_nome.title()
                break

        elif opcao == '2':
            while True:
                try:
                    nova_idade = int(input("Digite a nova idade: "))
                    if 0 <= nova_idade <= 123:
                        aluno_encontrado['idade'] = nova_idade
                        break
                    print("Idade inválida!\n")
                except ValueError:
                    print("Idade inválida!\n")

        elif opcao == '3':
            while True:
                try:
                    nova_nota = int(input("Digite a nova nota: "))
                    if 0 <= nova_nota <= 10:
                        aluno_encontrado['nota final'] = nova_nota
                        break
                    print("Nota inválida!\n")
                except ValueError:
                    print("Nota inválida!\n")

        elif opcao == '4':
            SERIES = {
                1: '1º ano', 2: '2º ano', 3: '3º ano',
                4: '4º ano', 5: '5º ano', 6: '6º ano',
                7: '7º ano', 8: '8º ano', 9: '9º ano',
            }
            while True:
                try:
                    nova_serie = int(input("Digite a nova série (1-9): "))
                    if 1 <= nova_serie <= 9:
                        aluno_encontrado['serie'] = SERIES[nova_serie]
                        if nova_serie != 9:
                            aluno_encontrado['formado'] = False
                        break
                    print("Série inválida!\n")
                except ValueError:
                    print("Série inválida!\n")

        elif opcao == '5':
            if aluno_encontrado['serie'] == '9º ano':
                while True:
                    status = input("O aluno já concluiu o 9º ano? (S/N): ").upper()
                    if status in ['S', 'N']:
                        aluno_encontrado['formado'] = (status == 'S')
                        break
                    print("Resposta inválida! Digite S para Sim ou N para Não.")
            else:
                print("Apenas alunos do 9º ano podem ter o status de conclusão alterado!")

        elif opcao == '6':
            print("\nEdição concluída!")
            break

        else:
            print("\nOpção inválida!")

        print(f"\nDados atualizados: {aluno_encontrado}")

def deletar_aluno(cadastro_alunos):
    if not cadastro_alunos:
        print("\nNenhum aluno cadastrado!")
        return

    nome = input("Digite o nome do aluno para excluir: ").title()
    for aluno in cadastro_alunos[:]:
        if aluno['nome'] == nome:
            cadastro_alunos.remove(aluno)
            print("\nAluno removido com sucesso!")
            return
    print("\nAluno não encontrado!")

def mostrar_nome_da_variavel(**kwargs) -> str:
    for nome in kwargs:
        return nome

def Verificar_int(contador, **kwargs) -> dict:
    while True:
        try:
            nome = mostrar_nome_da_variavel(**kwargs)
            arg = int(input(f'Digite a {cor_verde(nome)} do {contador}º aluno: '))
            return {nome: arg}
        except ValueError:
            print(f'{nome} inválida.\n')

def Limpar(*arg) -> str:
    texto = str(arg[0])
    return f'{texto.replace("[", "").replace("]", "").replace("\'", "")}'

def cor_verde(texto: str) -> str:
        return f'\033[32m{texto}\033[0m'

def nome_ja_cadastrado(nome: str, cadastros: list) -> bool:
    return any(aluno['nome'] == nome.title() for aluno in cadastros)


def exibir_menu():
    print('—' * 60)
    print(f'1. {cor_verde('Adicionar')} aluno')
    print(f'2. {cor_verde('Listar')} alunos')
    print(f'3. {cor_verde('Editar')} aluno')
    print(f'4. {cor_verde('Deletar')} aluno')
    print(f'5. {cor_verde('Sair')}')
    print('—' * 60)
    return input('Escolha uma opção: ').strip()

# cadastro_alunos = []
cadastro_alunos = [{
    'nome': 'João Silva',
    'idade': 15,
    'nota final': 8,
    'serie': '7º ano',
    'formado': False
},
{
    'nome': 'Maria De Souza',  # Ajustado para o formato correto
    'idade': 18,
    'nota final': 9,
    'serie': '9º ano',
    'formado': True
}]
print('—' * 60)
print(f'{"SISTEMA DE GESTÃO DE ALUNOS":^60}')

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
        print("\nEncerrando o programa...")
        break
    else:
        print("\nOpção inválida!")