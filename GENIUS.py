from random import randint
import os
from time import sleep


def limpaTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def verJogadores():
    if os.path.isfile('gamers.txt'):
        f = open('gamers.txt', 'r')
        for linha in f:
            linha = linha.rstrip()
            print(linha)
        f.close()


def cadastro(jogador):
   nome = input('Digite seu nome: ')

   jogador.append((nome))


def salvarJogador(jogador):
    f = open('gamers.txt','a')

    for nome in jogador:
        f.write(f' {nome} \n')

    f.close()


def game():
    print(f'Vamos Jogar!')
    sleep(2)
    ponto = 0
    jogador = []
    sorteado = randint(0, 9)
    correta = str(sorteado)
    print(f"O primeiro numero sorteado foi: {sorteado}")
    x = input("Digite a sequencia completa: ")

    while x == correta:
        ponto = len(correta) - 1
        sorteado = randint(0, 9)
        correta = correta + str(sorteado)
        limpaTela()
        print(f"O novo numero é: {sorteado}")
        x = input("Digite a sequencia completa: ")

    print(f"Errou! Voce ganhou {len(correta) - 1} pontos.")
    if ponto >= 10:
        salvarJogador(jogador)

    cont = 'Deseja continuar? [S|N]:'
    c = input(cont)
    if c in ['s','S']:
        limpaTela()
        game()
    elif c in ['N', 'n']:
        print('GAME OVER')
    else:
        print('Opção Inválida')
        c = input(cont)


def main():
    menu = '''--- GAME GENIUS ---
    [1] - Cadastrar
    [2] - Ranking +10 pts 
    [3] - Sair
    Escolha uma oção: '''

    opcao = input(menu)
    jogador = []

    while opcao not in ['3']:
        if opcao in ['1']:
            limpaTela()
            cadastro(jogador)
            game()
            salvarJogador(jogador)
            sleep(1)
        elif opcao in ['2']:
            limpaTela()
            verJogadores()
            sleep(3)
            limpaTela()
        elif opcao in ['3']:
            print('GAME OVER')

        else:
            print('Opção Inválida')

        opcao = input(menu)


if __name__ == '__main__':
    main()