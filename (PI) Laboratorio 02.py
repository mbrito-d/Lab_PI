#Laboratorio 02
#Maria Eduarda Brito

import math

#(01) Alice vai à lanchonete e decide comprar k cafés e n salgados, cujos preços unitários são p e q reais, respectivamente. Nesta semana, há uma promoção: a compra de um café com um salgado está com 20% de desconto frente ao preço usual. Escreva uma função que calcule o valor a ser pago por Alice.
def alice_na_lanchonete(k_caf: int, n_salg: int, p_caf: float, q_salg: float) -> float:
   if k_caf <= n_salg:
      valor_menor = k_caf
      valor_maior = (n_salg - k_caf)*q_salg
   else:
      valor_menor = n_salg
      valor_maior = (k_caf - n_salg)*p_caf
   valor_sem_desconto = ((valor_menor*p_caf) + (valor_menor*q_salg))*0.8
   return valor_sem_desconto + valor_maior



"""
 (02) Beverly precisa pintar o exterior de um tanque cilíndrico de raio *r* e altura *h* , parte de sua nova escultura. Sabe-se que cada lata de tinta com *l* litros custa *c* reais e possibilita a pintura de *p* metros quadrados por litro. Escreva uma função que calcule o número de latas a ser comprado e o valor a ser pago. 
    Nota: use `math.pi` e `math.ceil()`.
 """
def Beverlys_tank(r: float, h: float, litros: float, preco: float, metros: float) -> tuple:
   bases = input("Deseja pintar as bases do tanque? (s/n): ").strip().lower()
   if bases == 's':
      area = 2*math.pi*r*(h+r)
   else:
      area = 2*math.pi*r*h
   latas = math.ceil(area/(metros*litros))
   return latas, latas*preco


'''
(03) Polinomio de 3º grau
def polinomio(a: float, b: float, c: float, d: float, t0: float, t1: float) -> float:
   #derivada do polinomio: P'(t) = 3at^2 + 2bt + c
   t = 
   return (a*(t1**3) + b*(t1**2) + c*t1 + d) - (a*(t0**3) + b*(t0**2) + c*t0 + d)
'''

# (04) Uma quantidade *n* de doces está disponível para ser distribuída entre *m* crianças. Escreva uma função que retorne a quantidade de doces que cada criança pode receber, de modo que a divisão seja justa e todos recebam a mesma quantidade de doces. Caso não seja possível dividir igualmente, a função deve retornar -1.
def doces_criancas(n: int, m: int) -> int:
   if n < m: 
      return 0
   a = b = c = 1
   for i in range(1, n): 
      a *= i
   for j in range(1, m):
      b *= j
   for k in range(1, n-m+1):
      c *= k
   return (a//(b*c))

#(05)
def distancia_euclidiana(x1: float, y1: float, z1: float, x2: float, y2: float, z3: float) -> float:
   return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z3 - z1)**2)


#(06)
def palindromos(n: int) -> bool:
   if n < 10:
      return True
   elif n % 11 == 0:
      return True
   elif n % 101 == 0:
      return True
   elif n % 111 == 0:
      return True
   else:
      return False

def menu():
   print("\nBem vindo!\nMenu de Exercicios do Laboratorio 02:")
   print("1 - Alice na lanchonete")
   print("2 - Pintando o tanque da Beverly")
   print("3 - Polinomio de 3º grau")
   print("4 - Doces para crianças") 
   print("5 - Distancia euclidiana")
   print("6 - Palindromos")
   print("0 - Sair")

def obter_opcao():
   while True:
      escolha = input("Digite o número da opção desejada: ")
      if escolha in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "0"):
         return escolha
      else:
         print("Opção inválida. Tente novamente.")

def main():
   while True:
      menu()
      opcao = obter_opcao()
      contador = 's'
      if opcao == "1":
         while contador == 's':
            k = int(input("Digite a quantidade de cafes: "))
            n = int(input("Digite a quantidade de salgados: "))
            p = float(input("Digite o preco do cafe: "))
            q = float(input("Digite o preco do salgado: "))
            print("O valor a ser pago por Alice e: ", alice_na_lanchonete(k, n, p, q))
            contador = input("Deseja calcular outro lanche? (s/n): ").strip().lower()
      elif opcao == "2":
         while contador == 's':
            r = float(input("Digite o raio do tanque: "))
            h = float(input("Digite a altura do tanque: "))
            l = float(input("Digite a quantidade de litros por lata: "))
            c = float(input("Digite o preco da lata de tinta: "))
            p = float(input("Digite a quantidade de metros quadrados por litro: "))
            latas, valor = Beverlys_tank(r, h, l, c, p)
            print(f'Serão necessarias {latas} latas e valor total será {valor}')
            contador = input("Deseja calcular outro tanque? (s/n): ").strip().lower()
      elif opcao == "3":
         while contador == 's':
            a = float(input("Digite o coeficiente a: "))
            b = float(input("Digite o coeficiente b: "))
            c = float(input("Digite o coeficiente c: "))
            d = float(input("Digite o coeficiente d: "))
            t0 = float(input("Digite o valor de t0: "))
            t1 = float(input("Digite o valor de t1: "))
            print("O valor do polinomio é: ", polinomio(a, b, c, d, t0, t1))
            contador = input("Deseja calcular outro polinomio? (s/n): ").strip().lower()
      elif opcao == "4":
         while contador == 's':
            n = int(input("Quantos doces existem disponiveis: "))
            m = int(input("Quantas crianças no total: "))
            is_non_negative = m>=0 and n>=0
            if is_non_negative:
               print("A quantidade de doces que cada criança pode receber é: ", doces_criancas(n, m))
            else:
               print("Quantidade de doces ou crianças inválida.")
            contador = input("Deseja calcular outro exercicio? (s/n): ").strip().lower()
      elif opcao == "5":
         while contador == 's':
            x1, y1, z1 = map(float, input("Digite as coordenadas do ponto A: ").split())
            x2, y2, z2 = map(float, input("Digite as coordenadas do ponto B: ").split())
            print("A distancia euclidiana é: ", distancia_euclidiana(x1, y1, z1, x2, y2, z2))
            contador = input("Deseja calcular outra distancia? (s/n): ").strip().lower()
      elif opcao == "6":
         while contador == 's':
            n = int(input("Digite um numero: "))
            if n > 999 or n < 0:
               print("Numero invalido.")
            else:
               print("O numero é palindromo? ", palindromos(n))
            contador = input("Deseja verificar outro numero? (s/n): ").strip().lower()
      elif opcao == "0":
         print("\nObrigado por usar o programa!\nSaindo...")
         break

if __name__ == "__main__":
 main()