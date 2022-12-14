titulo = ''
tabuleiroPc = []
tabuleiroJogador = []
tamanho_tabuleiro = 15 #entrada do tamanho do tabuleiro.

def construirTabuleiro(tamanho_tabuleiro, tabuleiro): #Laço construtor de tabuleiro.
    for i in range(tamanho_tabuleiro):
        lista = []
        for j in range(tamanho_tabuleiro):
            lista.append(0)
        tabuleiro.append(lista)


def imprimirTabuleiro():
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

def posicionarBarco(tabuleiro, celula, barco):
    if barco[1] == 'horizontal':
        for i in range(barco[0]):
            tabuleiro[celula[0]][celula[1]+i] = '<'


barco = [5, 'horizontal']
celula = [2, 2]


construirTabuleiro(tamanho_tabuleiro, tabuleiroJogador)
construirTabuleiro(tamanho_tabuleiro, tabuleiroPc)
posicionarBarco(tabuleiroJogador, celula, barco)
imprimirTabuleiro()
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
print(' '*28, f'Olá, {jogador1}, POSICIONE SUAS EMBARCAÇÕES')


