
# 🎬 Projeto de Análise de Filmes com ETL, SQL e Dashboard Interativo

## 📖 Introdução

Este projeto tem como objetivo realizar uma **análise completa de dados de filmes** obtidos através da **API do TMDB (The Movie Database)**, passando por todo o processo de **ETL (Extração, Transformação e Carga)** até a criação de um **dashboard interativo** para visualização dos principais insights sobre os filmes mais populares e bem avaliados.

A análise visa compreender padrões de popularidade, desempenho por gênero e tendências de filmes ao longo dos anos, fornecendo informações valiosas que podem ajudar **plataformas de streaming** na tomada de decisão sobre conteúdos mais atrativos para o público.

---

## 💡 Problema de Negócio

Plataformas de streaming enfrentam o desafio de **entender quais gêneros e características de filmes atraem mais o público**.
Saber quais gêneros estão em alta, quais possuem maior avaliação média e como a popularidade varia com o tempo é essencial para direcionar estratégias de catálogo e marketing.

Com base nisso, o projeto busca responder a perguntas como:

* Quais são os **gêneros mais populares** entre os usuários?
* Quais gêneros apresentam **melhores avaliações médias**?
* **Filmes mais recentes** tendem a ser mais populares?
* Quais são os **Top 3 filmes mais populares** do banco de dados?

---

## ⚙️ Etapas do Projeto

### 🔹 1. ETL — Extração, Transformação e Carga

#### 🧩 **Extração**

Os dados foram coletados diretamente da **API do TMDB**, abrangendo diversos **gêneros cinematográficos** (Ação, Comédia, Drama, Terror, etc.).
Para cada gênero, foram extraídos cerca de **100 filmes** utilizando o endpoint `/discover/movie`.

#### 🔧 **Transformação**

Após a coleta, os dados passaram por:

* Limpeza e remoção de valores nulos;
* Ajuste do formato das datas (`release_date`);
* Arredondamento das notas de avaliação (`vote_average`);
* Inclusão do link completo para os pôsteres dos filmes;
* Remoção de colunas desnecessárias.

#### ☁️ **Carga**

Os dados tratados foram **carregados para um banco de dados PostgreSQL na nuvem**, permitindo consultas otimizadas e integração direta com ferramentas de análise.

---

### 🔹 2. EDA — Análise Exploratória de Dados (no PostgreSQL)

Com a base carregada no banco, foram realizadas consultas SQL para responder a questões analíticas, como:

* Identificação dos **Top 3 filmes mais populares**;
* Análise dos **gêneros mais populares**;
* Cálculo das **médias de avaliação por gênero**;
* Estudo da **popularidade dos filmes ao longo dos anos**, observando se filmes mais novos possuem maior repercussão.

Essas consultas formaram a base para a construção do dashboard analítico.

---

### 🔹 3. Dashboard Interativo

Foi desenvolvido um **dashboard interativo** para visualização dos resultados obtidos, contendo:

* 🎥 **Top 3 Filmes Mais Populares**
  Exibe os filmes com maiores índices de popularidade.

* 🎭 **Análise dos Gêneros Mais Populares**
  Mostra quais gêneros atraem mais atenção do público.

* ⭐ **Gêneros com Maiores Médias de Avaliação**
  Indica os gêneros com melhor desempenho crítico.

* 📆 **Popularidade dos Filmes por Ano**
  Permite observar a tendência temporal da popularidade (filmes mais recentes tendem a ser mais populares).

* 🔍 **Filtros Interativos**
  Filtros por **gênero**, **ano de lançamento** e **idioma original**, permitindo análises dinâmicas e personalizadas.



---

## 🧠 Tecnologias Utilizadas

| Etapa         | Tecnologias                    |
| ------------- | ------------------------------ |
| Extração      | Python, Requests, Pandas       |
| Transformação | Pandas, NumPy                  |
| Carga         | SQLAlchemy, PostgreSQL (nuvem) |
| EDA           | SQL (PostgreSQL)               |
| Visualização  | Power BI / Plotly Dash         |
| Outras        | API TMDB, Jupyter Notebook     |

---

## 📈 Resultados Esperados

Com base na análise e nas recomendações geradas, espera-se um **aumento de cerca de 20% no engajamento e retenção de usuários** nas plataformas de streaming, por meio de:

* Melhor curadoria de conteúdo;
* Priorização de gêneros mais atraentes;
* Lançamentos focados em filmes com características de alta popularidade.

---

## 🏁 Conclusão

O projeto apresentou uma visão abrangente sobre o comportamento dos filmes no mercado global, identificando padrões de popularidade, desempenho por gênero e tendências temporais.

Com o pipeline de **ETL automatizado**, o **banco de dados estruturado** e o **dashboard interativo**, é possível atualizar e visualizar os dados em tempo real, fornecendo uma base sólida para **decisões estratégicas em plataformas de streaming** e **estudos de mercado cinematográfico**.

---

