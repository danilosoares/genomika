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
	conn.commit()
	
	disease_exists = False
	gene_exists = False

	for row in rows:
		cursor = conn.execute("SELECT id FROM phenos_disease where name=(" + "'" + row[2] + "'" + ")")
		cursor_genes = conn.execute("SELECT id FROM phenos_gene where name=(" + "'" + row[1] + "'" + ")")

		diseases=cursor.fetchall()
		genes = cursor_genes.fetchall()

		if not diseases:
			conn.execute("INSERT INTO phenos_disease(id,name) VALUES(" + str(row[0]) + "," + "'" + str(row[2]) + "'" + ")")
			conn.commit()
		else:
			for disease in diseases:
				disease_id_to_insert = disease[0]
				disease_exists = True

		if not genes:
			conn.execute("INSERT INTO phenos_gene (id,name) VALUES(" + str(row[0]) + "," + "'" + str(row[1]) + "'" + ")")
			conn.commit()
	 	else:
	 		for gene in genes:
	 			gene_id_to_insert = gene[0]
	 			gene_exists = True
		
		if gene_exists and disease_exists:	
			conn.execute("INSERT INTO phenos_diseasegene (gene_id,disease_id) VALUES(" + str(gene_id_to_insert) + "," + str(disease_id_to_insert) + ")")
			conn.commit()
		elif gene_exists and not(disease_exists):
			conn.execute("INSERT INTO phenos_diseasegene (gene_id,disease_id) VALUES(" + str(gene_id_to_insert) + "," + str(row[0]) + ")")
			conn.commit()
		elif not(gene_exists) and disease_exists:
			conn.execute("INSERT INTO phenos_diseasegene (gene_id,disease_id) VALUES(" + str(row[0]) + "," + str(disease_id_to_insert) + ")")
			conn.commit()
		elif not(gene_exists) and not(disease_exists):
			conn.execute("INSERT INTO phenos_diseasegene (gene_id,disease_id) VALUES(" + str(row[0]) + "," + str(row[0]) + ")")
			conn.commit()

		disease_exists = False
		gene_exists = False
		
	conn.close()

print "Dados Atualizados Com Sucesso!"
