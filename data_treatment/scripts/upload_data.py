import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm  # <- Progress bar

from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_URL_PARAMS

def save(df: pd.DataFrame, table_name: str, chunksize: int = 10000) -> bool:
    """
    Push DataFrame into a PostgreSQL database with a progress bar.
    """
    try:
        # Create connection string
        url_params = f"?{POSTGRES_URL_PARAMS}" if POSTGRES_URL_PARAMS != "" else ""
        port = f":{POSTGRES_PORT}" if POSTGRES_PORT != "" else ""
        db_connect = (
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}{port}/{POSTGRES_DB}{url_params}"
        )
        engine = create_engine(db_connect)

        total_rows = len(df)
        print(f"Iniciando upload de {total_rows} linhas para a tabela '{table_name}'...")

        # Drop and create new table with first chunk
        df.iloc[:chunksize].to_sql(table_name, engine, if_exists='replace', index=False, method='multi', chunksize=1000)

        # Insert the remaining in chunks
        with tqdm(total=total_rows, desc="Upload Progress", unit="rows", initial=chunksize) as pbar:
            for i in range(chunksize, total_rows, chunksize):
                df.iloc[i:i + chunksize].to_sql(
                    table_name,
                    engine,
                    if_exists='append',
                    index=False,
                    method='multi'
                )
                pbar.update(len(df.iloc[i:i + chunksize]))

        print(f"✅ Dados salvos com sucesso na tabela '{table_name}' do PostgreSQL.")
        return True

    except Exception as e:
        print(f"❌ Erro ao salvar no PostgreSQL: {e}")
        return False
