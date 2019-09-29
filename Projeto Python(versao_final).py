# Projeto de Estrutura de Dados
# CONTROLE DE SALAS

#---------------------- FAZER MAIS TESTES COM FUNCIONALIDADES 02 E 03 -----------------

# LISTAS DE DADOS DO SOCIO
nome_completo = []
nome_socio = []
cpf_socio = []

# MATRIZES DAS SALAS/MES
sala01 = [list(range(24)) for i in range(31)]
sala02 = [list(range(24)) for i in range(31)]
sala03 = [list(range(24)) for i in range(31)]

# LISTAS DE RESERVA:
reservaID = []
socio_reservado = []
diaBanco = []
horarioBanco = []
salaBanco = []

#  VARIAVEIS 
identificador = 0
num = 1  
entrada = 0  
var1 = 1    
var2 = 2
var3 = 3    

# -----------------------------------------------------------------------------------------
# --------------------------FUNÇÕES-DE-TRATAMENTO-DE-DADOS---------------------------------
# -----------------------------------------------------------------------------------------
# Tratamento_de_string
def tratamento_dados_string(var):
    while not (var.isalpha()):
        var = input("Digite somente as letras da opçao: ")
    return var

# Tratamento_de_inteiro
def tratamento_dados_inteiro(var):
    while not (var.isdecimal()):
        var = input("Digite somente os números:")
    return int(var)

# Tratamento_booleano
def tratamento_dados_booleano(var):
    while not ((var == 'S') or (var == 's') or (var == 'N') or (var == 'n')):
        var = input("Digite SOMENTE S para confirmar ou N para cancelar: ")
    if (var == 'S') or (var == 's') :
        var = True
    else:
        var = False
    return var

# -----------------------------------------------------------------------------------------
# --------------------------------FUNCIONALIDADES------------------------------------------
#-----------------------------------------------------------------------------------------

# CADASTRAR SÓCIO 

def cadastro_socio():
    print("--------------------")
    print("MENU CADASTRO: ")
    print("--------------------")
    print("Digite seu nome: ")
    nome = tratamento_dados_string(input('Nome: '))
    nome_socio.append(nome)
    print("--------------------")
    nome_final = tratamento_dados_string(input('Ultimo nome: '))
    #ultimo_nome_socio.append(nome_final)
    nome_completo.append(nome + ' '+ nome_final) #TESTE...
    print("--------------------")
    cpf = tratamento_dados_inteiro(input('CPF: '))
    cpf_socio.append(cpf)
    print("-----------------------------------------\n")
    print("Cadastro realizado com Sucesso!\n")
    print("-----------------------------------------")

# REALIZAR RESERVA DE UMA SALA
def reserva_horario(ID):   # TESTES FEITOS, FUNCIONANDO!!!
    print("MENU RESERVA: ")
    nome = tratamento_dados_string(input('Nome do Socio: '))
    # verificação_do_socio
    if nome in nome_socio:
        dia = tratamento_dados_inteiro(input('Digite o dia:'))
        horario = tratamento_dados_inteiro(input("Digite o horario, inteiro de 0 a 23:"))
        sala = tratamento_dados_inteiro(input('Sala 1, 2 ou 3: '))
    # Verificação_de_horario_disponivel
        if (sala == 1):
            if isinstance(sala01[dia - 1][horario], int):
                ID += 1
                reservaID.append(ID)
                socio_reservado.append(nome)
                diaBanco.append(dia)
                horarioBanco.append(horario)
                salaBanco.append(sala)
                verificação = [nome, ID] 
                sala01[dia - 1].insert(horario, verificação)  
                sala01[dia - 1].pop(horario + 1)
                print("Reserva feita com sucesso!")
                return ID
            else:
                print("Esse horario e sala ja esta reservado")
        elif (sala == 2):
            if isinstance(sala02[dia - 1][horario], int):
                ID += 1
                reservaID.append(ID)
                socio_reservado.append(nome)
                diaBanco.append(dia)
                horarioBanco.append(horario)
                salaBanco.append(sala)
                verificação = [nome, ID]
                sala02[dia - 1].insert(horario, verificação)  
                sala02[dia - 1].pop(horario + 1)
                print("Reserva feita com sucesso!")
                return ID
            else:
                print("Esse horario e sala ja esta reservado")
        elif (sala == 3):
            if isinstance(sala03[dia - 1][horario], int):
                ID += 1
                reservaID.append(ID)
                socio_reservado.append(nome)
                diaBanco.append(dia)
                horarioBanco.append(horario)
                salaBanco.append(sala)
                verificação = [nome, ID]
                sala03[dia - 1].insert(horario, verificação)  
                sala03[dia - 1].pop(horario + 1)
                print("Reserva feita com sucesso!")
                return ID
            else:
                print("Esse horario e sala ja esta reservado")

    else:
        print("Socio não encontrado no sistema!\nPor favor, cadastre o sócio antes realizar a reserva.")

