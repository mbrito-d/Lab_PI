# Lista L2
# Maria Eduarda Brito

# 01. Dados floats |x| < 1 e 0 < ε  1, calcule uma aproximação com precisão ε para a função ln(1 + x), via série de Taylor-Maclaurin:
def Serie_Taylor_Maclaurin(x: float, epsilon: float) -> float:
    termo = x
    soma = 0
    k = 1
    while abs(termo) >= epsilon:
        soma += termo
        k += 1
        termo = ((-1)**(k+1))*(x**k)/k
    return soma
        
# 02
def eh_heap(H):
    """
    Verifica se uma lista é um heap.

    Args:
        H: A lista de inteiros.

    Returns:
        True se H é um heap, False caso contrário.
    """
    n = len(H)
    for j in range(1, n):
        if H[j // 2 - 1] < H[j]:
            return False
    return True

# Exemplos de uso:
H1 = [5, 2, 5, 1, 1, 4, 0, 1]
H2 = [5, 4, 3, 2, 1, 0]
H3 = [5, 2, 3, 3, 1]
H4 = [1, 4, 5, 2, 3, 8]

print(f"H1 é heap: {eh_heap(H1)}")
print(f"H2 é heap: {eh_heap(H2)}")
print(f"H3 é heap: {eh_heap(H3)}")
print(f"H4 é heap: {eh_heap(H4)}")


def maior_soma_distante(L, d):
    """
    Encontra a maior soma de dois elementos distantes em uma lista.

    Args:
        L: A lista de inteiros.
        d: A distância mínima entre os índices dos elementos.

    Returns:
        A maior soma encontrada.
    """
    n = len(L)
    maior_soma = float('-inf')
    
    for i in range(n - d):
        for j in range(i + d, n):
            soma = L[i] + L[j]
            if soma > maior_soma:
                maior_soma = soma
                
    return maior_soma

# Exemplo de uso:
L = [1, 5, 2, 8, 3, 9]
d = 2
resultado = maior_soma_distante(L, d)
print(f"Maior soma distante: {resultado}")

def segmento_maximo_zeros(A):
    """
    Encontra o segmento máximo de zeros em uma lista.

    Args:
        A: A lista de inteiros.

    Returns:
        Uma tupla (m, i, j) onde m é o comprimento do segmento máximo,
        i é o índice inicial e j é o índice final do segmento.
    """
    n = len(A)
    max_comprimento = 0
    inicio = -1
    fim = -1
    
    comprimento_atual = 0
    inicio_atual = -1
    
    for k in range(n):
        if A[k] == 0:
            if comprimento_atual == 0:
                inicio_atual = k
            comprimento_atual += 1
        else:
            if comprimento_atual > max_comprimento:
                max_comprimento = comprimento_atual
                inicio = inicio_atual
                fim = k
            comprimento_atual = 0
            
    if comprimento_atual > max_comprimento:
        max_comprimento = comprimento_atual
        inicio = inicio_atual
        fim = n
        
    return (max_comprimento, inicio, fim)

# Exemplo de uso:
A = [1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0]
m, i, j = segmento_maximo_zeros(A)
print(f"Segmento máximo de zeros: Comprimento = {m}, Início = {i}, Fim = {j}")


def josephus(n, m):
    """
    Resolve o problema de Josephus.

    Args:
        n: O número de pessoas.
        m: O passo de eliminação.

    Returns:
        O número do sobrevivente.
    """
    pessoas = list(range(1, n + 1))
    indice = 0
    
    while len(pessoas) > 1:
        indice = (indice + m - 1) % len(pessoas)
        pessoas.pop(indice)
        
    return pessoas[0]

# Exemplo de uso:
n = 5
m = 3
sobrevivente = josephus(n, m)
print(f"Sobrevivente: {sobrevivente}")


def contar_distintos(A):
    """
    Conta o número de números distintos em uma lista.

    Args:
        A: A lista de números inteiros.

    Returns:
        O número de números distintos.
    """
    distintos = set()
    for num in A:
        distintos.add(num)
    return len(distintos)

# Exemplo de uso:
A = [1, 2, 2, 3, 4, 4, 5]
num_distintos = contar_distintos(A)
print(f"Número de distintos: {num_distintos}")



def eh_sublista(A, L):
    """
    Verifica se uma lista A é sublista de L.

    Args:
        A: A sublista potencial.
        L: A lista maior.

    Returns:
        True se A é sublista de L, False caso contrário.
    """
    m = len(A)
    n = len(L)
    
    i = 0  # Índice para A
    j = 0  # Índice para L
    
    while i < m and j < n:
        if A[i] == L[j]:
            i += 1
        j += 1
        
    return i == m

# Exemplos de uso:
A1 = [12, 13, 10, 3]
L1 = [11, 12, 13, 11, 10, 9, 7, 3, 3]
L2 = [11, 12, 10, 11, 13, 9, 7, 3, 3]

print(f"A1 é sublista de L1: {eh_sublista(A1, L1)}")
print(f"A1 é sublista de L2: {eh_sublista(A1, L2)}")

def menu():
    print("\nBem vindo!\nMenu de Exercicios da Lista L2:")
    print("1. Questão 1")
    print("2. Questão 2")
    print("3. Questão 3")
    print("4. Questão 4")
    print("5. Questão 5")
    print("6. Questão 6")
    print("7. Questão 7")
    print("8. Questão 8")
    print("0. Sair")

def escolha():
 while True:
  escolha = input("Digite o número da opção desejada: ")
  if escolha in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "0"):
   return escolha
  else:
   print("Opção inválida. Tente novamente.")

def main():
 while True:
  menu()
  opcao = escolha()
  contador = 's'
  if opcao == "1":
   while contador == 's':
    x = float(input("Digite o valor de x: "))
    epsilon = float(input("Digite o valor de epsilon: "))
    print(f"A aproximação de ln(1 + {x}) é: ", Serie_Taylor_Maclaurin(x, epsilon))
    contador = input("Deseja continuar? (s/n): ").strip().lower()
  elif opcao == "2":
   print("Questão 2")
  elif opcao == "0":
   print("\nObrigado por usar o programa!\nSaindo...")
   break
  

if __name__ == "__main__":
 main()