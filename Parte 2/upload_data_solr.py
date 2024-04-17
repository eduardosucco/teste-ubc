import pandas as pd
import unicodedata
import pysolr
import logging
from datetime import datetime

# Configurando o logger principal
current_date = datetime.now().strftime("%Y%m%d")
log_filename = f"log_upload_data_solr_{current_date}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

# Função para registrar mensagens de log com a data, hora e milissegundos atuais
def log_info(message):
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
    logging.info(f"{current_time}: {message}")

# Função para normalizar os headers do DataFrame
def normalize_headers(df):
    df.columns = [unicodedata.normalize('NFD', col).encode('ascii', 'ignore').decode('utf-8').replace(' ', '_').lower() for col in df.columns]

# Função para formatar a data no DataFrame
def format_date(df, column):
    df[column] = pd.to_datetime(df[column]).dt.strftime('%Y-%m-%dT%H:%M:%SZ')

# Função para assegurar que cada linha tenha um ID único
def ensure_id(df):
    if 'id' not in df.columns:
        df.insert(0, 'id', range(1, len(df) + 1))
    else:
        df['id'] = range(1, len(df) + 1)

# Função para validar o formato da data no DataFrame
def validate_date_format(df):
    try:
        pd.to_datetime(df['data_de_nascimento'])
        return True, "DataFrame valido", None
    except ValueError as e:
        id_erro = df.loc[pd.to_datetime(df['data_de_nascimento'], errors='coerce').isnull(), 'id'].iloc[0]
        return False, f"Erro: {str(e)}", id_erro

# Função para deletar documentos existentes no Solr
def delete_existing_documents(solr):
    solr.delete(q='*:*')
    log_info("Documentos existentes excluidos do Solr.")

# Função para importar dados para o Solr
def import_to_solr(df, solr):
    documents = df.to_dict(orient='records')
    solr.add(documents)

# Início do processo
start_time = datetime.now()
log_info("--------------------------------------------------------------------")
log_info("Iniciando o processo de carga, transformacao e importacao dos dados.")

# Mudar o nome do arquivo para realizar upload
file_name = 'aluno.csv'

# Configuration and connection setups
solr_url = 'http://localhost:8983/solr/Alunos'
solr = pysolr.Solr(solr_url, always_commit=True)

try:
    # Carregando os dados do arquivo CSV
    log_info("Carregando dados do arquivo CSV.")
    dataframe = pd.read_csv(file_name)

    # Normalizando headers, formatando datas e assegurando IDs unicos
    log_info("Normalizando headers, formatando datas e assegurando IDs unicos.")
    normalize_headers(dataframe)
    format_date(dataframe, 'data_de_nascimento')
    ensure_id(dataframe)

    # Validando o formato da data
    log_info("Validando formato da data.")
    is_valid, message, error_id = validate_date_format(dataframe)
    if not is_valid:
        log_info(f"Erro encontrado no ID: {error_id}. Mensagem: {message}")
    
    # Deletando documentos existentes no Solr
    delete_existing_documents(solr)
    # Importando dados para o Solr
    import_to_solr(dataframe, solr)

    log_info("Dados importados para o Solr com sucesso.")

except Exception as e:
    log_info(f"Ocorreu um erro durante o processo: {str(e)}")

# Fim do processo
end_time = datetime.now()
duration = end_time - start_time
log_info(f"Fim do processo de carga, transformacao e importacao dos dados. Duracao: {duration}")
