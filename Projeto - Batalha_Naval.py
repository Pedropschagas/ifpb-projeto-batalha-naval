titulo = ''
tabuleiroPc = []
tabuleiroJogador = []
tamanho_tabuleiro = 15 #entrada do tamanho do tabuleiro.

def construirtabuleiro(tamanho_tabuleiro, tabuleiro): #Laço construtor de tabuleiro.
    for i in range(tamanho_tabuleiro):
        lista = []
        for j in range(tamanho_tabuleiro):
            lista.append(0)
        tabuleiro.append(lista)


def imprimirtabuleiro():
    limite = tamanho_tabuleiro
    if limite > 10:
        limite = 10
    referenciaLetra = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    print('   ', end='')
    for i in range(1, limite):
        print(i, end='  ')
    print(limite, end=' ')
    if tamanho_tabuleiro > 10:
        for i in range(11, tamanho_tabuleiro + 1):
            print(i, end=' ')
    if limite < 10:
        print('               ', end='')
    else:
        print('              ', end='')
    for i in range(1, limite):
        print(i, end='  ')
    print(limite, end=' ')
    if tamanho_tabuleiro > 10:
        for i in range(11, tamanho_tabuleiro + 1):
            print(i, end=' ')
    print()
    for i in range(tamanho_tabuleiro):
        print(referenciaLetra[i], end='  ')
        for j in range(tamanho_tabuleiro):
            print(tabuleiroJogador[i][j], end='  ')
        print('   ||     ', referenciaLetra[i], end='  ')
        for j in range(tamanho_tabuleiro):
            print(tabuleiroPc[i][j], end='  ')
        print()



construirtabuleiro(tamanho_tabuleiro, tabuleiroJogador)
construirtabuleiro(tamanho_tabuleiro, tabuleiroPc)
imprimirtabuleiro()
print()
print()

print(' '*54, 'BATALHA NAVAL')
print('-_'*60)
print()
jogador1 = input('Diga-me, Jogador1, qual é o seu nome?  ')
print()
print()
print()
print()
print(' '*28, f'Olá, {jogador1}, POSICIONE SUAS EMBARCAÇÕES ATÉ UM TOTAL DE 7 PONTOS')
