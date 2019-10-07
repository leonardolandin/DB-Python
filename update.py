import mysql.connector
import sys
import time
from pymongo import MongoClient

connect = mysql.connector.MySQLConnection(host='teroria.mysql.uhserver.com', database='teroria',user='teoriadopc', password='@T20192')
mongo = MongoClient('mongodb://localhost:27017/')
mongodb = mongo.teoria
collection = mongodb.usuario
cursor = connect.cursor()

print("================= Bem-vindo ao sistema de edição de cadastro =================")
print("================= Por favor, insira as informações =================")

nome = str(input("Digite seu nome: "))
if (len(nome) > 255) :
    print("O nome digitado passa dos limites propostos")
    sys.exit()

email = str(input("Digite seu e-mail: "))
if (len(email) > 100) :
    print("O e-mail digitado passa dos limites propostos")
    sys.exit()

senha = str(input("Digite sua senha: "))
if (len(senha) > 45) :
    print("A senha digitado passa dos limites propostos")
    sys.exit()

telefone = int(input("Digite seu numero de telefone (COM DDD): "))
if (len(str(telefone)) > 12) :
    print("O telefone informado passa dos limites propostos")
    sys.exit()

ini = time.time()
for i in range(0, 1000):
    cadastrar = ("UPDATE USUARIO set nome = %s, email = %s, senha = %s, telefone = %s where idUSUARIO = " + str(i))

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
    where = {"id": i}
    valores = {"$set" : {"nome" : nome, "email": email, "senha": senha, "telefone": telefone}}
    collection.update_many(where, valores)
finalmongo = time.time()
tempomongo = finalmongo - inimongo
print("O tempo de gravação no Mongo é: " + str(int(tempomongo)))
