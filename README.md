**#Dependência a ser instalada
**
psycopg2 - pip install psycopg2

**#Tarefa 1
**

O modelo não está adequado para o problema. Como é possível uma doença estar associada a vários genes e um gene pode estar relacionado com várias doenças **(Vide exemplo no PDF do processo seletivo)**, é necessário implementar um relacionamento m:n, onde uma doença possui vários genes e um gene pode estar relacionado a várias doenças.

Desta forma, deve ser criada uma tabela de relacionamento contendo o os ids da tabela de genes e da tabela de doenças (gene_id, disease_id).