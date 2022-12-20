
import random # importando a biblioteca para randomizar números

titulo = ''
tabuleiroPc = []
tabuleiroJogador = []
tamanho_tabuleiro = 5  # entrada do tamanho do tabuleiro.
caractereBarco = '<'
caractereRedor = '-'
barco = [0, '']
celula = [0, 0]
tamanhoDosBarcos = [5, 5, 4, 4, 3, 3, 2, 2]
placar = [0, 0]
flag = 0
atingiuBarco = False
tentativa = []
sentidoTiroBarco = 'direita'

# Laço construtor de tabuleiro.
def construirTabuleiro(tamanho_tabuleiro, tabuleiro):
    for i in range(tamanho_tabuleiro):
        lista = []
        for j in range(tamanho_tabuleiro):
            lista.append('*')
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
    print(f'PLACAR\n JOGADOR {placar[0]} X PC {placar[1]}')


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

#Função para ordenar ataques e placar.
def tiro(tabuleiro, celula, atirador):
    if tabuleiro[celula[0]][celula[1]] == caractereBarco:
        tabuleiro[celula[0]][celula[1]] = 'X'
        if atirador == 'jogador':
            placar[0] += 1
        else:
            placar[1] += 1
        imprimirTabuleiro()
        return True
    else:
        tabuleiro[celula[0]][celula[1]] = '0'
        imprimirTabuleiro()
        return False


#Função para ordenar ataque do PC.

def logicaPc():
    global flag
    global sentidoTiroBarco
    global atingiuBarco
    if flag == 0:
        x = random.randint(0, tamanho_tabuleiro-1)
        y = random.randint(0, tamanho_tabuleiro-1)
        celulaTiroPC = [x, y]
        tentativa.append(celulaTiroPC)
        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
        if atingiuBarco:
            flag = 1

    while atingiuBarco:
        if flag == 1:
            if sentidoTiroBarco == 'direita':
                celulaTiroPC = tentativa[-1] #[2,3]
                celulaTiroPC[1] += 1 #[2, 4]
                if celulaTiroPC[1] >= tamanho_tabuleiro: # analisando se saiu da parte direita do tabuleiro
                    sentidoTiroBarco = 'esquerda'
                    celulaTiroPC[1] -= 2
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        sentidoTiroBarco = 'cima'
                        return
                    else:
                        flag = 2
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        sentidoTiroBarco = 'esquerda'
                        flag = 2
                        return
                    else:
                        sentidoTiroBarco = 'direita'
            elif sentidoTiroBarco == 'esquerda':
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[1] -= 1
                if celulaTiroPC[1] < 0: # analisando se saiu da parte esquerda do tabuleiro
                    sentidoTiroBarco = 'cima'
                    celulaTiroPC[1] = 0
                    tentativa.append(celulaTiroPC)
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        celulaTiroPC[1] = 0
                        tentativa.append(celulaTiroPC)
                        sentidoTiroBarco = 'cima'
            elif sentidoTiroBarco == 'cima':
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] -= 1
                if celulaTiroPC[0] < 0:  # analisando se saiu da parte superior do tabuleiro
                    sentidoTiroBarco = 'baixo'
                    celulaTiroPC[0] += 2
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:  # Pode servir se quiser implementar barcos tamanho 1. Agora não precisa.
                        flag = 0
                        return
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        sentidoTiroBarco = 'baixo'
                        flag = 2
                        return
            elif sentidoTiroBarco == 'baixo':
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] += 1
                if celulaTiroPC[0] >= tamanho_tabuleiro:  # analisando se saiu da parte superior do tabuleiro
                    sentidoTiroBarco = 'direita'
                    celulaTiroPC[0] -= 1
                    tentativa.append(celulaTiroPC)
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        celulaTiroPC[0] += 1
                        tentativa.append(celulaTiroPC)
                        sentidoTiroBarco = 'direita'
                        flag = 2
                        return
        if flag == 2:
            if sentidoTiroBarco == 'direita':
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[1] += 1
                if celulaTiroPC[1] >= tamanho_tabuleiro:
                    flag = 0
                    break
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        flag = 0
                        return
            elif sentidoTiroBarco == 'esquerda':
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[1] -= 1
                if celulaTiroPC[1] < 0:
                    flag = 0
                    break
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        flag = 0
                        return
            elif sentidoTiroBarco == 'cima':
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] -= 1
                if celulaTiroPC[0] < 0:
                    flag = 0
                    break
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        flag = 0
                        return
            elif sentidoTiroBarco == 'baixo':
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] += 1
                if celulaTiroPC[0] >= tamanho_tabuleiro:
                    flag = 0
                    break
                else:
                    tentativa.append(celulaTiroPC)
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')
                    if not atingiuBarco:
                        flag = 0
                        return


# Main
construirTabuleiro(tamanho_tabuleiro, tabuleiroJogador)
construirTabuleiro(tamanho_tabuleiro, tabuleiroPc)

barco = [3, 'horizontal']
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
celula = [2, 2]
posicionarBarco(tabuleiroJogador, celula, barco)

CPUBarcos()

posicaoTiro = [2, 2]
tiro(tabuleiroPc, posicaoTiro, 'jogador')
logicaPc()

posicaoTiro = [1, 1]
tiro(tabuleiroPc, posicaoTiro, 'jogador')
logicaPc()

posicaoTiro = [3, 3]
tiro(tabuleiroPc, posicaoTiro, 'jogador')
logicaPc()

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
