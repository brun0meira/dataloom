from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
import core.supabase_client as supabase_client
import core.clickhouse_client as clickhouse_client
import core.data_processing as data_processing
import core.threads as threads
import pandas as pd

app = Flask(__name__)

# Create bucket if not exist
supabase_client.create_bucket('data')

# Create table if not exist
create_table_sql = os.path.join("sql/create_table.sql")
clickhouse_client.execute_sql_script(create_table_sql)

@app.errorhandler(404)
def not_found(error):
  return jsonify({"error": "Endpoint not found"}), 404
  
@app.route('/ingestion-csv', methods=['POST'])
def ingestion_csv():
  if 'file' not in request.files:
    return jsonify({"error": "No file found"}), 400
  
  for file in request.files.getlist('file'):
    if file and file.filename.endswith('.csv'):
      temp_folder = 'temp'
      csv_path = os.path.join(temp_folder, file.filename)
      
      try:
        # Cria uma pasta temp localmente
        os.makedirs(temp_folder, exist_ok=True)
        
        # Salva o arquivo CSV na pasta temp
        file.save(csv_path)
        
        # Converte o CSV para Parquet
        data_processing.convert_to_parquet(file.filename, temp_folder)
        
        # Faz upload do arquivo Parquet para o Supabase
        parquet_filename = file.filename.replace(".csv", ".parquet")
        parquet_path = os.path.join(temp_folder, parquet_filename)
        supabase_client.upload_file('data', parquet_path, parquet_filename)
        
        threads.transform_and_save(parquet_filename)
      except Exception as e:
        print(e)
        
      try:
          os.remove(csv_path)
          parquet_path = csv_path.replace(".csv", ".parquet")
          os.remove(parquet_path)
          print(f"Arquivo temp deletado com sucesso.")
      except Exception as e:
          print(f"Erro ao deletar o arquivo '{csv_path}': {e}") # noqa
          
      return jsonify({"message": "Arquivo convertido e upload feito com sucesso!"}), 200
    
    else:
      return jsonify({"error": "Formato de arquivo não permitido"}), 400

@app.route('/ingestion-json', methods=['POST'])
def ingestion_json():
  data = request.get_json()
  
  if not data or len(data) < 1:
    return jsonify({"error": "Invalid data"}), 400
  
  return data

@app.route('/bucket', methods=['POST'])
def create_bucket():
  data = request.get_json()
  
  if not data or 'bucket_name' not in data:
    return jsonify({"error": "Insira o nome de um bucket"}), 400

  else:
    print(data['bucket_name'])
    res = supabase_client.create_bucket(data['bucket_name'])
    return res

@app.route('/bucket', methods=['GET'])
def get_all_buckets():
  res = supabase_client.list_buckets()
  return res

@app.route('/save-data', methods=['POST'])
def save_data():
  data = request.get_json()
  filename = data['filename']
  
  parquet_path = f"temp/downloaded_{filename}"
  
  res = supabase_client.download_file("data", filename, parquet_path)
  
  df = pd.read_parquet(parquet_path)
  validation = data_processing.validate_file(filename, df)
  
  if not validation:
    return {"error": "Validation fail"}, 400
  
  df_prepared = data_processing.prepare_dataframe_for_insert(filename, df)
  
  client = clickhouse_client.get_client()
  res = clickhouse_client.insert_dataframe(client, 'working_data', df_prepared)
  
  try:
    os.remove(parquet_path)
    print(f"Arquivo temp deletado com sucesso.")
  except Exception as e:
      print(f"Erro ao deletar o arquivo '{csv_path}': {e}")      
  
  return {"ok": "Success to save the data"}

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)