import mysql.connector
import time
from pymongo import MongoClient

connect = mysql.connector.MySQLConnection(host='localhost', database='teoria',user='root', password='root')
mongo = MongoClient('mongodb://localhost:27017/')
mongodb = mongo.teoria
collection = mongodb.usuario
cursor = connect.cursor()

print("================= Bem-vindo ao sistema de edição de cadastro =================")

totalsql = 0
mongotp = 0
nome = 0
email = 0
senha = 0
telefone = 0

ini = time.time()
for j in range(0, 50):
    for i in range(0, 1000):
        nome = nome + 1
        email = email + 1
        senha = senha + 1
        telefone = telefone + 1
        cadastrar = ("UPDATE USUARIO set nome = %s, email = %s, senha = %s, telefone = %s where idUSUARIO = " + str(i))

        informacoes = (nome, email, senha, telefone)
        cursor.execute(cadastrar, informacoes)
        connect.commit()

    final = time.time()
    tempo = final - ini
    print("O tempo de gravação no SQL é: " + str(int(tempo)))

    inimongo = time.time()
    for i in range(0, 1000):
        nome = nome + 1
        email = email + 1
        senha = senha + 1
        telefone = telefone + 1

        where = {"id": i}
        valores = {"$set" : {"nome" : nome, "email": email, "senha": senha, "telefone": telefone}}
        collection.update_many(where, valores)
    finalmongo = time.time()
    tempomongo = finalmongo - inimongo
    print("O tempo de gravação no Mongo é: " + str(int(tempomongo)))

    totalsql = totalsql + tempo
    mongotp = mongotp + tempomongo

cursor.close()
connect.close()
print("Mongo" + str(int(mongotp)))
print("SQL" + str(int(totalsql)))
