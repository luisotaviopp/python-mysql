import mysql.connector
import os


# Variables
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_database = 'testepy'
db_charset = 'utf8'


# Start Connection
connection = mysql.connector.connect(host=db_host,
                                     user=db_user,
                                     password=db_password,
                                     database=db_database,
                                     charset=db_charset)

cursor = connection.cursor(dictionary=True)


def clear(): os.system('clear')


def back_to_menu():
    opt = input("\n Back to menu? (y/n)")

    if opt == 'y' or opt == 'Y':
        menu()
    else:
        quit()


def menu():
    print('\n')
    print('Select your next action:')
    print('1. List all users')          # pronto
    print('2. Search user by name.')
    print('3. Search user by id.')
    print('4. Insert new user.')
    print('5. Delete user.')
    print('6. Edit user.')
    print('7. Count by gender.')
    print('8. Quit.\n')

    opt = input('Select your next move (1 ~ 8): ')

    if opt == '1':
        clear()
        list_users()
    elif opt == '2':
        search_user_by_name()
    elif opt == '3':
        search_user_by_id()
    elif opt == '4':
        insert_user()
    elif opt == '5':
        delete_user()
    elif opt == '6':
        edit_user()
    elif opt == '7':
        get_count_by_gender()
    elif opt=='8':
        quit()
    else:
        print("Opcão incorreta")
        menu()


def list_users():
    clear()

    comando = "SELECT * FROM user"

    cursor.execute(comando)
    users = cursor.fetchall()

    for user in users:
        print('ID:' + str(user['id']) + ' Name: ' + user['name'] + ' Gender: ' + user['gender'] + ' Age: ' + str(user['age']))

    # print(users)        # pegando todos os usuários
    # print(users[0])     # pegando apenas o primeiro usuário

    back_to_menu()


def search_user_by_name():
    clear()

    user_name = input("Type the name of the user you want to search: ")
    comando = "SELECT * FROM user WHERE user.name LIKE '%" + str(user_name) + "%' "

    cursor.execute(comando)
    users = cursor.fetchall()

    for user in users:
        print('ID:' + str(user['id']) + '\nNome: ' + user['name'] + '\nSexo: ' + user['gender'] + '\nIdade: ' + str(user['age']) + '\n')

    back_to_menu()


def search_user_by_id():
    clear()

    user_name = input("Type the id of the user you want to search: ")
    comando = "SELECT * FROM user WHERE user.id = " + str(user_name)

    cursor.execute(comando)
    users = cursor.fetchall()

    for user in users:
        print('\nNome: ' + user['name'] + '\nSexo: ' + user['gender'] + '\nIdade: ' + str(
            user['age']) + '\n')

    back_to_menu()


def insert_user():
    clear()

    qtd = input("How many users you want to add? ")
    for i in range(int(qtd)):
        print('\nUser {}'.format(i+1))
        name = input('User {} - Name: '.format(i+1))
        age = input('User {} - Age: '.format(i+1))
        gender = input('User {} - Gender (masc, fem, other): '.format(i+1))
        cursor.execute("INSERT INTO user(name, age, gender) VALUES('{}',{},'{}')".format(name, age, gender))
        connection.commit()
        print('\nUser {} inserted.'.format(i + 1))

    back_to_menu()


def delete_user():
    clear()

    user_id = input('Insert the ID of the user you want to delete:  ')
    cursor.execute("DELETE FROM user WHERE id = {}".format(user_id))
    connection.commit()

    back_to_menu()


def edit_user():
    clear()

    user_id = input('User Id: ')
    user_name = input('Name: ')
    user_age = input('Age: ')
    user_gender = input('Gender: ')
    cursor.execute("UPDATE user SET name = '{}', age = {}, gender = '{}' WHERE id = {}".format(user_name, user_age, user_gender, int(user_id)))
    connection.commit()

    back_to_menu()


def get_count_by_gender():
    clear()

    #male
    comando = "SELECT COUNT(gender) as result FROM user WHERE gender = 'masc'; "
    cursor.execute(comando)
    result = cursor.fetchall()
    print("This database has {} male users.".format(str(result[0]['result'])))

    #female
    comando = "SELECT COUNT(gender) as result FROM user WHERE gender = 'fem'; "
    cursor.execute(comando)
    result = cursor.fetchall()
    print("This database has {} female users.".format(str(result[0]['result'])))

    #others
    comando = "SELECT COUNT(gender) as result FROM user WHERE gender = 'other'; "
    cursor.execute(comando)
    result = cursor.fetchall()
    print("This database has {} user(s) from other genders.".format(str(result[0]['result'])))

    back_to_menu()


def quit():
    clear()
    print("Bye :)")


# Start application
menu()
