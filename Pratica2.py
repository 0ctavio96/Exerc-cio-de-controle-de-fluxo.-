def calculo(nota1,nota2,nota3):
  media = (nota1+nota2+nota3)/3
  return media

nome = input("Qual é seu nome:")
print("Olá {}. Seja bem vindo(a) a calculadora de média.".format(nome))

nota1 = float(input("informe sua primeira nota: "))
nota2 = float(input("informe sua segunda nota: "))
nota3 = float(input("informe sua terceira nota: "))

resultado_media = calculo(nota1,nota2,nota3)
print(f"Sua media é: {resultado_media}")


# no inicio estava tentando declarar uma variavel que somasse as notas.
# exemplo da tentativa:
# total = float(nota1+nota2+nota3)
    # def calculo():
       # total /3
# print(calculo)
# Mas revisei o material de estudo e consegui.



 






 


