# Função para criar a tabela de diferenças
def babbage(eixo_y):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(n - 1):
        linha = []
        for j in range(n - i - 1):
            v = tabela[i][j] - tabela[i][j + 1]
            linha.append(v)
        tabela.append(linha)
    return tabela

# Função para encontrar a diferença correta
def resultado(dif, i):
    if dif[i][-1] == dif[-1][-1]:  # Para comparar o último elemento da última diferença
        return dif[i][-1]
    else:
        return dif[i][-1] - resultado(dif, i + 1)  # Subtração das diferenças anteriores

# Função que representa um polinômio de grau n
def polinomio(x, coeficientes, grau):
    soma = 0
    i = 0
    while i <= grau:
        soma += coeficientes[i] * (x ** (grau - i))
        i += 1
    return soma

# Entrada de dados pelo usuário
grau = int(input("Digite o grau do polinômio: "))
coeficientes = []

print("Digite os coeficientes do polinômio:")
for i in range(grau + 1):
    coef = float(input(f"Coeficiente de x^{grau - i}: "))
    coeficientes.append(coef)

x_input = int(input("Digite o valor de x para calcular: "))

# Criando os eixos X e Y
eixo_x = list(range(x_input))
eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]

# Gerando a tabela de diferenças
diffs = babbage(eixo_y)

# Exibindo os valores de X e Y
print("Eixo X:", eixo_x)
print("Eixo Y:", eixo_y)

# Exibindo a tabela de diferenças
print("Tabela de diferenças:")
for c, linha in enumerate(diffs):
    print(f"nível {c}: {linha}")

# Mostrando o resultado para x_input
res = resultado(diffs, 0)
print(f"O valor para x={x_input} -> {res}")
