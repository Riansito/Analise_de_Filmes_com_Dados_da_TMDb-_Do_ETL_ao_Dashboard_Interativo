import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def carregar_para_banco(df, engine):
    df.to_sql('filmes', con=engine, index=False, if_exists='replace')
    print("Carga dos dados feita com sucesso!")