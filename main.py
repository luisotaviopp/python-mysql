import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='', database='testepy', charset='utf8')
cursor = connection.cursor(dictionary=True)

# INSERT Simples
# cursor.execute("INSERT into user(name, age, gender) VALUES('Luis', 29, 'masc') ")
# connection.commit()

# INSERT
# name = input('Digite um nome: ')
# age = input('Digite a idade: ')
# gender = input('Digite o gênero (masc, fem, other): ')
# cursor.execute("INSERT INTO user(name, age, gender) VALUES('{}',{},'{}')".format(name, age, gender))
# connection.commit()

# DELETE
# id = input('Digite o ID do usuário que você quer deletar: ')
# cursor.execute("DELETE FROM user WHERE id = {}".format(id))
# connection.commit()

# SELECT
comando = "SELECT * FROM user"
cursor.execute(comando)
users = cursor.fetchall()

print(users)        # pegando todos os usuários
print(users[0])     # pegando apenas o primeiro usuário

# Formantando a lista.
# O str() é para converter o int para String antes de imprimir.

for user in users:
    print('Nome: ' + user['name'] + '\nSexo: ' + user['gender'] + '\nIdade: ' + str(user['age']) + '\n')
