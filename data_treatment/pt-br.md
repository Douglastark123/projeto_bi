<h1 style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
  <span>Project name</span>
  <span style="font-size: 16px">
    <a href="README.md">en</a> |
    <a href="pt-br.md">pt-br</a>
  </span>
</h1>

Apenas um pipeline simples de tratamento de dados.

## Pipeline

- ✅ Verificar se o arquivo existe  
- ✅ Carregar o dataset do arquivo  
- ✅ Limpar os dados  
- ✅ Salvar no banco de dados  
<!-- - ✅ Transformar os dados -->

## Pré-requisitos

- Certifique-se de que o Python está instalado. Você pode baixá-lo em [python.org](https://www.python.org/).  
- Certifique-se de que um banco de dados PostgreSQL está disponível ou, simplesmente, de que o Docker está instalado. Você pode baixá-lo em [docs.docker.com](https://docs.docker.com/get-started/get-docker/).

## Instalação

1. **Entre na pasta:**

   ```bash
   cd data_treatment
   ```

2. **(Opcional) Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

   ***Entre no ambiente virtual:***

   Linux:
   ```bash
   source venv/bin/activate 
   ```
   Windows:
   ```ps1
   venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Como executar

1. Crie um arquivo `.env` (você pode usar o exemplo em: `.env.example`)

2. Certifique-se de que o banco de dados Postgres está rodando, OU apenas execute:
```bash
docker compose up -d
```

3. Baixe o dataset em: [Tabela Fipe](https://www.kaggle.com/datasets/franckepeixoto/tabela-fipe), coloque-o dentro da pasta `data` e verifique se a variável de ambiente correspondente está correta e ativa.

4. Execute o script principal:

```bash
python main.py
```

## Licença

[MIT](LICENSE) – Sinta-se à vontade para usar e modificar.
