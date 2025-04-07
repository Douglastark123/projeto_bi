import pandas as pd
from unidecode import unidecode

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and Transform data."""
    if df is None or df.empty:
        print("Erro: Dataset vazio ou inválido.")
        return None
    
    # Makes a copy to work with, and not alter the original
    df_clean = df.copy()
    
    print("Iniciando limpeza e transformação dos dados...")
    
    # 1. Remove duplicatas
    duplicates_before = df_clean.shape[0]
    df_clean = df_clean.drop_duplicates()
    duplicates_removed = duplicates_before - df_clean.shape[0]
    print(f"Duplicatas removidas: {duplicates_removed}")
    
    # 2. Handle missing values
    prior_missing_values = df_clean.isna().sum().sum()
    
    # Numeric columns - replace NaN for column median
    for column in ['anoModelo', 'anoReferencia']:
        if column in df_clean.columns:
            df_clean[column] = df_clean[column].fillna(df_clean[column].median())
    
    # Text columns - replace NaN for "Desconhecido"
    for column in ['marca', 'modelo']:
        if column in df_clean.columns:
            df_clean[column] = df_clean[column].fillna("Desconhecido")
    
    # FIPE code - replace NaN for "N/A"
    if 'codigoFipe' in df_clean.columns:
        df_clean['codigoFipe'] = df_clean['codigoFipe'].fillna("N/A")
    
    post_missing_values = df_clean.isna().sum().sum()
    print(f"Valores ausentes tratados: {prior_missing_values - post_missing_values}")
    
    # 3. Standardize columns 'marca' and 'modelo'
    if 'marca' in df_clean.columns:
        df_clean['marca'] = df_clean['marca'].str.lower().str.strip()
        df_clean['marca'] = df_clean['marca'].apply(lambda x: unidecode(str(x)) if isinstance(x, str) else x)
        df_clean['marca'] = df_clean['marca'].str.title()
    
    if 'modelo' in df_clean.columns:
        df_clean['modelo'] = df_clean['modelo'].str.lower().str.strip()
        df_clean['modelo'] = df_clean['modelo'].apply(lambda x: unidecode(str(x)) if isinstance(x, str) else x)
        df_clean['modelo'] = df_clean['modelo'].str.title()
    
    print("Limpeza e transformação concluídas com sucesso.")
    return df_clean