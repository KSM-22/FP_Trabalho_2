"""
2. Jogo de Pedra, Papel e Tesoura
Descrição: Implementar o jogo clássico de Pedra, Papel e Tesoura, onde o usuário
joga contra o computador.
Estruturas utilizadas:
• Tupla: Para armazenar as opções ("Pedra", "Papel", "Tesoura").
• Laço while: Para permitir ao usuário jogar várias rodadas até decidir parar.
• Condicionais (if, elif, else): Para determinar o vencedor de cada rodada.
"""
import random

options = ('Pedra', 'Papel', 'Tesoura')


def inputChoose():
    print("""
    Opções disponíveis:
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
    """)
    while True:
        selectedMode = str(input('Qual você vai mostrar? '))
        if selectedMode == "1":
            return 'Pedra'
        elif selectedMode == "2":
            return 'Papel'
        elif selectedMode == "3":
            return 'Tesoura'
        else:
            print('Escolha inválida, selecione ou 1 ou 2 ou 3.')
            continue


def findWinner(players: dict[str, str]):
    jogadores = list(players.keys())

    opt1 = players[jogadores[0]]
    opt2 = players[jogadores[1]]
    if opt1 == 'Pedra':
        # opt1 perdeu
        if opt2 == 'Papel':
            jogadores.remove(jogadores[0])
        # opt1 ganhou
        elif opt2 == 'Tesoura':
            jogadores.remove(jogadores[1])
    elif opt1 == 'Papel':
        # opt1 perdeu
        if opt2 == 'Tesoura':
            jogadores.remove(jogadores[0])
        # opt1 ganhou
        elif opt2 == 'Pedra':
            jogadores.remove(jogadores[1])
    elif opt1 == 'Tesoura':
        # opt1 perdeu
        if opt2 == 'Pedra':
            jogadores.remove(jogadores[0])
        # opt1 ganhou
        elif opt2 == 'Papel':
            jogadores.remove(jogadores[1])
    return jogadores


def pve():
    while True:
        money = float(input('Digite sua aposta R$'))
        while money <= 0:
            print('Digite um valor de dinheiro válido!')
            money = float(input('Digite sua aposta R$'))

        aiChoose = random.choice(options)
        playerChoose = inputChoose()
        print('-' * 60)
        print(f'O Jogador escolheu {playerChoose} e o computador escolheu {aiChoose}')
        print(f'{playerChoose} x {aiChoose}')
        print('-' * 60)
        winner = findWinner({"Jogador": playerChoose, "Computador": aiChoose})
        if len(winner) > 1:
            # Empate
            print('Como os dois escolheram igual houve um empate!')
        else:
            print(f'O vencedor foi o {winner[0]}, pois {playerChoose} ganha de {aiChoose}!')
            if winner[0] == 'Jogador':
                print(f'Parabéns, você apostou R${money:.2f} e ganhou R${money * 2:.2f}')
                print(
                    f'No entanto, com a taxa de serviço do sistema e terceiros seu valor líquido é de R${money + 0.5:.2f}')
            else:
                print(f'Você perdeu, mas não se preocupe seu bonus de dinheiro foi aprimorado caso ganhe na proxima!')
            print('-' * 60)

        proceedOption = str(input('Deseja continuar? [S/N] ')).upper()
        if proceedOption == 'S':
            continue
        elif proceedOption == 'N':
            break
        else:
            print('Opção inválida, encerrando sistema.')
            break


def pvp():
    print('nada')


display_gameModes = '-' * 30 + """
[1] Jogador x Jogador
[2] Jogador x Computador
""" + '-' * 30
print(display_gameModes)

while True:
    selectedMode = str(input('Selecione o modo:'))
    if selectedMode == "1":
        pvp()
    elif selectedMode == "2":
        pve()
    else:
        print('Modo inválido, selecione 1 ou 2.')
        continue
    break
