import os

def file_exists(file: str):
    if not os.path.isfile(file):
        print(f"Erro: O arquivo {file} não existe.")
        return False
    return True