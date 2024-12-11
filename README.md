# Previsão de Vendas com Regressão Linear

## Descrição do Projeto

Este projeto visa prever o **valor das vendas** com base nos **investimentos em marketing** em diferentes plataformas, utilizando um modelo de regressão linear. O conjunto de dados contém informações sobre investimentos em anúncios no YouTube, Facebook e jornais, além das vendas resultantes desses investimentos. O objetivo é identificar como cada canal de marketing impacta as vendas e prever futuros valores de vendas com base em diferentes níveis de investimento.

## Visão Geral do Projeto

Para construir o modelo preditivo, seguimos as seguintes etapas:

1. **Preparação e Exploração dos Dados**: Carregamos e exploramos o dataset para entender as relações iniciais entre as variáveis.
2. **Divisão dos Dados**: Utilizando a biblioteca Scikit-learn, dividimos o conjunto de dados em conjuntos de treino e teste.
3. **Construção do Modelo de Regressão Linear**: Treinamos o modelo de regressão linear com os dados de treino, utilizando os investimentos em marketing como variáveis independentes (YouTube, Facebook, e jornal) e as vendas como variável dependente.
4. **Avaliação do Modelo**: Avaliamos o desempenho do modelo utilizando o **coeficiente de determinação (R²)** para medir a precisão das previsões.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Pandas**: Manipulação e análise de dados.
- **NumPy**: Computação numérica.
- **Scikit-learn**: Implementação e avaliação do modelo de regressão linear.

## Estrutura do Dataset

O dataset `MKT.csv` contém as seguintes colunas:

- **youtube**: Investimento em anúncios no YouTube (em milhares de dólares).
- **facebook**: Investimento em anúncios no Facebook (em milhares de dólares).
- **newspaper**: Investimento em anúncios em jornais (em milhares de dólares).
- **sales**: Vendas correspondentes aos investimentos (em milhares de unidades).

Essas variáveis representam o investimento em cada plataforma e o retorno em vendas, sendo utilizadas para treinar o modelo de regressão e prever vendas futuras.

## Resultados

Os resultados do projeto incluem:

- **Modelo de Regressão Linear Treinado**: Um modelo preditivo capaz de estimar o valor das vendas com base nos investimentos em diferentes canais de marketing.
- **Coeficiente de Determinação (R²)**: A precisão do modelo é medida pelo R², que indica a proporção de variação nas vendas explicada pelos investimentos em marketing.
- **Insights sobre Impacto de Cada Canal**: O modelo também revela o impacto relativo de cada canal de marketing (YouTube, Facebook e jornais) nas vendas, auxiliando na tomada de decisões estratégicas para otimização de investimentos.

## Contato
Se você tiver dúvidas ou sugestões, entre em contato por [vitttormuniz@gmail.com](mailto:vitttormuniz@gmail.com).
