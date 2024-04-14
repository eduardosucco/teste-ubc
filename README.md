# Parte 2

Esta parte contém instruções para configurar uma instância do Apache Solr usando Docker e realizar o upload de um arquivo CSV no Apache Solr fazendo as devidas validações.

## Instruções de Uso

1. **Criar Instância Docker:**

   Para criar uma instância do Docker, execute o seguinte comando:

   ```
   docker run -d -p 8983:8983 --name solr_instance -t solr
   ```

2. **Acessar a Interface do Solr Admin:**

   Após a criação da instância, acesse a interface do Solr Admin em [http://localhost:8983/solr](http://localhost:8983/solr).

3. **Criar Core:**

   No Solr Admin Interface, crie um novo core chamado "Alunos".

4. **Definir Configurações e Esquema:**

   Após a criação do core, execute os seguintes comandos para definir as configurações e o esquema necessários:

   ```
   docker cp solrconfig.xml solr_instance:/var/solr/data/Alunos/solrconfig.xml
   docker cp schema.xml solr_instance:/var/solr/data/Alunos/schema.xml
   ```

5. **Adicionar CSV:**

   Coloque o arquivo CSV desejado na raiz do projeto.

6. **Configurar Upload de Dados:**

   Abra o arquivo `upload_data_solr.py` e modifique a variável `file_name` com o caminho do arquivo CSV desejado.

## Observações

Certifique-se de ter o Docker instalado e em execução no seu sistema antes de seguir estas instruções.
