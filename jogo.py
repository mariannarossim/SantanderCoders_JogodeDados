import numpy as np

# Função que realiza a simulação de lançamento de dois dados de seis lados
def simulacao_lancamento_dados(n_simulacoes=1000):
    resultados = np.random.randint(1, 7, size=(n_simulacoes, 2))  # Gerar resultados dos lançamentos
    soma_resultados = np.sum(resultados, axis=1)  # Calcular a soma dos resultados de cada lançamento
    return soma_resultados

# Simular os lançamentos e armazenar os resultados
resultados_simulacao = simulacao_lancamento_dados()

# Calcular e imprimir estatísticas dos resultados
media = np.mean(resultados_simulacao)
minimo = np.min(resultados_simulacao)
maximo = np.max(resultados_simulacao)

print("Média dos resultados:", media)
print("Lançamento mínimo:", minimo)
print("Lançamento máximo:", maximo)

# Contagem de ocorrências de cada possível lançamento
ocorrencias = np.bincount(resultados_simulacao)[2:]

for i, ocorrencia in enumerate(ocorrencias, start=2):
    print(f"Número de vezes que {i} ocorreu:", ocorrencia)

# Teste de hipótese
print("\nTeste de hipótese:")

# Calculando a probabilidade teórica para cada lançamento
probabilidade_teoria = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36

# Imprimindo a hipótese nula (H0)
print("Hipótese nula (H0): A proporção de cada resultado é igual à probabilidade teórica.")
print(f"Probabilidade teórica para cada lançamento: {probabilidade_teoria}")

# Calculando a frequência relativa dos resultados da simulação
frequencia_relativa = ocorrencias / np.sum(ocorrencias)

# Imprimindo as probabilidades teóricas e as frequências relativas
for i in range(2, 13):
    print(f"Probabilidade teórica de {i}: {probabilidade_teoria[i-2]:.4f}, Frequência relativa: {frequencia_relativa[i-2]:.4f}")
