# -*- coding: utf-8 -*-

import psycopg2
import sqlite3

try:
	conn=psycopg2.connect("dbname='dfu5v18hea0jro' user='puxsikmrnjnnml' host='107.22.175.206' password='fpqWwIT73lFClOn23I1MMYpjP3'")
except:
    print "Erro ao conectar a base de dados"
else:
	cur=conn.cursor()
	cur.execute("""select * from pheno_db""")
	rows=cur.fetchall()
	conn.close()

try:
	conn = sqlite3.connect('db.sqlite3')
except:
	print "Erro ao conectar a base de dados!"
else:
	
	cur=conn.cursor()
	conn.execute("DELETE FROM phenos_gene")
	conn.execute("DELETE FROM phenos_disease")
	conn.execute("DELETE FROM phenos_diseasegene")

	for row in rows:
		conn.execute("INSERT INTO phenos_gene (name) VALUES(" + "'" + row[1] + "'" + ")")
		conn.execute("INSERT INTO phenos_disease (name) VALUES(" + "'" + row[2] + "'" + ")")

		gene = conn.execute("SELECT id FROM phenos_gene WHERE name=" + "'" + row[1] + "'")
		disease = conn.execute("SELECT id FROM phenos_disease WHERE name=" + "'" + row[2] + "'")

		for row in gene:
			gene_id = row[0]
		for row in disease:
			disease_id = row[0]

		conn.execute("INSERT INTO phenos_diseasegene (gene_id,disease_id) VALUES(" + str(gene_id) + "," + str(disease_id) + ")")

	conn.commit()
	conn.close()

print "Dados Atualizados Com Sucesso!"