# Remover_reserva
def remover_reserva(): # REFAZER ALGUNS TESTES COM TODAS AS SALAS!!!
    print('\nRESERVA ATUAL:')
    nome = tratamento_dados_string(input('Nome do Socio cadastrado: '))
    if nome in nome_socio:
        dia = tratamento_dados_inteiro(input('Digite o dia:'))
        horario = tratamento_dados_inteiro(input("Digite o horario, inteiro de 0 a 23:"))
        sala = tratamento_dados_inteiro(input('Sala 1, 2 ou 3: '))
        if (sala == 1):
            if isinstance(sala01[dia - 1][horario], list):
                if (sala01[dia - 1][horario][0] == nome):
                    ID = sala01[dia - 1][horario][1]
                    indice = reservaID.index(ID) # Segundo meu entendimento isso nao é para dar erro no metodo index
                    socio_reservado.pop(indice)
                    diaBanco.pop(indice)
                    horarioBanco.pop(indice)
                    salaBanco.pop(indice)  
                    reservaID.pop(indice)
                    sala01[dia - 1].pop(horario)
                    #print(sala01[dia - 1])
                    sala01[dia - 1].insert(horario, horario)
                    #print(sala01[dia - 1])
                    print("Reserva removida com sucesso")
                
                else:
                    print("Esse essa sala e horario não esta reservado para esse socio")
            else:
                print("Este horario esta disponivel")
        
        elif (sala == 2):
            if isinstance(sala02[dia - 1][horario], list):
                if (sala02[dia - 1][horario][0] == nome):
                    ID = sala02[dia - 1][horario][1]
                    indice = reservaID.index(ID)
                    socio_reservado.pop(indice)
                    diaBanco.pop(indice)
                    horarioBanco.pop(indice)
                    salaBanco.pop(indice)
                    reservaID.pop(indice)
                    sala02[dia - 1].pop(horario)
                    sala02[dia - 1].insert(horario, horario)
                    print("Reserva removida com sucesso")
                else:
                    print("Esse essa sala e horario não esta reservado para esse socio")
            else:
                print("Este horario esta disponivel")
        
        elif (sala == 3):
            if isinstance(sala03[dia - 1][horario], list):
                if (sala03[dia - 1][horario][0] == nome):
                    ID = sala03[dia - 1][horario][1]
                    indice = reservaID.index(ID)
                    socio_reservado.pop(indice)
                    diaBanco.pop(indice)
                    horarioBanco.pop(indice)
                    salaBanco.pop(indice)
                    reservaID.pop(indice)
                    sala03[dia - 1].pop(horario)
                    sala03[dia - 1].insert(horario, horario)
                    print("Reserva removida com sucesso")
                else:
                    print("Esse essa sala e horario não esta reservado para esse socio")
            else:
                print("Este horario esta disponivel")
            
    else:
        print("\nSocio não cadastrado no sistema!\nPor favor, cadastre o socio antes fazer a reserva.")
        
