
import random # importando a biblioteca para randomizar números

titulo = ''
tabuleiroPc = []
tabuleiroJogador = []
tamanho_tabuleiro = 15  # entrada do tamanho do tabuleiro.
caractereBarco = '<'
caractereRedor = '-'
barco = [0, '']
celula = [0, 0]
tamanhoDosBarcos = [5, 4, 3, 3, 2, 2]

# Laço construtor de tabuleiro.
def construirTabuleiro(tamanho_tabuleiro, tabuleiro):
    for i in range(tamanho_tabuleiro):
        lista = []
        for j in range(tamanho_tabuleiro):
            lista.append(0)
        tabuleiro.append(lista)


def imprimirTabuleiro():
    limite = tamanho_tabuleiro
    if limite > 10:
        limite = 10
    referenciaLetra = ['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
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


# A função verifica se o barco estoura o espaço do tabuleiro e se fica muito próximo de outro barco já posicionado
def verificarSePodePosicionar(tabuleiro, celula, barco):
    if barco[1] == 'horizontal':
        if (celula[1]+barco[0] > tamanho_tabuleiro) or (celula[0] >= tamanho_tabuleiro):
            return False
        for i in range(barco[0]):
            if (tabuleiro[celula[0]][celula[1]+i] == caractereBarco) or (tabuleiro[celula[0]][celula[1]+i] == caractereRedor):
                return False
    else:
        if (celula[0]+barco[0] > tamanho_tabuleiro) or (celula[1] >= tamanho_tabuleiro):
            return False
        for i in range(barco[0]):
            if (tabuleiro[celula[0]+i][celula[1]] == caractereBarco) or (tabuleiro[celula[0]+i][celula[1]] == caractereRedor):
                return False
    return True


# Função para posicionar o barco num tabuleiro
def posicionarBarco(tabuleiro, celula, barco):

    if not verificarSePodePosicionar(tabuleiro, celula, barco):
        # print("Você não pode colocar barco nessa posição!")
        return False

    if barco[1] == 'horizontal':
        for i in range(barco[0]):
            tabuleiro[celula[0]][celula[1]+i] = caractereBarco
    else:
        for i in range(barco[0]):
            tabuleiro[celula[0]+i][celula[1]] = caractereBarco

    marcarRedorBarco(tabuleiro)
    return True

# Função que marca ao redor de um baco posicionado. Para que não tenha seja colocado outro barco próximo.


def marcarRedorBarco(tabuleiro):
    for i in range(tamanho_tabuleiro): # iterando na linha
        for j in range(tamanho_tabuleiro): # iterando na coluna
            if tabuleiro[i][j] != caractereBarco:
                for k in range(3): #linha fixa
                    for l in range(3): #coluna
                        # i=0 j=0 k=0 l=0
                        if (i - 1 + k >= 0) and (j - 1 + l >= 0) and (i - 1 + k < tamanho_tabuleiro) and (j - 1 + l < tamanho_tabuleiro):
                            if tabuleiro[i-1+k][j-1+l] == caractereBarco:
                                tabuleiro[i][j] = caractereRedor


# Função para posicionar um barco de forma randomica, se um barco não puder ser posicionado ela vai tentar 100 vezes.
def posicionarBarcoCPU(tabuleiro, tamanhoBarco):
    maximoTentativas = 0
    while maximoTentativas <= 100:
        barco = [0, '']
        celula = [0, 0]
        barco[0] = tamanhoBarco
        barcoSentido = random.randrange(2)
        if barcoSentido == 0:
            barco[1] = "horizontal"
        else:
            barco[1] = "vertical"
        celula[0] = random.randrange(tamanho_tabuleiro)
        celula[1] = random.randrange(tamanho_tabuleiro)

        if (posicionarBarco(tabuleiro, celula, barco)):
            return True

        maximoTentativas += 1
    return False


# Aqui a função que vai analisar quantos barcos deve inserir automaticamente para a CPU.
def CPUBarcos():
    tamanhoMaxBarco = []

    for i in range(len(tamanhoDosBarcos)):
        if tamanho_tabuleiro > 12:
            tamanhoMaxBarco.append(tamanhoDosBarcos[i])
        elif tamanho_tabuleiro > 9 and tamanhoDosBarcos[i] <= 4:
            tamanhoMaxBarco.append(tamanhoDosBarcos[i])
        elif tamanhoDosBarcos[i] <= 3:
            tamanhoMaxBarco.append(tamanhoDosBarcos[i])

    for i in tamanhoMaxBarco:
        if not (posicionarBarcoCPU(tabuleiroPc, i)):
            print(
                "Número máximo de tentativas para a CPU posicionar barcos estourou, rode o APP novamente!")


# Main
construirTabuleiro(tamanho_tabuleiro, tabuleiroJogador)
construirTabuleiro(tamanho_tabuleiro, tabuleiroPc)

barco = [5, 'horizontal']
celula = [2, 2]
posicionarBarco(tabuleiroJogador, celula, barco)

barco = [5, 'vertical']
celula = [8, 5]
posicionarBarco(tabuleiroJogador, celula, barco)

barco = [2, 'horizontal']
celula = [1, 13]
posicionarBarco(tabuleiroJogador, celula, barco)

barco = [4, 'vertical']
celula = [11, 12]
posicionarBarco(tabuleiroJogador, celula, barco)

barco = [2, 'vertical']
celula = [11, 0]
posicionarBarco(tabuleiroJogador, celula, barco)

barco = [3, 'horizontal']
celula = [6, 10]
posicionarBarco(tabuleiroJogador, celula, barco)

CPUBarcos()

imprimirTabuleiro()


# print()
# print()

# print(' '*54, 'BATALHA NAVAL')
# print('-_'*60)
# print()
# jogador1 = input('Diga-me, Jogador1, qual é o seu nome?  ')
# print()
# print()
# print()
# print()
# print(' '*28, f'Olá, {jogador1}, POSICIONE SUAS EMBARCAÇÕES')
