import getpass
import random

options = ('Pedra', 'Papel', 'Tesoura')


def inputChoose():
    print("""Opções disponíveis:
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
    """)
    while True:
        selectedMode = getpass.getpass(prompt='Qual você vai mostrar? ')
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

    # Verifica o empate
    if opt1 == opt2:
        return jogadores

    # Verficia a vitoria do Jogador 1
    if opt1 == 'Pedra' and opt2 == 'Tesoura':
        jogadores.remove(jogadores[1])
    elif opt1 == 'Papel' and opt2 == 'Pedra':
        jogadores.remove(jogadores[1])
    elif opt1 == 'Tesoura' and opt2 == 'Papel':
        jogadores.remove(jogadores[1])
    # Se alcança o else, significa que não é empate e o J1 não ganhou, portanto, o J2 venceu.
    else:
        jogadores.remove(jogadores[0])

    return jogadores


def pve():
    while True:
        print('Caso não queira apostar coloque 0 no valor.')
        money = float(input('Digite sua aposta R$'))
        while money < 0:
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
            if money != 0:
                if winner[0] == 'Jogador':
                    print(f'Parabéns, você apostou R${money:.2f} e ganhou R${money * 2:.2f}')
                    print(
                        f'No entanto, com a taxa de serviço do sistema e terceiros seu valor líquido é de R${money + 0.5:.2f}')
                else:
                    print(
                        f'Você perdeu, mas não se preocupe seu bonus de dinheiro foi aprimorado caso ganhe na proxima!')
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
    while True:
        betOption = str(input('Vocês vão querer apostar? (S/N)')).upper()
        p1_name = str(input('\nQual nome do Jogador 1? ')).strip().capitalize()
        p1_choose = inputChoose()
        p1_money = 0

        p2_name = str(input('\nQual nome do Jogador 2? ')).strip().capitalize()
        p2_choose = inputChoose()
        p2_money = 0
        if betOption == "S":
            p1_money = float(input(f'{p1_name}, digite o valor de sua aposta R$'))
            while p1_money <= 0:
                print('Digite um valor de dinheiro válido!')
                p1_money = float(input('Digite sua aposta R$'))

            p2_money = float(input(f'{p2_name},digite o valor de sua aposta R$'))
            while p2_money <= 0:
                print('Digite um valor de dinheiro válido!')
                p2_money = float(input('Digite sua aposta R$'))

        gameData = {p1_name: p1_choose, p2_name: p2_choose}

        print('-' * 60)
        print(f'{p1_name} escolheu {p1_choose} e {p2_name} escolheu {p2_choose}')
        print(f'{p1_choose} x {p2_choose}')
        print('-' * 60)
        winner = findWinner(gameData)
        if len(winner) > 1:
            # Empate
            print('Como os dois escolheram igual houve um empate!')
        else:
            print(
                f'O vencedor foi o {winner[0]}, pois {gameData.pop(winner[0])} ganha de {list(gameData.values())[0]}!')
            if betOption == 'S':
                print(f'{p1_name} apostou R${p1_money:.2f} e {p2_name} apostou R${p2_money:.2f}')
                print(f'Parabéns {winner[0]} você ganhou R${p1_money + p2_money:.2f}')
            print('-' * 60)

        proceedOption = str(input('Deseja continuar? [S/N] ')).upper()
        if proceedOption == 'S':
            continue
        elif proceedOption == 'N':
            break
        else:
            print('Opção inválida, encerrando sistema.')
            break


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
