import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
import os

tables_columns = {
  "employee_final": [
    "id_employee",
    "name",
    "surname",
    "cpf",
    "status",
    "role",
    "initial_date",
    "end_date",
    "store_id"
  ],
  "sku_cost": [
    "cod_prod",
    "data_inicio",
    "data_fim",
    "custo"
  ],
  "sku_dataset": [
    "cod_prod",	
    "nome_abrev",
    "nome_completo",
    "descricao",	
    "categoria",	
    "sub_categoria",	
    "marca",	
    "conteudo_valor",	
    "conteudo_medida"
  ],
  "sku_price": [
    "cod_prod",	
    "data_inicio",	
    "data_fim",
    "preco"
  ],
  "sku_status_dataset": [
    "cod_prod",
    "data_inicio",	
    "data_fim"
  ],
  "store_final": [
    "nome_loja",
    "regiao",
    "diretoria",
    "data_inauguracao"
  ],
  "target_store_final": [
    "month",
    "store_id",
    "sales_target"
  ],
  "target_salesperson_final": [
    "id_employee",
    "sales_target",
    "month"
  ],
  "year": [
    "data",
    "cod_vendedor",
    "cod_loja",
    "cod_transacao",
    "quantidade",
    "cod_prod",
    "preco"
  ]
}

def process_data(data):
  # TODO
  print("Processing data...")

def prepare_dataframe_for_insert(filename, df):
  df['date_ingestion'] = datetime.now()
  df['data_row'] = df.apply(lambda row: row.to_json(), axis=1)
  df['tag'] = filename.replace(".parquet", "")
  
  return df[['date_ingestion', 'data_row', 'tag']]

# ======== Function to convert csv file to parquet ========== #    
def convert_to_parquet(filename, temp_folder):
  if filename.endswith(".csv"):
    csv_path = os.path.join(temp_folder, filename)
    parquet_path = os.path.join(temp_folder, filename.replace(".csv", ".parquet"))
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, index=False)
    print(f"Convertido: {csv_path} -> {parquet_path}")

# ======== Function to convert json file to parquet ========== #    
def convert_to_other_type(filename, temp_folder):
  if filename.endswith(".csv"):
    csv_path = os.path.join(filename)
    json_path = os.path.join(temp_folder, filename.replace(".csv", ".json"))
    df = pd.read_csv(csv_path)
    df.to_json(json_path, index=False)
    print(f"Convertido: {csv_path} -> {json_path}")

def validate_file(filename, df):
  columns = df.columns
  
  if '20' in filename:
    filename = 'year'

  for data in tables_columns:
    if data in filename:  
      
      for column in columns:
        if column not in tables_columns[data]:
          return False
      
  return True
