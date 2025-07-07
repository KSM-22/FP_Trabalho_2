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

options = ('pedra', 'papel', 'tesoura')


def inputChoose():
    print("""
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
    """)
    while True:
        selectedMode = str(input('Qual você vai mostrar? '))
        if selectedMode == "1":
            return 'pedra'
        elif selectedMode == "2":
            return 'papel'
        elif selectedMode == "3":
            return 'tesoura'
        else:
            print('Escolha inválida, selecione ou 1 ou 2 ou 3.')
            continue


def findWinner(players: dict[str, str]):
    jogadores = list(players.keys())

    opt1 = players[jogadores[0]]
    opt2 = players[jogadores[1]]
    if opt1 == 'pedra':
        # opt1 perdeu
        if opt2 == 'papel':
            jogadores.remove(jogadores[0])
        # opt1 ganhou
        elif opt2 == 'tesoura':
            jogadores.remove(jogadores[1])
    elif opt1 == 'papel':
        # opt1 perdeu
        if opt2 == 'tesoura':
            jogadores.remove(jogadores[0])
        # opt1 ganhou
        elif opt2 == 'pedra':
            jogadores.remove(jogadores[1])
    elif opt1 == 'tesoura':
        # opt1 perdeu
        if opt2 == 'pedra':
            jogadores.remove(jogadores[0])
        # opt1 ganhou
        elif opt2 == 'papel':
            jogadores.remove(jogadores[1])
    return jogadores


def pve():
    money = float(input('Digite sua aposta R$'))
    while money <= 0:
        print('Digite um valor de dinheiro válido!')
        money = float(input('Digite sua aposta R$'))
    while True:
        aiChoose = random.choice(options)
        playerChoose = inputChoose()
        print('-'*50)
        print(f'O Jogador escolheu {playerChoose.title()} e o computador escolheu {aiChoose.title()}')
        print(f'{playerChoose.title()} x {aiChoose.title()}')
        print('-'*50)
        winner = findWinner({"Jogador": playerChoose, "Computador": aiChoose})
        if len(winner) > 1:
            # Empate
            print('Como os dois escolheram igual houve um empate!')
        else:
            print(f'O vencedor foi o {winner[0]}!')
            if winner[0] == 'Jogador':
                print(f'Parabéns, você apostou R${money} e ganhou R${money * 2:.2f}')
                print(f'No entanto, com a taxa de serviço do sistema e terceiros seu valor líquido é de R${money + 0.5:.2f}')
            print('-'* 50)


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
