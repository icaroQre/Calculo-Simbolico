def soma(a, b):
    """
    Função recursiva para soma de dois números inteiros: [70]
    """
    if b == 0:
        return a
    return soma(a + 1, b - 1)


def subtracao(a, b):
    """
    Função recursiva para subtração de dois números inteiros: [70]
    """
    if b == 0:
        return a
    return subtracao(a - 1, b - 1)


def multiplicacao(a, b):
    """
    Função recursiva para multiplicação usando apenas soma: [70]
    """
    if b == 0:
        return 0
    return soma(a, multiplicacao(a, b - 1))


def divisao_inteira(a, b):
    """
    Função recursiva para divisão inteira usando apenas subtração: [70]
    """
    if a < b:
        return 0
    return soma(1, divisao_inteira(subtracao(a, b), b))


def resto_divisao(a, b):
    """
    Função recursiva para calcular o resto da divisão usando apenas subtração: [70]
    """
    if a < b:
        return a
    return resto_divisao(subtracao(a, b), b)


def exponenciacao(base, exp):
    """
    Função recursiva para exponenciação (base^exp), considerando exp >= 0: [80]
    """
    if exp == 0:
        return 1
    return multiplicacao(base, exponenciacao(base, subtracao(exp, 1)))


def fatorial(n):
    """
    Função recursiva para cálculo do fatorial de um número inteiro positivo: [90]
    """
    if n == 0 or n == 1:
        return 1
    return multiplicacao(n, fatorial(subtracao(n, 1)))


def fibonacci(n, memo={}):
    """
    Função recursiva para calcular o n-ésimo número da sequência de Fibonacci,
    utilizando memoização para melhorar a eficiência: [100]
    """
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = soma(fibonacci(subtracao(n, 1), memo), fibonacci(subtracao(n, 2), memo))
    return memo[n]


# Testando todas as fnuções
if __name__ == "__main__":
    print("Soma(5, 3):", soma(5, 3))
    print("Subtração(5, 3):", subtracao(5, 3))
    print("Multiplicação(5, 3):", multiplicacao(5, 3))
    print("Divisão inteira(7, 2):", divisao_inteira(7, 2))
    print("Resto da divisão(7, 2):", resto_divisao(7, 2))
    print("Exponenciação(2, 3):", exponenciacao(2, 3))
    print("Fatorial(5):", fatorial(5))
    print("Fibonacci(10):", fibonacci(10))
