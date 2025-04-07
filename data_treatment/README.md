<h1 style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
  <span>Data Treatment</span>
  <span style="font-size: 16px">
    <a href="README.md">en</a> |
    <a href="pt-br.md">pt-br</a>
  </span>
</h1>

Just a simple data treatment pipeline.

## Pipeline

- ✅ Check if file exists
- ✅ Load the file dataset
- ✅ Clean data
- ✅ Save it into database
<!-- - ✅ Transform data -->

## Prerequisites

- Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
- Make sure you have PostgreSQL database available, or simply make sure you have Docker installed. You can download it from [docs.docker.com](https://docs.docker.com/get-started/get-docker/).

## Installation

1. **Enter folder:**

   ```bash
   cd data_treatment
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```

   ***Enter virtual environment:***

   Linux
   ```bash
   source venv/bin/activate 
   ```
   Windows
   ```psl
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Create an `.env` file (you can use the example in: `.env.example`)

2. Make sure you have Postgres database up and running, OR just run
```bash
docker compose up -d
```

3. Download the dataset at: [Tabela Fipe](https://www.kaggle.com/datasets/franckepeixoto/tabela-fipe), place it inside the folder `data`, and check the enviroment variable correspondent to it is both correct and active

4. Run the main script:

```bash
python main.py
```

## License

[MIT](LICENSE) – Feel free to use and modify.