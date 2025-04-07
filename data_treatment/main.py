import pandas as pd
from config import DATASET_FILE, POSTGRES_TABLE
from scripts import (
    file_exists,
    load_data,
    transform_data,
    save
)

def main():
    # 1. check if file exists
    if not file_exists(file=DATASET_FILE):
        return
    
    # 2. load dataset
    df_raw: pd.DataFrame = load_data(DATASET_FILE)
    if df_raw is None:
        return
    
    # 3. clean and transform data
    processed_data: pd.DataFrame = transform_data(df_raw)
    if processed_data is None:
        return
    
    # show some basic stats
    print("\nResumo dos dados após limpeza:")
    print(f"Total de registros: {processed_data.shape[0]}")
    if 'marca' in processed_data.columns:
        print(f"Marcas únicas: {processed_data['marca'].nunique()}")
    if 'modelo' in processed_data.columns:
        print(f"Modelos únicos: {processed_data['modelo'].nunique()}")
    if 'valor' in processed_data.columns:
        print(f"Valor médio: R${processed_data['valor'].mean():.2f}")
        print(f"Valor mínimo: R${processed_data['valor'].min():.2f}")
        print(f"Valor máximo: R${processed_data['valor'].max():.2f}")
    
    # 4. push to database
    save(df=processed_data, table_name=POSTGRES_TABLE)

if __name__ == "__main__":
    main()