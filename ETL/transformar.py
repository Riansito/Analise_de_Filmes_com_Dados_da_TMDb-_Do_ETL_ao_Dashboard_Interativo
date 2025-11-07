import pandas as pd



def transformar_dados(df) -> pd.DataFrame:
    """
    Realiza o tratamento dos dados de filmes obtidos da API TMDb.

    Parâmetros:
        df (pd.DataFrame): DataFrame original com os filmes.
        api_key (str): Chave de acesso à API do TMDb.

    Retorna:
        pd.DataFrame: DataFrame transformado e limpo.
    """
    df_copy = df.copy()

    # Remove linhas com valores nulos
    df_copy.dropna(inplace=True)

    # Arredonda as notas de avaliação para 2 casas decimais
    df_copy["vote_average"] = df_copy["vote_average"].apply(lambda x: round(x, 2))

    # Adiciona o domínio completo para o poster
    link_site_api = "https://image.tmdb.org/t/p/w500"
    df_copy["poster_path"] = df_copy["poster_path"].apply(lambda x: f"{link_site_api}{x}")

    # Remove colunas que não serão utilizadas
    colunas_remover = ["backdrop_path", "adult", "original_title", "video", "genre_ids"]
    df_copy.drop(columns=colunas_remover, inplace=True)

    # Converte a coluna de data de lançamento para datetime
    df_copy["release_date"] = pd.to_datetime(df_copy["release_date"])

    #Removendo duplicatas
    df_copy.drop_duplicates(subset="id", inplace=True)

    print("Transformação dos dados feita com sucesso!")

    return df_copy

