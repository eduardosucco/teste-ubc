import pandas as pd
import unicodedata
import pysolr

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
    return df

def format_date(df, column):
    df[column] = pd.to_datetime(df[column]).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    return df

def ensure_id(df):
    if 'id' not in df.columns:
        df.insert(0, 'id', range(1, len(df) + 1))
    else:
        df['id'] = range(1, len(df) + 1)
    return df

def validate_date_format(df, date_column='data_de_nascimento'):
    try:
        pd.to_datetime(df[date_column])
        return True, "DataFrame válido", None
    except ValueError as e:
        id_erro = df.loc[pd.to_datetime(df[date_column], errors='coerce').isnull(), 'id'].iloc[0]
        return False, f"Erro: {str(e)}", id_erro

# Data loading and transformation
dataframe = pd.read_csv(file_name)
dataframe = normalize_headers(dataframe)
dataframe = format_date(dataframe, 'data_de_nascimento')
dataframe = ensure_id(dataframe)

# Validation
is_valid, message, error_id = validate_date_format(dataframe)
if not is_valid:
    print(f"Erro encontrado no ID: {error_id}. Mensagem: {message}")

# Solr functions
def delete_existing_documents(solr):
    solr.delete(q='*:*')

def import_to_solr(df, solr):
    delete_existing_documents(solr)
    documents = df.to_dict(orient='records')
    solr.add(documents)

# Executing the import
import_to_solr(dataframe, solr)
print("Arquivo CSV importado para o Solr com sucesso!")