# Pesquisar horarios disponiveis
def pesquisar_disponibilidade():  # NAO PRECISA SER ALTERADA...
    print("Disponibilidade de horarios:")
    dia = tratamento_dados_inteiro(input('Digite o dia:'))
    horario = tratamento_dados_inteiro(input("Digite o horario, inteiro de 0 a 23:"))
    if isinstance(sala01[dia - 1][horario], int):
        print("\nSALA 01 HORARIO DISPONIVEL")
    else:
        print("\nSALA 01 HORARIO NÃO DISPONIVEL")
    if isinstance(sala02[dia - 1][horario], int):
        print("\nSALA 02 HORARIO DISPONIVEL")
    else:
        print("\nSALA 02 HORARIO NÃO DISPONIVEL")
    if isinstance(sala03[dia - 1][horario], int):
        print("\nSALA 03 HORARIO DISPONIVEL")
    else:
        print("\nSALA 01 HORARIO NÃO DISPONIVEL")

# Pesquisar por reservar do sócio no dia    
def pesquisar_reserva(): # FUNCIONANDO
    print("Pesquisa de reservas no dia:")
    contSala01 = 0
    contSala02 = 0
    contSala03 = 0
    nome = tratamento_dados_string(input('Nome do Socio cadastrado: '))
    if (nome in nome_socio):
        dia = tratamento_dados_inteiro(input('Digite o dia:'))
        for i in sala01[dia -1]:
            if isinstance(i, list):
                if (i[0] == nome):
                    print("Reserva do socio {} as {} hora(s) na sala 01".format(i[0], contSala01))
                    contSala01 = contSala01 + 1
                else:
                    contSala01 = contSala01 + 1
            else:
                contSala01 = contSala01 + 1    
        for p in sala02[dia -1]:
            if isinstance(p, list):
                if (p[0] == nome):
                    print("Reserva do socio {} as {} hora(s) na sala 02".format(p[0], contSala02))
                    contSala02 = contSala02 + 1
                else:
                    contSala02 = contSala02 + 1
            else:
                contSala02 = contSala02 + 1
        for k in sala03[dia -1]:
            if isinstance(k, list):
                if (k[0] == nome):
                    print("Reserva do socio {} as {} hora(s) na sala 03".format(k[0], contSala03))
                    contSala03 = contSala03 + 1
                else:
                    contSala03 = contSala03 + 1
            else:
                contSala03 = contSala03 + 1
    else:
        print("\nSocio não cadastrado no sistema!\n Por favor, cadastre o socio antes fazer a reserva.")    

