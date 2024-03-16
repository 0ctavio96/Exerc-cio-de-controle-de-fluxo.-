inicio = input("Olá, qual é seu nome?")
print(f"Seja bem vindo(a) {inicio}, por qual caminho você vai? ")
escolha =(input('Caminho [A], caminho [B] ou caminho [C]: ').upper())

if escolha == "A":
   print("Caminho ruim, cheio de obstaculos.")   
elif escolha == "B":
   print("O melhor caminho, curto e rápido")
elif escolha == "C":
   print("Caminho intermédio, porem com vistas incriveis.") 
else:
   print("Que pena, posso te flar apénas sobre os caminhos.")
   
   

# import random

# def adivinhe ():
#    print("Vamos começar, adivinhe o numero atravez de palpites.") 
#    numero_aleatorio = random.randrange(0,100)
#    numero_tentativas = 10
#    while numero_tentativas < 0:
#         palpite = int(input("tentativa 1: "))
#         if palpite == numero_aleatorio:
#          print("Parabéns, você acertou.")
#          break
#         else:
#            if palpite > numero_aleatorio:
#               print("seu numero é menor. ")
#            else:
#               print("Seus numero é maior.")

