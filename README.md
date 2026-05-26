# Simulação de Jogo de Dados

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-green)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)

Projeto desenvolvido durante o bootcamp **Santander Coders**, com o objetivo de simular um jogo de dados e reunir estatísticas para analisar sua justiça, identificar os resultados mais prováveis e formular previsões sobre jogos futuros.

---

## Sobre o projeto

A proposta consiste em modelar computacionalmente o lançamento de dois dados de seis lados, executar um grande número de simulações e aplicar conceitos de estatística descritiva e inferencial sobre os resultados obtidos. O projeto exercita o uso de bibliotecas científicas do Python para manipulação e análise de dados.

---

## Bibliotecas utilizadas

| Biblioteca | Descrição |
|------------|-----------|
| [NumPy](https://numpy.org/) | Biblioteca para computação científica e manipulação eficiente de arrays |
| [Matplotlib](https://matplotlib.org/) | Biblioteca para visualização de dados (utilizada na análise de frequência) |

---

## Desafios propostos

O projeto foi estruturado em quatro etapas:

### 1. Simulação de dados

Implementação de uma função que simula o lançamento de dois dados de seis lados (valores de 1 a 6), retornando a soma dos resultados.

### 2. Múltiplas simulações

Utilização da função anterior para simular um grande número de jogos (1000 lançamentos), armazenando os resultados em um array NumPy.

### 3. Análise de dados

Cálculo e exibição das seguintes estatísticas:

- Média dos resultados obtidos
- Valores máximo e mínimo registrados
- Frequência de ocorrência de cada soma possível (2 a 12)

### 4. Teste de hipótese

Análise da seguinte questão: supondo um jogo justo, em que todos os lançamentos sejam igualmente prováveis, o resultado da simulação coincide com essa suposição? A discussão envolve a comparação entre a distribuição observada e a distribuição teórica esperada, bem como suas implicações para um jogador.

---

## Estrutura do repositório

```
simulacao-jogo-de-dados/
├── README.md
└── simulacao_dados.py     # Código-fonte da simulação e análise
```

---

## Requisitos

### Versão do Python

Recomenda-se a utilização do **Python 3.10 ou superior**.

### Instalação das dependências

```bash
pip install numpy matplotlib
```

---

## Como executar

```bash
# Clone o repositório
git clone https://github.com/mariannarossim/simulacao-jogo-de-dados.git

# Acesse o diretório do projeto
cd simulacao-jogo-de-dados

# Execute o script
python simulacao_dados.py
```

Recomenda-se o uso de um ambiente virtual (`venv`) para isolar as dependências:

```bash
python -m venv venv
# Ativação no Windows
venv\Scripts\activate
# Ativação no Linux/macOS
source venv/bin/activate
```

---

## Considerações sobre o resultado

Em um jogo justo com dois dados de seis lados, as somas possíveis variam de 2 a 12, mas **não são igualmente prováveis**. A soma 7 é a mais provável, pois pode ser obtida por seis combinações distintas (1+6, 2+5, 3+4, 4+3, 5+2, 6+1), enquanto as somas 2 e 12 possuem apenas uma combinação possível cada. A análise da simulação evidencia essa distribuição teórica e demonstra como o comportamento empírico se aproxima da distribuição esperada conforme o número de lançamentos aumenta — um princípio conhecido como **Lei dos Grandes Números**.

---

## Conceitos aplicados

| Área | O que o projeto demonstra |
|------|---------------------------|
| **Python** | Definição de funções, estruturas de controle, manipulação de arrays |
| **NumPy** | Geração de números aleatórios, vetorização, funções estatísticas |
| **Estatística** | Medidas de tendência central, distribuição de frequência, teste de hipótese |
| **Probabilidade** | Espaço amostral, distribuição teórica, Lei dos Grandes Números |

---

## Autora

**Marianna Rossi**

Projeto desenvolvido durante o bootcamp **Santander Coders**.

[GitHub](https://github.com/mariannarossim)

---

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
