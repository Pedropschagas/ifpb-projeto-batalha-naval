import os
import random # importando a biblioteca para randomizar números
import time

titulo = ''
tabuleiroPc = []
tabuleiroJogador = []
tamanho_tabuleiro = 0  # entrada do tamanho do tabuleiro.
caractereBarco = '<'
caractereRedor = '-'
caractereAgua = '*'
barco = [0, '']
celula = [0, 0]
tamanhoDosBarcos = [5, 5, 4, 4, 3, 2, 2]
tamanhoMaxBarco = []
placar = [0, 0]
flag = 0
atingiuBarco = False
tentativa = []
sentidoTiroBarco = 'direita'
pontosGanhador = 0


def limparTela():
    os.system('cls')

# Laço construtor de tabuleiro.
def construirTabuleiro(tamanho_tabuleiro, tabuleiro):
    for i in range(tamanho_tabuleiro):
        lista = []
        for j in range(tamanho_tabuleiro):
            lista.append('*')
        tabuleiro.append(lista)

# função para mostrar tabuleiro na tela
def imprimirTabuleiro():
    limparTela()
    
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|                         BATALHA NAVAL                          |")
    print("|                                                                |")  
    print(f'                   PLACAR ==> JOGADOR {placar[0]} X PC {placar[1]}')  
    print("")
    print("")
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
            if tabuleiroJogador[i][j] == caractereRedor:
                print(caractereAgua, end='  ')
            else:
                print(tabuleiroJogador[i][j], end='  ')
        print('   ||     ', referenciaLetra[i], end='  ')
        for j in range(tamanho_tabuleiro):
            if tabuleiroPc[i][j] == caractereRedor or tabuleiroPc[i][j] == caractereBarco:
                print(caractereAgua, end='  ')
            else:
                print(tabuleiroPc[i][j], end='  ')
        print()
    print()

# funcção para mostrar apenas o tabuleiro do jogador no início do jogo
def imprimirTabuleiroJogador():
    global tamanho_tabuleiro
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
            
    print()

    for i in range(tamanho_tabuleiro):
        print(referenciaLetra[i], end='  ')
        for j in range(tamanho_tabuleiro):
            if tabuleiroJogador[i][j] == caractereRedor:
                print(caractereAgua, end='  ')
            else:
                print(tabuleiroJogador[i][j], end='  ')
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
    global pontosGanhador
    global tamanhoMaxBarco

    for i in tamanhoMaxBarco:
        pontosGanhador += i
        if not (posicionarBarcoCPU(tabuleiroPc, i)):
            print(
                "Número máximo de tentativas para a CPU posicionar barcos estourou, rode o APP novamente!")

# Função que cria uma lista de barcos dependendo do tamanho do tabuleiro escolhido
def tamanhoBarcosEscolhidos ():
    global tamanhoDosBarcos
    global tamanhoMaxBarco
    global tamanho_tabuleiro

    for i in range(len(tamanhoDosBarcos)):
        if tamanho_tabuleiro > 12:
            tamanhoMaxBarco.append(tamanhoDosBarcos[i])
        elif tamanho_tabuleiro > 9 and tamanhoDosBarcos[i] <= 4:
            tamanhoMaxBarco.append(tamanhoDosBarcos[i])
        elif tamanhoDosBarcos[i] <= 3:
            tamanhoMaxBarco.append(tamanhoDosBarcos[i])

# Função para ordenar ataques e placar.
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
        if tabuleiro[celula[0]][celula[1]] == 'X' or tabuleiro[celula[0]][celula[1]] == '0':
            imprimirTabuleiro()
            return False
        tabuleiro[celula[0]][celula[1]] = '0'
        imprimirTabuleiro()
        return False

# Função para verificar o vitorioso
def vitoria():
    global pontosGanhador
    global placar
    if placar[0] == pontosGanhador:
        return 1
    elif placar[1] == pontosGanhador:
        return 2
    return 0

# Função para ordenar ataque do PC.
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

# Função para jogar
def jogando():
    while vitoria() == 0:
        print("Escolha uma coordenada para atacar")

        celula= [0,0]
        entrada = input("Escolha a Linha:").lower()
        try:
            entrada = ord(entrada)-97
        except:
            entrada = -1
        while entrada >= tamanho_tabuleiro or entrada < 0:
            imprimirTabuleiro()
            print("Escolha uma linha válida!")
            entrada = input("Escolha a Linha:").lower()
            try:
                entrada = ord(entrada)-97
            except:
                entrada = -1
        celula[0] = entrada

        try:
            entrada = int(input("Escolha a Coluna:"))
        except:
            entrada = -1
        entrada -= 1
        while entrada >= tamanho_tabuleiro or entrada < 0:
            imprimirTabuleiro()
            print("Escolha uma coluna válida!")
            try:
                entrada = int(input("Escolha a Coluna:"))
            except:
                entrada = -1      
            entrada -= 1
        
        celula[1] = entrada

        if not tiro(tabuleiroPc, celula, "jogador"):
            logicaPc()
        imprimirTabuleiro()
    if vitoria() == 1:
        telaDaVitoriaJogador()
    else:
        telaDaVitoriaPc()

