import mysql.connector
import sys
import time
from pymongo import MongoClient


connect = mysql.connector.MySQLConnection(host='teroria.mysql.uhserver.com', database='teroria',user='teoriadopc', password='@T20192')
mongo = MongoClient('mongodb://localhost:27017/')
mongodb = mongo.teoria
collection = mongodb.usuario
cursor = connect.cursor()

print("================= Bem-vindo ao sistema de cadastro =================")
print("================= Por favor, insira as informações =================")

nome = str(input("Digite o nome: "))
if (len(nome) > 255) :
    print("O nome digitado passa dos limites propostos")
    sys.exit()

email = str(input("Digite o e-mail: "))
if (len(email) > 100) :
    print("O e-mail digitado passa dos limites propostos")
    sys.exit()

senha = str(input("Digite a senha: "))
if (len(senha) > 45) :
    print("A senha digitado passa dos limites propostos")
    sys.exit()

telefone = int(input("Digite o numero de telefone (COM DDD): "))
if (len(str(telefone)) > 12) :
    print("O telefone informado passa dos limites propostos")
    sys.exit()

ini = time.time()
for i in range(0,1000):
    cadastrar = ("INSERT INTO USUARIO "
               "(idUSUARIO ,nome, email, senha, telefone) "
                "VALUES (idUSUARIO, %s, %s, %s, %s)")

    informacoes = (nome, email, senha, telefone)

    cursor.execute(cadastrar, informacoes)
    connect.commit()
cursor.close()
connect.close()
final = time.time()
tempo = final - ini
print("O tempo de gravação no SQL é: " + str(int(tempo)))


inimongo = time.time()
for i in range(0, 1000):
    usuario = [{
    "id": i,
    "nome": nome,
    "email": email,
    "senha": senha,
    "telefone": telefone
    }]
    insert = collection.insert_many(usuario)
    insert.inserted_ids
finalmongo = time.time()
tempomongo = finalmongo - inimongo
print("O tempo de gravação no Mongo é: " + str(int(tempomongo)))