# Alterar reserva para outro socio cadastrado        
def alterar_socio():  # FUNCIONANDO, FAZER MAIS TESTES DEPOIS!!!
    print("ALTERAR SOCIO DA RESERVA:")
    nome = tratamento_dados_string(input('Nome do socio reservado: '))
    if (nome in nome_socio):
        dia = tratamento_dados_inteiro(input('Digite o dia:'))
        horario = tratamento_dados_inteiro(input("Digite o horario, inteiro de 0 a 23:"))
        sala = tratamento_dados_inteiro(input('Sala 1, 2 ou 3: '))
        if (sala == 1):
            if isinstance(sala01[dia -1][horario], list):
                if (sala01[dia -1][horario][0] == nome):
                    print("Horario reservado para o socio {}".format(nome))
                    confirmacao = tratamento_dados_booleano(input("Vc deseja mesmo ALTERAR a reserva s/n ?"))
                    if (confirmacao == True):
                        nome_novo = tratamento_dados_string(input('Agora digite o nome do novo socio para efetuar a alteração: '))
                        ID = sala01[dia -1][horario][1]
                        indice = reservaID.index(ID)
                        socio_reservado.pop(indice)
                        socio_reservado.insert(indice, nome_novo)
                        sala01[dia - 1][horario].pop(0)
                        sala01[dia - 1][horario].insert(0, nome_novo)
                        print("Alteração feita com sucesso!")
                    else:
                        print("Operação cancelada pelo usuario!")
                else:
                    print("Horario nao esta resevado para o socio {}\nPor favor verifique a(s) reserva(s) do socio nesse dia".format(nome))   
            else: 
                print("Esse horário está disponível!")
        
        elif (sala == 2):
            if isinstance(sala02[dia -1][horario], list):
                if (sala02[dia -1][horario][0] == nome):
                    print("Horario reservado para o socio {}".format(nome))
                    confirmacao = tratamento_dados_booleano(input("Vc deseja mesmo ALTERAR a reserva s/n ?"))
                    if (confirmacao == True):
                        nome_novo = tratamento_dados_string(input('Agora digite o nome do novo socio para efetuar a alteração: '))
                        ID = sala02[dia -1][horario][1]
                        indice = reservaID.index(ID)
                        socio_reservado.pop(indice)
                        socio_reservado.insert(indice, nome_novo)
                        sala02[dia - 1][horario].pop(0)
                        sala02[dia - 1][horario].insert(0, nome_novo)
                        print("Alteração feita com sucesso!")
                    else:
                        print("Operação cancelada pelo usuario!")
                else:
                     print("Horario nao esta resevado para o socio {}\nPor favor verifique a(s) reserva(s) do socio nesse dia".format(nome))   
            else: 
                 print("Esse horário está disponível!")        
        elif (sala == 3):
            if isinstance(sala03[dia -1][horario], list):
                if (sala03[dia -1][horario][0] == nome):
                    print("Horario reservado para o socio {}".format(nome))
                    confirmacao = tratamento_dados_booleano(input("Vc deseja mesmo ALTERAR a reserva s/n ?"))
                    if (confirmacao == True):
                        nome_novo = tratamento_dados_string(input('Agora digite o nome do novo socio para efetuar a alteração: '))
                        ID = sala03[dia -1][horario][1]
                        indice = reservaID.index(ID)
                        socio_reservado.pop(indice)
                        socio_reservado.insert(indice, nome_novo)
                        sala03[dia - 1][horario].pop(0)
                        sala03[dia - 1][horario].insert(0, nome_novo)
                        print("Alteração feita com sucesso!")
                    else:
                        print("Operação cancelada pelo usuario!")
                else:
                    print("Horario nao esta resevado para o socio {}\nPor favor verifique a(s) reserva(s) do socio nesse dia".format(nome))   
            else: 
                print("Esse horário está disponível!")    