# !!!!!!!!!!!!!!!!!!!!        TELAS DE EXIBIÇÃO        !!!!!!!!!!!!!!!!!
def telaApersentacao():
    limparTela()
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|                                                                |")    
    print("|                       JOGO BATALHA NAVAL                       |")
    print("|                                                                |")    
    print("|                                                                |")    
    print("------------------------------------------------------------------")
    print("                           INSTRUÇÕES:")
    print("Legenda de símbolos e suas representações:")
    print(caractereAgua, " = água")
    print(caractereBarco, " = barco")
    print("X = barco atingido")
    print("0 = tiro na água")
    print("------------------------------------------------------------------")
    print("Pressione ENTER para inciar")

def telaEscolhaTamanhoTabuleiro():
    limparTela()
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|                 ESCOLHA A DIFICULDADE DO JOGO                  |")
    print("|                                                                |")    
    print("------------------------------------------------------------------")
    print("Digite:")
    print("F = Fácil")
    print("M = Moderado")
    print("D = Difícil")

def telaEscolherBarcos(tamanho):
    limparTela()
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|               POSICIONE SEUS BARCOS NO TABULEIRO               |")
    print("|                                                                |")    
    print("------------------------------------------------------------------")
    imprimirTabuleiroJogador()
    print("Você vai escolher a orientação do seu navio de tamanho", tamanho, "agora.")
    print("O navio, quando na horizontal, será posicionado da esquerda para direita.")
    print("O navio, quando na vertical, será posicionado de cima para baixo.")
    print("Não poderão haver Navios adjacentes.")

def telaNaviosJogadorPosicionados():
    limparTela()
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|                                                                |")    
    print("|                     NAVIOS POSICIONADOS!                       |")
    print("|                  PREPARE-SE PARA A BATALHA!                    |")    
    print("|                                                                |")     
    print("|                                                                |")    
    print("------------------------------------------------------------------")
    imprimirTabuleiroJogador()

def telaContagemNaviosPC():
    for i in range(5,-1,-1):
        limparTela()
        print("------------------------------------------------------------------")
        print("|                                                                |")
        print("|                                                                |")    
        print("|                COMPUTADOR POSICIONANDO NAVIOS                  |")
        print("|                                                                |")            
        print("|                             ",i,"                                |")    
        print("|                                                                |")     
        print("|                                                                |")    
        print("------------------------------------------------------------------")
        time.sleep(1)

def telaDaVitoriaJogador():
    limparTela()
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|                                                                |")    
    print("|                            PARABÉNS!                           |")
    print("|                    VOCÊ DERROTOU O INIMIGO!                    |")    
    print("|                                                                |")     
    print("|                                                                |")    
    print("------------------------------------------------------------------")

def telaDaVitoriaPc():
    limparTela()
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|                                                                |")    
    print("|                            PARABÉNS!                           |")
    print("|                          VOCÊ  PERDEU!                         |")    
    print("|                                                                |")     
    print("|                                                                |")    
    print("------------------------------------------------------------------")

def startGame():    
    barco = [0, '']
    celula = [0,0]  


    global tamanho_tabuleiro
    entrada = ""
    telaApersentacao()
    entrada = input().lower()
    print(entrada)
    if entrada != '€³¤€üé®þü³¤€¼üé®þ':
        telaEscolhaTamanhoTabuleiro() 
        entrada = input().lower()
        while True:
            if entrada == 'f':
                tamanho_tabuleiro = 5
                break
            elif entrada == 'm':
                tamanho_tabuleiro = 10
                break
            elif entrada == 'd':
                tamanho_tabuleiro = 15
                break
            else:
                print("Opção Inválida!")
                print("Digite uma opção correta!")                
                entrada = input().lower()
        construirTabuleiro(tamanho_tabuleiro, tabuleiroJogador)
        construirTabuleiro(tamanho_tabuleiro, tabuleiroPc)
        tamanhoBarcosEscolhidos()


        for i in tamanhoMaxBarco:                 
            telaEscolherBarcos(i)
            barco[0] = i       
            while True:                
                while True:                
                    entrada = input("Escolha o sentido (H = horizontal | V = Vertical):").lower()
                    if entrada == 'h':
                        barco[1] = "horizontal"
                        break
                    if entrada == 'v':
                        barco[1] = "vertical"
                        break
                    else:
                        telaEscolherBarcos(i)
                        print("Opção Inválida! Escolha um sentido válido.")


                entrada = input("Escolha a Linha:").lower()
                try:
                    entrada = ord(entrada)-97
                except:
                    entrada = -1
                while entrada >= tamanho_tabuleiro or entrada < 0:
                    telaEscolherBarcos(i)
                    print("Escolha uma linha válida!")
                    entrada = input("Escolha a Linha:").lower()
                    try:
                        entrada = ord(entrada)-97
                    except:
                        entrada = -1
                celula[0] = entrada

                try:
                    entrada = int(input("Escolha a Coluna:"))
                except:
                    entrada = -1
                entrada -= 1
                while entrada >= tamanho_tabuleiro or entrada < 0:
                    telaEscolherBarcos(i)
                    print("Escolha uma coluna válida!")
                    try:
                        entrada = int(input("Escolha a Coluna:"))
                    except:
                        entrada = -1      
                    entrada -= 1
                
                celula[1] = entrada

                if posicionarBarco(tabuleiroJogador, celula, barco):
                    break                                  
                telaEscolherBarcos(i)
                print("Posição inválida! Posicione novamente.")
        
        telaNaviosJogadorPosicionados()

    time.sleep(5)    
    telaContagemNaviosPC()           
    CPUBarcos()
    imprimirTabuleiro()

    jogando()

startGame()
