/* ============================================================
   🎬 ANÁLISE DE FILMES — EXPLORAÇÃO POR GÊNERO, ANO E IDIOMA
   ============================================================ */

/* ============================================================
   0️⃣ ESTRUTURA DA TABELA
   ============================================================ */
CREATE TABLE filmes (
    id INT PRIMARY KEY,
    original_language VARCHAR(10),
    overview TEXT,
    popularity DECIMAL,
    poster_path TEXT,
    release_date DATE,
    title TEXT,
    vote_average DECIMAL,
    vote_count INT,
    genre VARCHAR(50)
);

/* ============================================================
   🔍 CONSULTA BASE — VERIFICAÇÃO INICIAL DOS DADOS
   ============================================================ */
SELECT * FROM filmes;


/* ============================================================
   1️⃣ ANÁLISE POR GÊNERO — POPULARIDADE E DESEMPENHO
   ------------------------------------------------------------
   Objetivos:
   - Identificar quais gêneros são mais populares;
   - Comparar popularidade com nota média (qualidade crítica);
   - Detectar gêneros com apelo comercial, mas baixa avaliação.
   ============================================================ */
WITH status_filmes AS (
    SELECT 
        genre AS nome_gen, 
        AVG(popularity) AS media_popularidade,
        COUNT(*) AS quantidade,
        AVG(vote_average) AS media_nota
    FROM filmes
    GROUP BY genre
    ORDER BY media_popularidade DESC
)
SELECT
    nome_gen,
    media_popularidade, 
    quantidade,
    media_nota, 
    ROW_NUMBER() OVER() AS ranking
FROM status_filmes;


/* ============================================================
   2️⃣ ANÁLISE TEMPORAL — TENDÊNCIAS POR ANO DE LANÇAMENTO
   ------------------------------------------------------------
   Objetivos:
   - Avaliar variações de notas e popularidade ao longo do tempo;
   - Verificar se filmes recentes são mais populares;
   - Destacar os gêneros mais populares por ano.
   ============================================================ */

-- 📊 Popularidade e nota média por ano
SELECT 
    EXTRACT(YEAR FROM release_date) AS ano,
    AVG(popularity) AS media_popularidade,
    COUNT(*) AS quantidade,
    AVG(vote_average) AS media_nota
FROM filmes
GROUP BY ano
ORDER BY ano DESC;


-- 🏆 Top 5 gêneros mais populares por ano
WITH top_ano_genero AS (
    SELECT 
        ano, 
        genre, 
        media_popularidade, 
        media_nota,
        RANK() OVER(PARTITION BY ano ORDER BY media_popularidade DESC, ano DESC) AS rank
    FROM ( 
        SELECT 
            EXTRACT(YEAR FROM release_date) AS ano,
            genre,
            AVG(popularity) AS media_popularidade,
            COUNT(*) AS quantidade,
            AVG(vote_average) AS media_nota
        FROM filmes
        GROUP BY 1,2
        ORDER BY ano DESC
    ) a
)
SELECT 
    ano, 
    genre,
    media_popularidade,
    media_nota,
    rank
FROM top_ano_genero
WHERE rank BETWEEN 1 AND 5;


/* ============================================================
   3️⃣ ANÁLISE POR IDIOMA — DIVERSIDADE E ALCANCE GLOBAL
   ------------------------------------------------------------
   Objetivos:
   - Identificar os idiomas originais mais comuns;
   - Verificar quais idiomas dominam em popularidade e nota média;
   - Avaliar se o domínio do inglês é absoluto ou se há diversidade.
   ============================================================ */
SELECT 
    original_language,
    AVG(popularity) AS media_popularidade,
    AVG(vote_average) AS media_nota,
    COUNT(*) AS total_filmes
FROM filmes
GROUP BY original_language
HAVING COUNT(*) > 5
ORDER BY media_popularidade DESC;