# Pedir o nome, verificar o a reserva e depois alterar o horario         
def alterar_horario(): # ACHEI UMA FALHA MAS JA IMPLEMENTEI NA SALA 01, FALTA O RESTO...
    print("Digite os dados da reserva:\n")
    nome = tratamento_dados_string(input('Nome: '))
    if (nome in nome_socio):
        dia = tratamento_dados_inteiro(input('Digite o dia:'))
        horario = tratamento_dados_inteiro(input("Digite o horario, inteiro de 0 a 23:"))   # diaBanco = []horarioBanco = []salaBanco = []
        sala = tratamento_dados_inteiro(input('Sala 1, 2 ou 3: '))
        if (sala == 1):
            if isinstance(sala01[dia -1][horario], list):
                if (sala01[dia -1][horario][0] == nome):
                    ID = sala01[dia -1][horario][1]
                    indice = reservaID.index(ID)
                    # PRINTAR OS DADOS ANTES CONFIRMAR
                    print("Dados: sócio {}, dia {}, sala {}, horario {}".format(socio_reservado[indice], diaBanco[indice], salaBanco[indice], horarioBanco[indice]))
                    confirmacao = tratamento_dados_booleano(input("Vc deseja mesmo ALTERAR a reserva s/n ?"))
                    if (confirmacao == True):
                        horario_novo = tratamento_dados_inteiro(input("Digite o novo horario entre 0 a 23:"))
                        if isinstance(sala01[dia -1][horario_novo], int):
                            # TESTANDO...
                            horarioBanco.pop(indice)
                            horarioBanco.insert(indice, horario_novo)
                            # Deixar o horario antigo normalmente
                            sala01[dia - 1].pop(horario)
                            sala01[dia - 1].insert(horario, horario)
                            # Colocar o novo horario
                            verificacao =[nome, ID]
                            sala01[dia - 1].pop(horario_novo)
                            sala01[dia - 1].insert(horario_novo, verificacao)
                            print("Alteração feita com sucesso!")
                        else:
                            print("Esse horario já esta reservado!")
                    else:
                        print("Operação cancelada pelo usuario!")
                else:
                    print("Horario nao esta resevado para o socio {}\nPor favor verifique a(s) reserva(s) do socio nesse dia".format(nome))   
            else: 
                print("Esse horário está disponível!")
                
        elif (sala == 2):
            if isinstance(sala02[dia -1][horario], list):
                if (sala02[dia -1][horario][0] == nome):
                    ID = sala02[dia -1][horario][1]
                    indice = reservaID.index(ID)
                    # PRINTAR OS DADOS ANTES CONFIRMAR
                    print("Dados: sócio {}, dia {}, sala {}, horario {}".format(socio_reservado[indice], diaBanco[indice], salaBanco[indice], horarioBanco[indice]))
                    confirmacao = tratamento_dados_booleano(input("Vc deseja mesmo ALTERAR a reserva s/n ?"))
                    if (confirmacao == True):
                        horario_novo = tratamento_dados_inteiro(input("Digite o novo horario entre 0 a 23:"))
                        if isinstance(sala02[dia -1][horario_novo], int):
                            # TESTANDO...
                            horarioBanco.pop(indice)
                            horarioBanco.insert(indice, horario_novo)
                            # Deixar o horario antigo normalmente
                            sala01[dia - 1].pop(horario)
                            sala01[dia - 1].insert(horario, horario)
                            # Colocar o novo horario
                            verificacao =[nome, ID]
                            sala02[dia - 1].pop(horario_novo)
                            sala02[dia - 1].insert(horario_novo, verificacao)
                            print("Alteração feita com sucesso!")
                        else:
                            print("Esse horario já esta reservado!")
                    else:
                        print("Operação cancelada pelo usuario!")
                else:
                    print("Horario nao esta resevado para o socio {}\nPor favor verifique a(s) reserva(s) do socio nesse dia".format(nome))   
            else: 
                print("Esse horário está disponível!")
        elif (sala == 3):
            if isinstance(sala03[dia -1][horario], list):
                if (sala03[dia -1][horario][0] == nome):
                    ID = sala03[dia -1][horario][1]
                    indice = reservaID.index(ID)
                    # PRINTAR OS DADOS ANTES CONFIRMAR
                    print("Dados: sócio {}, dia {}, sala {}, horario {}".format(socio_reservado[indice], diaBanco[indice], salaBanco[indice], horarioBanco[indice]))
                    confirmacao = tratamento_dados_booleano(input("Vc deseja mesmo ALTERAR a reserva s/n ?"))
                    if (confirmacao == True):
                        horario_novo = tratamento_dados_inteiro(input("Digite o novo horario entre 0 a 23:"))
                        if isinstance(sala03[dia -1][horario_novo], int):
                            # TESTANDO...
                            horarioBanco.pop(indice)
                            horarioBanco.insert(indice, horario_novo)
                            # Deixar o horario antigo normalmente
                            sala03[dia - 1].pop(horario)
                            sala03[dia - 1].insert(horario, horario)
                            # Colocar o novo horario
                            verificacao =[nome, ID]
                            sala03[dia - 1].pop(horario_novo)
                            sala03[dia - 1].insert(horario_novo, verificacao)
                            print("Alteração feita com sucesso!")
                        else:
                            print("Esse horario já esta reservado!")
                    else:
                        print("Operação cancelada pelo usuario!")
                else:
                    print("Horario nao esta resevado para o socio {}\nPor favor verifique a(s) reserva(s) do socio nesse dia".format(nome))   
            else: 
                print("Esse horário está disponível!")
                
