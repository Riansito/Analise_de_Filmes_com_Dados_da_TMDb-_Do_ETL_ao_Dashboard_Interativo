import pandas as pd
import requests
import time
from utils import api_key

def extrair(genre_id, genre_name, paginas=5):
    filmes = []
    for p in range(1, paginas + 1):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&with_genres={genre_id}&page={p}"
        r = requests.get(url)
        if r.status_code != 200:
            print(f"Erro ao buscar página {p} do gênero {genre_name}: {r.status_code}")
            continue
        
        data = r.json()
        filmes.extend(data.get("results", []))
        time.sleep(1.5)
    
    df = pd.DataFrame(filmes)
    df["genre"] = genre_name
    print(f"{genre_name}: {len(df)} filmes coletados")
    return df
