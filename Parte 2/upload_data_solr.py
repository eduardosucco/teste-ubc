import pandas as pd
import unicodedata
import pysolr
import logging
from datetime import datetime

# Obtendo a data atual para nomear o arquivo de log
current_date = datetime.now().strftime("%Y%m%d")
log_filename = f"log_upload_data_solr_{current_date}.log"

# Configurando o logger com o nome do arquivo personalizado
logging.basicConfig(filename=log_filename, level=logging.INFO)

# Função de log
def log_info(message):
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logging.info(f"{current_time}: {message}")

# Mudar o nome do arquivo para realizar upload
file_name = 'aluno.csv'

# Configuration and connection setups
solr_url = 'http://localhost:8983/solr/Alunos'
solr = pysolr.Solr(solr_url, always_commit=True)

# Helper functions
def unaccent(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def normalize_headers(df):
    df.columns = [unaccent(col.replace(' ', '_')).lower() for col in df.columns]
    log_info("Headers normalizados.")
    return df

def format_date(df, column):
    df[column] = pd.to_datetime(df[column]).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    log_info("Datas formatadas.")
    return df

def ensure_id(df):
    if 'id' not in df.columns:
        df.insert(0, 'id', range(1, len(df) + 1))
    else:
        df['id'] = range(1, len(df) + 1)
    log_info("ID assegurado.")
    return df

def validate_date_format(df, date_column='data_de_nascimento'):
    try:
        pd.to_datetime(df[date_column])
        log_info("Formato de data validado.")
        return True, "DataFrame válido", None
    except ValueError as e:
        id_erro = df.loc[pd.to_datetime(df[date_column], errors='coerce').isnull(), 'id'].iloc[0]
        log_info(f"Erro de formato de data encontrado. Mensagem de erro: {str(e)}. ID do erro: {id_erro}")
        return False, f"Erro: {str(e)}", id_erro

# Data loading and transformation
log_info("Iniciando processo de carga e transformação dos dados.")
dataframe = pd.read_csv(file_name)
dataframe = normalize_headers(dataframe)
dataframe = format_date(dataframe, 'data_de_nascimento')
dataframe = ensure_id(dataframe)

# Validation
log_info("Validando formato de datas.")
is_valid, message, error_id = validate_date_format(dataframe)
if not is_valid:
    log_info(f"Erro encontrado no ID: {error_id}. Mensagem: {message}")

# Solr functions
def delete_existing_documents(solr):
    solr.delete(q='*:*')
    log_info("Documentos existentes excluídos do Solr.")

def import_to_solr(df, solr):
    delete_existing_documents(solr)
    documents = df.to_dict(orient='records')
    solr.add(documents)
    log_info("Dados importados para o Solr com sucesso.")

# Executing the import
log_info("Iniciando processo de importação para o Solr.")
import_to_solr(dataframe, solr)
log_info("Arquivo CSV importado para o Solr com sucesso!")
