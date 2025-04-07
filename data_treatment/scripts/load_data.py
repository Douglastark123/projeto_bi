import pandas as pd

def load_data(file: str) -> pd.DataFrame:
    """Loads dataset from CSV file."""
    try:
        df = pd.read_csv(file, encoding='utf-8')
        print(f"Dataset carregado com sucesso. Formato: {df.shape}")
        return df
    except Exception as e:
        print(f"Erro ao carregar o dataset: {e}")
        return None