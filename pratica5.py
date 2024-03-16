import random

def explorar_ilha():
 print("Bem-vindo(a) ao Jogo de Aventura na Ilha Misteriosa\n")

 print("Instruções:\nVocê é um corajoso explorador em busca de tesouros em uma ilha misteriosa. Ao longo de sua jornada, enfrentará desafios e tomará decisões que moldarão o resultado da aventura. Siga as instruções apresentadas para explorar a ilha e descobrir seus segredos.\n")

 print("Cenário Inicial:\nVocê acorda em uma praia deserta, rodeado por palmeiras e sons de pássaros desconhecidos. À sua frente, uma densa floresta, na direita caminhos desconhecidos e a sua esquerda, uma montanha misteriosa. Escolha sabiamente para determinar o destino de sua jornada.\n")

 while True:
   print("Qual é sua escolha:\n A) Floresta densa: \n B) Caminhos desconhecidos: \n C) Montanha misteriosa:")
   escolha = str(input("Resposta: ").upper())

   if escolha == "A":
    floresta_densa()
   elif escolha == "B":
    Caminhos_desconhecidos()
   elif escolha == "C":
    montanha_desconhecida()
   else:
    print("Escolha invalida, escolha novamente.")

def floresta_densa():
  print("Ok! Você escolheu a floresta densa, onde varios exploradores ja foram de arrasta pra cima, mas,você pode ter a chace de por ela chegar ao tesouro secreto.\n")
  print("Depois de ter andado por varias horas, se deprando com varios anamais venenosos, insetos, você encontrou uma caverna, entrou la e exolorou, chagando no final dela, ao lado de uma rocha tinha, uma chave e dois baùs, qual você decide abrir?  ")
  print("A) Baú da direita\n B) Baú da esquerda\n C) Decide voltar e explorar outro lugar da ilha.")
  escolha_do_bau = input("Resposta: ")
  escolha_do_bau = escolha_do_bau.upper()
  if escolha_do_bau == "A":
    if random.random() < 0.8:
      print("Abriu e BOOOOOMM, era uma armadilha dos povos nativos, foi capiturado.")
    else:
      print("Você encontrou os numeros do Euro-milhões, está rico.")
      return 
  elif escolha_do_bau == "B":
    print("Você abriu e não encontrou nada.")
  else:
    print("Resposta invalida! Tente novamente.")
    
def Caminhos_desconhecidos():
  print("Sua escolha foi os caminhos desconhecidos, onde somente o pirata Bugg conseguiu passar por ele e achar o tesouro, continue aqui e vamos ver se você vai ser capaz.")
  print("Você faz uma boa escolha, os caminhos densconhecidos, são tranquilos de andarem, porem é a trilha de tribos da ilha. Depois de um tempo explorando, tu chegou em uma ponte e então, oque vai ser decidido?\n A) Atravesar a ponte.\n B) Voltar e exolorar outra lugar da ilha.")
  escolha2 = input("Resposta: ")
  escolha2 = escolha2.upper()
  if random.random() < 1.0:
    if escolha2 == "A":
      print("Você passou a ponte, chegou no esqueleto do capitão Bugg e achou o numero do Euro-milhões.")
    else:
      print("AAAA NÃO!!!! Um nativo te viu e jogou rio abaixo.")
      return 
  elif escolha2 == "B":
    print("Voltandoo!.")
  else:
    print("Resposta invalida! Tente novamente.")
    
def montanha_desconhecida():
  print("Ok! Indo em direção a montanha tem varias placas avisando 'Perigo', 'Não se aproxime', mas como queremos achar o tesouro, devemos escolher.\n A) Continuar \n B) Voltar, para ir por outro caminho")
  escolha = input("Resposta:")
  escolha = escolha.upper()
  if random.random() < 0.6:
    if escolha == "A":
      print("Você continuou, enfrentou o monstro que vive na montanha e pegou o tesouro.")
    else:
      print("MEU DEUS!! Você foi morto pelo monstro. ")
      return
  elif escolha == "B":
    print("Voltandooo!!")
  else:
    print("Resposta invalida! Tente novamente.")
    
print("Continue a aventura.")
explorar_ilha()



  


    
    
  