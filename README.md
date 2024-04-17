**Desafio Técnico para Analista de Dados e Importação para o Solr**
---

Aqui está o passo a passo da resolução de ambos os desafios, detalhando cada etapa realizada para atender aos requisitos dos produtos solicitados.

# Parte 1

Nesta seção, contém os passos para construção do dashboard com informações relacionadas ao ambiente acadêmico.

1. **Construção da Fonte de Dados**

   - Para ter a fonte de dados, utilizei a query "fonte_dados.sql" para criar três tabelas: Alunos, Matérias e Notas.

2. **Tratamento dos Dados no Power BI**

   Após a criação das tabelas, conectei as fontes de dados ao Power BI e executei os seguintes tratamentos para preparar os dados para uso:

   - Combinei as tabelas Alunos, Matérias e Notas utilizando as chaves correspondentes.
   - Identifiquei e tratei quaisquer valores ausentes ou inconsistentes.
   - Renomeei as colunas conforme necessário para facilitar a compreensão.
   - Converti os tipos de dados conforme apropriado (por exemplo, datas para o formato adequado).
   - Realizei outras transformações de dados necessárias para limpar e preparar os dados para análise.

3. **Criação das Visualizações**

   Com os dados prontos, criei a identidade visual e montei as visualizações de acordo com os requisitos solicitados. Isso incluiu:

   - Seleção de paleta de cores e fontes que refletissem a identidade do projeto.
   - Desenvolvimento de gráficos, tabelas e outros elementos visuais para representar os dados de forma clara e compreensível.
   - Organização lógica e intuitiva das visualizações para facilitar a análise dos dados.

4. **Dashboard Acadêmico**

   Após a construção das visualizações, disponibilizei o arquivo "Dashboard_Academico.pbix" contendo o dashboard completo com as três visões diferentes criadas.

   Este arquivo pode ser aberto no Power BI para explorar as visualizações e interagir com os dados.



# Parte 2

Esta seção contém instruções para configurar uma instância do Apache Solr usando Docker e realizar o upload de um arquivo CSV no Apache Solr com as devidas validações.

## Instruções de Uso

1. **Criar Instância Docker:**

   Execute o seguinte comando para criar uma instância do Docker:

   ```
   docker run -d -p 8983:8983 --name solr_instance -t solr
   ```

2. **Acessar a Interface do Solr Admin:**

   Após a criação da instância, acesse a interface do Solr Admin em [http://localhost:8983/solr](http://localhost:8983/solr).

3. **Criar Core:**

   Na interface do Solr Admin, crie um novo core chamado "Alunos".

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
