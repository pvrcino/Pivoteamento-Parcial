import os;

#Variavel global para armazenamento da matriz A
A = [];
#Variavel global para armazenamento da matriz A sem alteracoes pelo pivotamento
raw_A = [];


#Variavel global para armazenamento do vetor b
b = [];
#Variavel global para armazenamento do vetor b sem alteracoes pelo pivotamento
raw_b = [];

#Variavel para armazenamento do numero de variaveis do sistema
n = 0

def clear():
  ''' Funcao para limpar o terminal de execucao dependendo do S.O.
  '''
  os.system('cls' if os.name == 'nt' else 'clear')


def lerMatriz():
  ''' Funcao responsavel para ler o número de variaveis 
      e a matriz A
  '''

  global A; #Chamada da variavel global A.
  global raw_A; #Chamada da variavel global raw_A.

  global n; #Chamada da variavel global n.

  #Solicitacao da quantidade de variaveis e armazenamento na variavel global n.
  n = input("Insira a quantidade de variáveis do sistema linear\n")
  try:
    #Verifica se n é um inteiro
    n = int(n)
    A = []; #Limpa a matriz A.
    clear() #Limpa o terminal.

    #Leitura da matriz A e armazenamento na variavel global A.
    print("Insira a matriz A:")
    for i in range (n):
      leitura = input()
      linha = list(map(float, leitura.split()))
      #Verifica se o tamanho da linha é menor que o numero de variaveis, caso verdadeiro, preenche com o número 0.
      if len(linha) < n: 
        for j in range (len(linha),n):
          linha.append(0.0)
        A.append(linha)

      #Verifica se o tamanho da linha é maior que o numero de variaveis, caso verdadeiro, pede para inserir tudo novamente.
      elif len(linha) > n: 
        clear()
        print("Matriz A estourou o limite de variáveis! ", end = "")
        return lerMatriz()
      else:
        A.append(linha)

    clear() #Limpa o terminal

    #Realiza o print da matriz A e pede pro usuario realizar a confirmacao, caso nao confirmado, pede para inserir tudo novamente.
    print("Matriz A:", end = "")
    for i in range (n):
      print("\n", end = "")
      for j in range (n):
        print(format(A[i][j]) + " ", end="")
    confirm = input("\n\nDigite 1 para CONFIRMAR a matriz A ou qualquer outro número para CANCELAR\n")
    clear() #Limpa o terminal
    if (confirm != "1"):
      lerMatriz()
    else:
      raw_A = A #Armazena a matriz A na variavel raw_A para caso de impressao do sistema futuro após pivoteamento.
  #Caso n nao seja inteiro, pede para digitar o numero de variaveis novamente.
  except ValueError: 
    clear()
    lerMatriz()

def lerVetor():
  ''' Funcao responsavel para ler o vetor b
  '''
  global b; #Chamada da variavel global b.
  global raw_b; #Chamada da variavel global raw_b.

  global n; #Chamada da variavel global n.

  #Leitura do vetor b e armazenamento na variavel global b.
  print("Insira o vetor b:")
  leitura = input()
  b = list(map(float, leitura.split()))

  #Verifica se o tamanho de b é menor que o numero de variaveis, caso verdadeiro, preenche com o numero 0.
  if len(b) < n:
    for j in range (len(b),n):
      b.append(0.0)
  #Verifica se o tamanho de b é maior que o numero de variaveis, caso verdadeiro, pede pro usuario inserir o vetor novamente.
  elif (len(b) > n):
    print("Vetor b estourou o limite de variáveis! ", end = "")
    return lerVetor()

  clear() #Limpa o terminal
  print("Vetor b:")
  #Printa o vetor b e pede confirmacao para o usuario, caso nao confirme, pede para inserir o vetor novamente.
  for i in range (n):
    print(format(b[i]))
  confirm = int(input("\nDigite 1 para CONFIRMAR o vetor b ou qualquer outro número para CANCELAR\n"))
  clear() # Limpa o terminal.
  if (confirm != 1):
    lerVetor()
  else:
    raw_b = b; #Armazena o vetor b na variavel raw_b para caso de impressao do sistema futuro após pivoteamento.

