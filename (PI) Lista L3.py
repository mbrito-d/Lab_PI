import math

def dia_da_semana(d, m, a):
    """
    Calcula o dia da semana para uma data fornecida.

    Args:
        d: Dia (1 <= d <= 31).
        m: Mês (1 <= m <= 12).
        a: Ano (a >= 1).

    Returns:
        O dia da semana (0: Domingo, 1: Segunda, ..., 6: Sábado).
    """
    if not (1 <= d <= 31 and 1 <= m <= 12 and a >= 1):
        raise ValueError("Data inválida.")

    a0 = a - (14 - m) // 12
    x = a0 + a0 // 4 - a0 // 100 + a0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    return d0

# Exemplo de uso:
d = 21
m = 11
a = 2024
dia = dia_da_semana(d, m, a)
dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
print(f"O dia da semana para {d}/{m}/{a} é: {dias[dia]}")

def busca_pares(A, x):
    """
    Encontra dois índices i e j em A tais que A[i] + A[j] = x.

    Args:
        A: Lista de valores numéricos.
        x: Valor alvo.

    Returns:
        Uma tupla (i, j) com os índices, ou (n, n) se não encontrar.
    """
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] + A[j] == x:
                return (i, j)
    return (n, n)

# Exemplo de uso:
A = [2, 7, 11, 15]
x = 9
i, j = busca_pares(A, x)
print(f"Índices para soma {x}: ({i}, {j})")

def eh_permutacao_circular(s, t):
    """
    Verifica se s é permutação circular de t.

    Args:
        s: Primeira sequência.
        t: Segunda sequência.

    Returns:
        True se s é permutação circular de t, False caso contrário.
    """
    n = len(s)
    if n != len(t):
        return False

    for k in range(1, n + 1):
        if s[k-1:] == t[:n-k+1] and s[:k-1] == t[n-k+1:]:
            return True
    return False

# Exemplo de uso:
s = [2, 3, 5, 4, 1]
t = [4, 1, 2, 3, 5]
print(f"s é permutação circular de t: {eh_permutacao_circular(s, t)}")

s = [3, 5, 1, 4, 2]
t = [4, 1, 2, 3, 5]
print(f"s é permutação circular de t: {eh_permutacao_circular(s, t)}")

def busca_padroes(S, T):
    """
    Conta o número de ocorrências de S como segmento em T.

    Args:
        S: Padrão a ser buscado.
        T: Texto onde buscar.

    Returns:
        O número de ocorrências de S em T.
    """
    m = len(S)
    n = len(T)
    ocorrencias = 0

    if m > n:
        return 0

    for k in range(n - m + 1):
        if T[k:k+m] == S:
            ocorrencias += 1
    return ocorrencias

# Exemplo de uso:
S = [0, 1, 0]
T = [0, 1, 0, 2, 3, 0, 4, 5, 0, 1, 0, 6, 7, 8, 9, 0, 3, 10, 2, 0, 1, 0, 1, 0]
ocorrencias = busca_padroes(S, T)
print(f"Ocorrências de S em T: {ocorrencias}")

def inversoes(A):
    """
    Encontra as inversões em uma lista A.

    Args:
        A: Lista de números distintos.

    Returns:
        Uma lista de tuplas, onde cada tupla representa uma inversão.
    """
    n = len(A)
    inversoes_lista = []
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                inversoes_lista.append((i, j))
    return inversoes_lista

# Exemplo de uso:
A = [2, 3, 8, 6, 1]
lista_inversoes = inversoes(A)
print(f"Inversões em A: {lista_inversoes}")

def identidade_bezout(m, n):
    """
    Calcula o MDC de m e n, e encontra a e b tais que am + bn = d.

    Args:
        m: Primeiro inteiro positivo.
        n: Segundo inteiro positivo.

    Returns:
        Uma tupla (d, a, b) onde d é o MDC de m e n, e am + bn = d.
    """
    if m == 0:
        return n, 0, 1
    
    d, a1, b1 = identidade_bezout(n % m, m)
    a = b1 - (n // m) * a1
    b = a1
    return d, a, b

# Exemplo de uso:
m = 24
n = 18
d, a, b = identidade_bezout(m, n)
print(f"MDC({m}, {n}) = {d}, e {a}*{m} + {b}*{n} = {d}")