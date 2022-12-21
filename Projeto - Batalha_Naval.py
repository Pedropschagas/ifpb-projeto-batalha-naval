import os
import random # importando a biblioteca para randomizar números
import time

titulo = ''
tabuleiroPc = []
tabuleiroJogador = []
tamanho_tabuleiro = 0  # entrada do tamanho do tabuleiro.
caractereBarco = '🚢'
caractereRedor = '-'
caractereAgua = '🟦'
caractereAcerto = '💥'
caractereErro = '❌'
barco = [0, '']
celula = [0, 0]
tamanhoDosBarcos = [5, 5, 4, 4, 4, 3, 2, 2]
tamanhoMaxBarco = []
placar = [0, 0]
flag = 'random'
atingiuBarco = False
tentativa = []
sentidoTiroBarco = 'direita'
sentidoTiro = 'direita'
pontosGanhador = 0

def limparTela():
    os.system('cls')

# Laço construtor de tabuleiro.
def construirTabuleiro(tamanho_tabuleiro, tabuleiro):
    for i in range(tamanho_tabuleiro):
        lista = []
        for j in range(tamanho_tabuleiro):
            lista.append(caractereAgua)
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
    print('    ', end='')
    for i in range(1, limite):        
        if i < 9:
            print(i, end='  ')
        else:
            print(i, end=' ')
    print(limite, end=' ')
    if tamanho_tabuleiro > 10:
        for i in range(11, tamanho_tabuleiro + 1):
            print(i, end=' ')
    if limite < 10:
        print('                ', end='')
    else:
        print('              ', end='')
    for i in range(1, limite):        
        if i < 9:
            print(i, end='  ')
        else:
            print(i, end=' ')
    print(limite, end=' ')
    if tamanho_tabuleiro > 10:
        for i in range(11, tamanho_tabuleiro + 1):
            print(i, end=' ')
    print()
    for i in range(tamanho_tabuleiro):
        print(referenciaLetra[i], end='  ')
        for j in range(tamanho_tabuleiro):
            if tabuleiroJogador[i][j] == caractereRedor:
                print(caractereAgua, end=' ')
            else:
                print(tabuleiroJogador[i][j], end=' ')
        print('   ||    ', referenciaLetra[i], end='  ')
        for j in range(tamanho_tabuleiro):
            if tabuleiroPc[i][j] == caractereRedor or tabuleiroPc[i][j] == caractereBarco:
                print(caractereAgua, end=' ')
            else:
                print(tabuleiroPc[i][j], end=' ')
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
    print('    ', end='')
    for i in range(1, limite):
        if i < 9:
            print(i, end='  ')
        else:
            print(i, end=' ')
    print(limite, end=' ')
    if tamanho_tabuleiro > 10:
        for i in range(11, tamanho_tabuleiro + 1):
            print(i, end=' ')
            
    print()

    for i in range(tamanho_tabuleiro):
        print(referenciaLetra[i], end='  ')
        for j in range(tamanho_tabuleiro):
            if tabuleiroJogador[i][j] == caractereRedor:
                print(caractereAgua, end=' ')
            else:
                print(tabuleiroJogador[i][j], end=' ')
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
    if atirador != "jogador":
        print("       !!!  PC Atirando na posição", chr(celula[0] + 65), celula[1]+1, "  !!!")
        # print(flag, "->",sentidoTiro)
        time.sleep(2)
    if tabuleiro[celula[0]][celula[1]] == caractereBarco:
        tabuleiro[celula[0]][celula[1]] = caractereAcerto
        if atirador == 'jogador':
            placar[0] += 1
        else:
            placar[1] += 1
        imprimirTabuleiro()
        return 1
    else:
        if tabuleiro[celula[0]][celula[1]] == caractereAcerto or tabuleiro[celula[0]][celula[1]] == caractereErro:            
            imprimirTabuleiro()
            print("Tentou atirar em um local já atacado, tente novamente!")
            time.sleep(2)
            return 2
        tabuleiro[celula[0]][celula[1]] = caractereErro
        imprimirTabuleiro()        
        return 0

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
def logicaPc(vezdoPC):
    global flag
    global sentidoTiroBarco
    global atingiuBarco
    global sentidoTiro

    while vezdoPC:
        if flag == "random":
            x = random.randint(0, tamanho_tabuleiro-1)
            y = random.randint(0, tamanho_tabuleiro-1)
            celulaTiroPC = [x, y]
            tentativa.append(celulaTiroPC)
            atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, 'pc')            
            if atingiuBarco == 1:
                flag = "procurar_sentido"
            else:
                return
        elif flag == "procurar_sentido":                # procurando sentido do barco
            if sentidoTiro == "direita":                # direção do tiro a ser dado
                celulaTiroPC = tentativa[-1]            # última posição das tentativas
                celulaTiroPC[1] += 1                    # incrementando a posição do tiro pra direita
                if celulaTiroPC[1] < tamanho_tabuleiro: # verificando se o tiro não vai passar do tamanho do tabuleiro
                    tentativa.append(celulaTiroPC)      # adiciona a tentativa
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") # dá um tiro
                    if atingiuBarco == 1:                        
                        flag = "sentido_horizontal"     # se o navio for atingido, o sentido do mesmo é horizontal
                    else:                        
                        celulaTiroPC[1] -= 1            # retorna para o estado inicial, onde o barco foi localizado
                        tentativa.append(celulaTiroPC)  # insere o estado inicial as tentativas 
                        sentidoTiro = "esquerda"
                        return                          # encerra a função para o jogador dar seu tiro
                else:                                   # se não conseguir dar o tiro por causa do tamanho do tabuleiro                        
                    celulaTiroPC[1] -= 1                # retorna para o estado inicial, onde o barco foi localizado
                    tentativa.append(celulaTiroPC)      # insere o estado inicial as tentativas 
                    sentidoTiro = "esquerda"            # muda o sentido do tiro para o lado oposto
            elif sentidoTiro == "esquerda":           
                celulaTiroPC = tentativa[-1]            
                celulaTiroPC[1] -= 1                    
                if celulaTiroPC[1] >= 0:                 # verificando se o tiro não vai passar do tamanho do tabuleiro, nesse caso para a esquerda
                    tentativa.append(celulaTiroPC)      
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                    if atingiuBarco == 1:                        
                        flag = "sentido_horizontal"     
                    else:                        
                        celulaTiroPC[1] += 1            
                        tentativa.append(celulaTiroPC)
                        flag = "sentido_vertical"
                        sentidoTiro = "cima"
                        return                 
                else:                                                      
                    celulaTiroPC[1] += 1                
                    tentativa.append(celulaTiroPC) 
                    sentidoTiro = "cima"                # muda o sentido do tiro para cima
            elif sentidoTiro == "cima":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] -= 1                    
                if celulaTiroPC[0] >= 0:
                    tentativa.append(celulaTiroPC)      
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                    if atingiuBarco == 1:                        
                        flag = "sentido_vertical"     
                    else:                        
                        celulaTiroPC[0] += 1            
                        tentativa.append(celulaTiroPC)  
                        sentidoTiro = "baixo"
                        return                 
                else:                                                      
                    celulaTiroPC[0] += 1                
                    tentativa.append(celulaTiroPC)      
                    sentidoTiro = "baixo"
            elif sentidoTiro == "baixo":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] += 1                    
                if celulaTiroPC[0] < tamanho_tabuleiro:
                    tentativa.append(celulaTiroPC)      
                    atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                    if atingiuBarco == 1:                        
                        flag = "sentido_vertical"     
                    else:                        
                        celulaTiroPC[0] -= 1 
                        tentativa.append(celulaTiroPC)  
                        sentidoTiro = "direita"
                        return                 
                else:                                                      
                    celulaTiroPC[0] -= 1
                    tentativa.append(celulaTiroPC)      
                    sentidoTiro = "direita"
        elif flag == "sentido_horizontal":
            if sentidoTiro == "direita":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[1] += 1
                if celulaTiroPC[1] >= tamanho_tabuleiro or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:                  
                    flag = "inicio_navio_encontrado"
                    sentidoTiro = "esquerda"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto:                        
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "inicio_navio_encontrado"
                            sentidoTiro = "esquerda"
                            return
            if sentidoTiro == "esquerda":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[1] -= 1
                if celulaTiroPC[1] < 0 or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:                  
                    flag = "inicio_navio_encontrado"
                    sentidoTiro = "direita"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto:                        
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "inicio_navio_encontrado"
                            sentidoTiro = "direita"
                            return
        elif flag == "sentido_vertical":
            if sentidoTiro == "cima":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] -= 1
                if celulaTiroPC[0] < 0 or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:                  
                    flag = "inicio_navio_encontrado"
                    sentidoTiro = "baixo"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto:                        
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "inicio_navio_encontrado"
                            sentidoTiro = "baixo"
                            return
            if sentidoTiro == "baixo":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] += 1
                if celulaTiroPC[0] >= tamanho_tabuleiro or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:                  
                    flag = "inicio_navio_encontrado"
                    sentidoTiro = "cima"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto:                        
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "inicio_navio_encontrado"
                            sentidoTiro = "cima"
                            return
                        
        elif flag == "inicio_navio_encontrado":
            if sentidoTiro == "direita":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[1] += 1
                if celulaTiroPC[1] >= tamanho_tabuleiro or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:
                    flag = "random"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto: 
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "random"
                            return
                        
            if sentidoTiro == "esquerda":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[1] -= 1
                if celulaTiroPC[1] < 0 or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:
                    flag = "random"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto: 
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "random"
                            return
                        
            if sentidoTiro == "cima":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] -= 1
                if celulaTiroPC[0] < 0 or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:
                    flag = "random"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto: 
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "random"
                            return
                        
            if sentidoTiro == "baixo":
                celulaTiroPC = tentativa[-1]
                celulaTiroPC[0] += 1
                if celulaTiroPC[0] >= tamanho_tabuleiro or tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereErro:
                    flag = "random"
                else:
                    if not tabuleiroJogador[celulaTiroPC[0]][celulaTiroPC[1]] == caractereAcerto: 
                        tentativa.append(celulaTiroPC)      
                        atingiuBarco = tiro(tabuleiroJogador, celulaTiroPC, "pc") 
                        if atingiuBarco == 0:
                            flag = "random"
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

        if tiro(tabuleiroPc, celula, "jogador") == 0 :
            logicaPc(True)
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
    print(caractereAcerto, " = barco atingido")
    print(caractereErro, " = tiro na água")
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
    print("Você poderá posicionar", len(tamanhoMaxBarco), "Navios!!")
    print("O navio, quando na horizontal, será posicionado da esquerda para direita.")
    print("O navio, quando na vertical, será posicionado de cima para baixo.")
    print("Não poderão haver Navios adjacentes.")
    print("Escolha a orientação do seu navio de tamanho", tamanho, "agora.")

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