def resolveSistema():
  ''' Funcao responsavel para resolver o sistema Ax = b por pivoteamento gaussiano
  '''
  global A; #Chamada da variavel global A.
  global b; #Chamada da variavel global b.

  global n; #Chamada da variavel global n.

  x = []; #Cria um vetor x para armazenamento dos valores de cada variavel do sistema.

  #Realiza o algoritimo para resolucao de sistema linear por eliminacao gaussiana com pivoteamento.
  for k in range (n-1):
    pivo = A[k][k];
    l_pivo = k
    for i in range (k+1, n):
      if (abs(A[i][k]) > abs(pivo)):
        pivo = A[i][k]
        l_pivo = i
    if (pivo == 0):
      print("A matriz A é singular!")
    
    else:
      try:
        if (l_pivo != k):
          for j in range (n):
            troca = A[k][j];
            A[k][j] = A[l_pivo][j]
            A[l_pivo][j] = troca
          troca = b[k]
          b[k] = b[l_pivo]
          b[l_pivo] = troca
        for i in range (k+1, n):
          m = A[i][k]/A[k][k];
          A[i][k] = 0
          for j in range (k+1, n):
            A[i][j] = A[i][j] - m*A[k][j]
          b[i] = b[i] - m*b[k]
      except ZeroDivisionError:
        print("Não foi possivel resolver o sistema por esse método!")
        return menu(0);
  try:
    for i in range (n):
      xn = round(b[i]/A[i][i]);
      x.append(xn);
    for k in range (n-2,-1,-1):
      s = 0
      for j in range (k+1, n):
        s = s + A[k][j]*x[j]
      x[k] = round((b[k] - s)/A[k][k])

    #Printa o vetor X de solucao.
    print("Vetor x:")
    print("[",end="")
    for i in range (n):
      if (i != n-1):
        print(format(x[i]))
      else:
        print(format(x[i]) + "]")
    print("\n",end="")
  except ZeroDivisionError:
    print("Não foi possivel resolver o sistema por esse método!")
    return menu(0);
    

def imprimeSistema():
  ''' Funcao responsavel por imprimir o sistema Ax = b
  '''
  clear() #Limpa o terminal

  #Printa o sistema Ax = b formatado com precisao de duas casas decimais nos floats
  for i in range (n):
    if (i == 0):
      print("[", end="")
    else:
      print(" ",end = "")
    for j in range (n):
      formated = "{:.2f}".format(raw_A[i][j])
      print(formated, end="")
      if ((i == n-1) and (j == n-1)):
        print("]", end="")
      if (j != n-1):
        print(" ", end="")
      if (j == n-1):
        print("   ", end="")
        if (i == 0):
          print("[", end="")
        formated = "{:.2f}".format(raw_b[i])
        print(formated, end="")
        if (i == n-1):
          print("]")
        else:
          print("\n", end="")
  print("\n",end="")

def menu(escolha):

  ''' Funcao responsavel por mostrar o menu de opcoes para o usuario

   :param escolha: Escolha do usuario do menu.
  '''
  #Caso a escolha seja 0, mostra todas as opcoes do menu e pede para o usuario escolher uma.
  if (escolha == 0):
    opcoes = int(input("1 - Inserir matiz A e vetor b\n2 - Imprimir sistema Ax = b\n3 - Resolver sistema Ax = b\n4 - Sair\n"))
    menu(opcoes)

  #Caso a escolha seja 1, le a matriz A e o vetor b.
  elif (escolha == 1):
    clear() #Limpa o terminal
    lerMatriz()
    lerVetor()
    menu(0)
  #Caso a escolha seja 2, imprime o sistema Ax = b.
  elif (escolha == 2):
    clear()
    imprimeSistema()
    menu(0)
  #Caso a escolha seja 3, resolve o sistema Ax = b e apresenta o vetor x solucao.
  elif (escolha == 3):
    clear()
    resolveSistema()
    print("Sistema resolvido com sucesso!\n")
    menu(0)
  #Caso a escolha seja 4, finaliza o programa.
  elif (escolha == 4):
    clear()
    print("Programa finalizado!")
  #Caso a escolha outro numero qualquer, limpa o terminal e imprime o menu novamente.
  else:
    clear()
    menu(0)

#Inicia o menu.
menu(0)