import random

numero_aleatorio = random.randrange(1,100)
print(numero_aleatorio)

print("Desafio:\n Adivinhe o numero que foi gerado aleatoriamente.")

tentativa1 = int(input('tentativa 1: '))
if tentativa1 == numero_aleatorio:
   print("Parabéns você acertou, precisando de 1 tentativas.")
elif tentativa1 > numero_aleatorio:
   print("Menos.")
elif tentativa1 < numero_aleatorio:
   print("Mais.")    
else:
   tentativa1 != numero_aleatorio
   print("Proxima tentativa.")

tentativa2 = int(input('tentativa 2: '))
if tentativa2 == numero_aleatorio:
   print("Parabéns você acertou, precisando de 2 tentativas.")
elif tentativa2 > numero_aleatorio:
   print("Menos.")
elif tentativa2 < numero_aleatorio:
   print("Mais.")
else:
   tentativa2 != numero_aleatorio
   print("Proxima tentativa.")

tentativa3= int(input('tentativa 3: '))
if tentativa3 == numero_aleatorio:
   print("Parabéns você acertou, precisando de 3 tentativas. ")
elif tentativa3 > numero_aleatorio:
   print("Menos.")
elif tentativa3 < numero_aleatorio:
   print("Mais.")
else:
   tentativa3 != numero_aleatorio
   print("Proxima tentativa.")
   
tentativa4= int(input('tentativa 4: '))
if tentativa4 == numero_aleatorio:
 print("Parabéns você acertou, precisando de 4 tentativas. ")
elif tentativa4 > numero_aleatorio:
  print("Menos.")
elif tentativa4 < numero_aleatorio:
  print("Mais.")
else:
   tentativa3 != numero_aleatorio
   print("Proxima tentativa.") 


tentativa5= int(input('tentativa 5: '))
if tentativa5 == numero_aleatorio:
   print("Parabéns você acertou, precisando de 5 tentativas. ")
elif tentativa5 > numero_aleatorio:
   print("Menos.")
elif tentativa5 < numero_aleatorio:
   print("Mais.")
else:
   tentativa5 != numero_aleatorio
   print("Proxima tentativa.")

tentativa6= int(input('Ultima tentativa: '))
if tentativa6 == numero_aleatorio:
   print("Parabéns você acertou, precisando de 6 tentativas. ")
elif tentativa6 > numero_aleatorio:
   print("Game over.")
elif tentativa6 < numero_aleatorio:
   print("Game over.")
else:
   print("Game over.")

# print("Depois de ter caminhado por horas, você se depara com uma cabana abandonada, e logo acima tem destroços de um avião.\n Agora você deve escolher oque fazer.")
#   print("A) Avião.\n B) Cabana.")

#   escolha_de_A = str(input("Resposta: ").upper())
#   if escolha_de_A == "A":
#    print("Você subio no aviaõ e acabou escorregando, caindo e morrendo, que pena!!!\n GAME OVER.")


