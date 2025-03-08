#Laboratorio 01
#Maria Eduarda Brito

import math
import random

#(01) Dada uma temperatura em Celsius, determine sua equivalente em Fahrenheit.
def celsius_para_fahrenheit(temperatura):
 return temperatura * (9.0/5.0) + 32.0



#(02) Dada uma temperatura em Fahrenheit, determine sua equivalente em Celsius.
def fahrenheit_para_celsius(temperatura):
  return (temperatura - 32) * (5.0/9.0)



"""
(03) Dadas uma temperatura em Fahrenheit e uma velocidade de vento em milhas por hora, o National Weather Service (serviço atmosférico americano) define a temperatura efetiva (sensação térmica) em Fahrenheit por: 
   wc = 35.74 + 0.6215 * t + (0.4575 * t - 35.75) * v ** 0.16
   Escreva uma função que recebe dois floats — uma temperatura em Celsius e uma velocidade em kilômetros por hora — e devolve a temperatura efetiva em Celsius. 
"""
def sensacao_termica_fahrenheit(temp_Celcius, velo_Km):
  temp_Fahrenheit = celsius_para_fahrenheit(temp_Celcius)
  velo_Mph = velo_Km / 1.60934
  return 35.74 + 0.6215 * temp_Fahrenheit + (0.4575 * temp_Fahrenheit - 35.75) * velo_Mph ** 0.16



"""
(04) Escreva funções que:
  recebe floats b e h e devolve a área de um triângulo de base b e altura h;
  recebe um float r e devolve a área de um círculo de raio r; use import math e math.pi.
"""
def area_triangulo(b, h):
  return b * h / 2

def area_circulo(r):
  return math.pi * r ** 2



#(05) Escreva uma função que recebe uma quantia inicial p , uma taxa de juros anual r e um período (em anos) t e devolve o montante que você teria se investisse p reais a uma taxa r continuamente por t anos. A resposta é dada por: pe(rt)
def previsao_investimento(p:float, r: float, t: int)-> float:
  return p * math.exp(r * t)



#(06) Escreva uma função que recebe três valores, x, y e z, e devolve os valores mínimo e máximo de {x,y,z}.
def min_max(x, y, z):
 if x < y and x < z:
  minimo = x
 elif y < x and y < z:
  minimo = y
 else:
  minimo = z
 if x > y and x > z:
  maximo = x
 elif y > x and y > z:
  maximo = y
 else:
  maximo = z
 return minimo, maximo



#(07) Dados floats a, b e c, calcule as raízes reais (caso existam) do polinômio quadrático P(x)= ax^2 + bx + c. Utilize a fórmula de Bháskara
def raizes(a: float, b: float, c: float)-> tuple:
 delta = b ** 2 - 4 * a * c
 if delta > 0:
  x1 = (-b + math.sqrt(delta)) / (2 * a)
  x2 = (-b - math.sqrt(delta)) / (2 * a)
  return x1, x2
 elif delta < 0:
  x = "Não possui raízes reais"
  return x
 else:
  x = -b / (2 * a)
  return x
 


#(08) Escreva uma função que recebe cinco valores em {0,1} e devolve verdadeiro (True) se o número de uns é maior que o de zeros, ou falso (False) em caso contrário.
def quantos_uns_maior_que_zeros(a: int, b: int, c: int, d: int, e: int)-> bool:
 if a + b + c + d + e > 2:
  return True
 else:
  return False



#(09)Escreva uma função que recebe cinco valores em True,False e devolve verdadeiro (True) se a quantidade de verdadeiros recebidos é ímpar, ou falso (False) em caso contrário.
def sao_impares(a: bool, b: bool, c: bool, d: bool, e: bool)-> bool:
 if a + b + c + d + e % 2 != 0:
  return True
 else:
  return False


"""
(10)Mini Quadra é uma simplificação da Mega Sena, na qual o apostador deve escolher quatro números inteiros distintos entre 1 e 20, inclusive.
    Escreva um programa que gere todos os jogos possíveis (i.é, todas as quádruplas). Você deve imprimir um jogo por linha.
    Modifique seu programa para que receba um inteiro não negativo n e gere todos os jogos com valores entre 1 e n , inclusive (em vez de 1 e 20).
"""
def Mini_Quadra(n):
 combinations = []
 for i in range(1, n-2):
  for j in range(i + 1, n-1):
   for k in range(j + 1, n):
    for l in range(k + 1, n+1):
     combinations.append((i, j, k, l))
 return combinations

def sortear_mini_quadra(n):
 sorteado = random.sample(range(1, n + 1), 4)
 sorteado.sort()  # Ordena os números para manter a consistência
 return tuple(sorteado)

def verificar_resultado(combinacao_usuario, combinacao_sorteada):
 return combinacao_usuario == combinacao_sorteada


"""
(11) Escreva funções que:
   recebe um inteiro n >= 0 e devolve n!, o fatorial de n, definido por 0! = 1 e n! = n * (n-1) para n > 0;
   recebe inteiros e devolve n, m >= 0 e devolve o coeficiente binomial de n e m, dado por n! / (m! * (n-m)!).
 Observe que o coeficiente binomial de n e m é o número de subconjuntos com m elementos que podem ser tomados de um conjunto com n elementos. Por exemplo, coeficente binomial de 20 e 4 é o número de jogos que seu programa (10) deve ter impresso na saída.
"""
def fatorial(n):
 if n == 0:
  return 1
 else:
  for i in range (1, n+1):
   n *= i
 return n
   