# Relatorio de reservas
def listar_relatorio(): # FUNCIONANDO
    print("Relatorio das reservas:\n")
    for i in range(len(reservaID)):
        print("Reserva {}°".format(i+1))
        print("Socio: {}".format(socio_reservado[i]))
        print("Dia: {}".format(diaBanco[i]))
        print("Horario: {} horas".format(horarioBanco[i]))
        print("Sala: {}\n".format(salaBanco[i]))
        

#---------------------  Funções de leitura e salvando dados ----------------------------
        
def lendo_reserva(): # tentar tira o global e usar os parametros...
    arquivo = open("dados_reserva.txt")
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    linha4 = arquivo.readline()
    linha5 = arquivo.readline()
    linha6 = arquivo.readline()

    global reservaID, socio_reservado, diaBanco, horarioBanco, salaBanco, identificador # melhorar isso depois...
    
    reservaID = linha1.split(',')
    reservaID.pop()
    socio_reservado = linha2.split(',')
    socio_reservado.pop()
    diaBanco = linha3.split(',')
    diaBanco.pop()
    horarioBanco = linha4.split(',')
    horarioBanco.pop()
    salaBanco = linha5.split(',')
    salaBanco.pop()
    converter = linha6  # melhorar isso depois...
    identificador = int(converter)
    arquivo.close()

def lendo_cadastro():  # TESTAR LEITURA SEM O METODO GLOBAL
    arquivo = open('dados_cadastro.txt')
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    global nome_socio, cpf_socio
    nome_socio = linha1.split(',')
    nome_socio.pop()
    cpf_socio = linha2.split(',')
    cpf_socio.pop()
    arquivo.close()


def lendo_Matrizes(numl,sala):  # IMPLEMENTADO MAS AINDA FALTA FAZER ALGUNS TESTES
    # LENDO UMA LINHA TXT, OU UM DIA DO VETOR SALA/MES
    arquivo = open('dados_matrizes{}.txt'.format(numl))
    def ler_linha(n):
        linha = arquivo.readline()
        linha.strip()
        print(linha)
        vetor = linha.split(",")
        vetor.pop()
        sala.pop(n)
        sala.insert(n, []) # ERRO  PODE SER AQUI..
        ver = []            # ERRO  PODE SER AQUI..
        #print(vetor)
        for i in vetor: 
            try:
                sala[n].append(int(i))
            except:         # DEU CERTO MAS NAO ESTOU ANIMADO COM ESSE CODIGO...
                ver.append(i.split("-"))
                for k in ver:
                    nome = k[0]
                    ident = int(k[1])
                    vet_temp = [nome, ident]
                    sala[n].append(vet_temp)
                ver = []
        n += 1
        arquivo.readline()
        if (n<30): 
            ler_linha(n)
        if (n == 30):
            ler_linha(n)
            print("SAINDO DA FUNÇAO RECURSIVA...")
    ler_linha(entrada)        
    arquivo.close()

    
# SALVANDO OS DADOS DAS RESERVAS
def salvar_reserva(): # NAO CHAMAR POR ENQUANTO...
    arquivo = open('dados_reserva.txt', 'w')
    for i in reservaID: # LINHA 01 --> ESCREVENDO (SALVANDO) OS DADOS DA ID RESERVA...
        print(i, end=',', file=arquivo)
    arquivo.write("\n")
    for j in socio_reservado:
        print(j, end=',', file=arquivo)
    arquivo.write("\n")
    for l in diaBanco:
        print(l, end=',', file=arquivo)
    arquivo.write("\n")
    for m in horarioBanco:
        print(m, end=',', file=arquivo)
    arquivo.write("\n")
    for n in salaBanco:
        print(n, end=',', file=arquivo)
    arquivo.write("\n")
    print(identificador, file=arquivo) #salvando o contador do ID
    arquivo.close()

