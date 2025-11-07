from ETL.extrair import extrair
from ETL.transformar import *
from ETL.carregar import carregar_para_banco
from utils import *
from sqlalchemy import create_engine



if __name__ == "__main__":
    """
    Executa o pipeline completo de ETL.
    """
    # Extração
    df_acao = extrair(28, "Action") 
    df_comedia = extrair(35, "Comedy") 
    df_drama = extrair(18, "Drama") 
    df_aventura = extrair(12, "Adventure") 
    df_animacao = extrair(16, "Animation") 
    df_crime = extrair(80, "Crime") 
    df_documentario = extrair(99, "Documentary") 
    df_familia = extrair(10751, "Family") 
    df_fantasia = extrair(14, "Fantasy") 
    df_historia = extrair(36, "History") 
    df_terror = extrair(27, "Horror") 
    df_misterio = extrair(9648, "Mystery") 
    df_scifi = extrair(878, "Science Fiction") 
    df_thriller = extrair(53, "Thriller") 
    df_guerra = extrair(10752, "War") 
    df_faroeste = extrair(37, "Western") 
    dfs = [df_acao, df_comedia, df_drama, df_aventura, df_animacao, df_crime, df_documentario, df_familia, df_fantasia, df_historia, df_terror, df_misterio, df_scifi, df_thriller, df_guerra, df_faroeste] df_final = pd.concat(dfs, ignore_index=True)

    df_final = pd.concat(dfs, ignore_index=True)

    # Transformação
    df = transformar_dados(df_final)


    # --- 1️⃣ Criar a conexão com o banco Postgres ---
    engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}sslmode=require")
    carregar_para_banco(df, engine)

    print("🎯 Pipeline ETL finalizado com sucesso!")