#Menu
def exibir_menu():
 print("Menu de Exercicios do Laborátorio 01:")
 print("1. Celsius para Fahrenheit")
 print("2. Fahrenheit para Celsius")
 print("3. Sensação Térmica em Fahrenheit")
 print("4. Área de uma forma geométrica")
 print("5. Previsão de Investimento")
 print("6. Mínimo e Máximo")
 print("7. Raízes de um Polinômio")
 print("8. Quantos 1 são maiores que 0")
 print("9. Se são ímpares")
 print("10. Mini Quadra")
 print("11. Fatorial e Coeficiente Binomial")
 print("0. Sair")

def obter_escolha():
 while True:
  escolha = input("Digite o número da opção desejada: ")
  if escolha in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "0"):
   return escolha
  else:
   print("Opção inválida. Tente novamente.")

def main():
 while True:
  exibir_menu()
  escolha = obter_escolha()
  if escolha == "1":
   contador ='s'
   while contador == 's':
    temperatura = float(input("Digite a temperatura em Celsius: "))
    print("A temperatura em Fahrenheit é: ", celsius_para_fahrenheit(temperatura))
    contador = input("Deseja ver outra temperatura (s/n): ").strip().lower()
  elif escolha == "2":
   contador ='s'
   while contador == 's':
    temperatura = float(input("Digite a temperatura em Celsius: "))
    print("A temperatura em Celcius é: ", fahrenheit_para_celsius(temperatura))
    contador = input("Deseja ver outra temperatura (s/n): ").strip().lower()
  elif escolha == "3":
   contador ='s'
   while contador == 's':
    temp_Celcius = float(input("Digite a temperatura em Celcius: "))
    velo_Km = float(input("Digite a velocidade do vento em Kmph: "))
    print("A sensação térmica em Fahrenheit é: ", sensacao_termica_fahrenheit(temp_Celcius, velo_Km))
    contador = input("Deseja ver outra temperatura (s/n): ").strip().lower()
  elif escolha == "4":
   contador ='s'
   while contador == 's':
    print("Escolha a forma geométrica:")
    print("1. Círculo") 
    print("2. Triângulo")
    forma = input("Digite o número da opção desejada: ")
    if forma == "1":
     r = float(input("Digite o raio do círculo: "))
     print("A área do círculo é: ", area_circulo(r))
    elif forma == "2":
     b = float(input("Digite a base do triângulo: "))
     h = float(input("Digite a altura do triângulo: "))
     print("A área do triângulo é: ", area_triangulo(b, h))
    contador = input("Deseja ver outra área (s/n): ").strip().lower()
  elif escolha == "5":
   contador ='s'
   while contador == 's':
    p = float(input("Digite a quantia inicial: "))
    r = float(input("Digite a taxa de juros anual: "))
    t = int(input("Digite o período em anos: "))
    print("O montante que você teria se investisse é: ", previsao_investimento(p, r, t))
    contador = input("Deseja ver outra previsão (s/n): ").strip().lower()
  elif escolha == "6":
   contador ='s'
   while contador == 's':
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    z = float(input("Digite o terceiro valor: "))
    print("O valor os valores mínimo e máximo são, respectivamente: ", min_max(x, y, z)) 
    contador = input("Deseja ver outro valor (s/n): ").strip().lower()
  elif escolha == "7":
   contador ='s'
   while contador == 's':
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    print("As raízes do polinômio são: ", raizes(a, b, c))
    contador = input("Deseja ver outra raiz (s/n): ").strip().lower()
  elif escolha == "8":
   contador ='s'
   while contador == 's':
    a, b, c, d, e = map(int, input("Digite os 5 numeros (0 ou 1): ").split())
    print("O número de uns é maior que o de zeros: ", quantos_uns_maior_que_zeros(a, b, c, d, e))
    contador = input("Deseja ver outro valor (s/n): ").strip().lower()
  elif escolha == "9":
   contador ='s'
   while contador == 's':
    a, b, c, d, e = map(bool, input("Digite os 5 valores (True ou False): ").split())
    print("A quantidade de verdadeiros é ímpar: ", sao_impares(a, b, c, d, e))
    contador = input("Deseja ver outro valor (s/n): ").strip().lower()
  elif escolha == "10":
   contador ='s'
   while contador == 's': 
    n = int(input("Digite o valor de n: "))
    combinations = Mini_Quadra(n)
    ver_combinações = input("Deseja ver todas as combinações (s/n): ").strip().lower()
    if ver_combinações == "s":
     for comb in combinations:
      print(comb)
    decisao = input("Deseja jogar na Mini Quadra? (s/n): ").strip().lower()
    if decisao == "s":
     combinacao_sorteada = sortear_mini_quadra(n)
     combinacao_usuario = tuple(map(int, input("Digite 4 números distintos entre 1 e n: ").split()))
    if verificar_resultado(combinacao_usuario, combinacao_sorteada):
        print("Parabéns! Você acertou a combinação!")
    else:
        print("Que pena! Você errou a combinação. Tente novamente!")
        print(f"A combinação sorteada foi: {combinacao_sorteada}")
    contador = input("Deseja ver outro jogo (s/n): ").strip().lower()
  elif escolha == "11":
   contador ='s'
   while contador == 's':
    n = int(input("Digite o valor de n: "))
    m = int(input("Digite o valor de m: "))
    print(f"O fatorial de {n} é {fatorial(n):.2e} e o coeficiente binomial é {fatorial(n) / (fatorial(m) * fatorial(n - m)):.2f}")
    contador = input("Deseja ver outro valor (s/n): ").strip().lower
  elif escolha == "0":
   print("\nObrigado por usar o programa!\nSaindo...")
   break

if __name__ == "__main__":
 main()