# Salvando os dados do cadastro:
def salvar_cadastro():
    #nome_completo = []
    #ultimo_nome_socio = []
    arquivo = open('dados_cadastro.txt', 'w')
    for i in nome_socio: # LINHA 01 --> ESCREVENDO (SALVANDO) OS DADOS DA ID RESERVA...
        print(i, end=',', file=arquivo)
    arquivo.write("\n")
    for j in cpf_socio:
        print(j, end=',', file=arquivo)
    arquivo.write("\n")
    arquivo.close()
    print("\nDados salvos com sucessos!")

# SALVANDO MATRIZ(sala)
def salvando_matrizes(sala, num_sala): #TESTANDO...
    arquivo_teste = open('dados_matrizes{}.txt'.format(num_sala), 'w')
    cont = 0
    for i in sala:
        for p in i:     
            if isinstance(p, int):
                print(p, end=',', file=arquivo_teste) 
            elif isinstance(p, list): 
                for m in p:
                    if (cont < 1):
                        print(m, end='-', file=arquivo_teste)
                        cont += 1
                    elif (cont == 1):
                        print(m, end=',', file=arquivo_teste)
                        cont = 0
                       
        print("\n", file=arquivo_teste)
    arquivo_teste.close()
    if (num_sala <3):  # SALVAR POR CIMA VARIAS VEZES SEM GERANDO SOMENTE 3 ARQ
        num_sala += 1
        return num_sala
    elif(num_sala >=3):
        num_sala = 1
        return num_sala

# IMPRESSÃO DO MENU DE ESCOLHA
def menu():
    print('=================Menu=================\n'
          '1 - Cadastro do sócio: \n'
          '2 - Realizar reserva de uma sala\n'
          '3 - Remoção da reserva feita pelo sócio\n'
          '4 - Pesquisar por horários livres no dia\n'
          '5 - Pesquisar reserva do socio no dia\n'
          '6 - Alteração do sócio da reserva\n'
          '7 - Alteração do horário da reserva;\n'
          '8 - Listar relatório das reservas\n'
          '9 - Salvar dados da reserva\n'
          '0 - Sair\n'
          '======================================')
 
try:    
    lendo_cadastro()
    lendo_Matrizes(var1, sala01)
    lendo_Matrizes(var2, sala02)
    lendo_Matrizes(var3, sala03)
    lendo_reserva()
except:
    pass
  
# -----------------------------   Estrutura de chamadas das funçoes --------------------------------
menu()
meuMenu = input('Digite a opçao desejada: ')
while (meuMenu == '1') or (meuMenu == '2') or (meuMenu == '3') or (meuMenu == '4') or (meuMenu == '5') or (meuMenu == '6')  or (meuMenu == '7') or (meuMenu == '8') or (meuMenu == '9'):
    if meuMenu == '1':
        cadastro_socio()
        menu()
        meuMenu = input('Digite a opçao desejada: ')

    elif meuMenu == '2':
        identificador = reserva_horario(identificador)
        menu()
        meuMenu = input('Digite a opçao desejada: ')

    elif meuMenu == '3':
        remover_reserva()
        menu()
        meuMenu = input('Digite a opçao desejada: ')

    elif meuMenu == '4':
        pesquisar_disponibilidade()
        menu()
        meuMenu = input('Digite a opçao desejada: ')
        
    elif meuMenu == '5':
        pesquisar_reserva()
        menu()
        meuMenu = input('Digite a opçao desejada: ')
        
    elif meuMenu == '6':
        alterar_socio()
        menu()
        meuMenu = input('Digite a opçao desejada: ')
    
    elif meuMenu == '7':
        alterar_horario()
        menu()
        meuMenu = input('Digite a opçao desejada: ')
        
    elif meuMenu == '8':
        listar_relatorio()
        menu()
        meuMenu = input('Digite a opçao desejada: ')
        
    elif meuMenu == '9':
        salvar_reserva()
        salvar_cadastro()
        num = salvando_matrizes(sala01, num)
        num = salvando_matrizes(sala02, num)
        num = salvando_matrizes(sala03, num)
        menu()
        meuMenu = input('Digite a opçao desejada: ')
    else:
        print("SAINDO DO PROGRAMA")


