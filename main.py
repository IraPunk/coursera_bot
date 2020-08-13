# This is a sample Python script.

import sys
import telebot
import mysql.connector
from mysql.connector import errorcode

bot = telebot.TeleBot("1173396580:AAEnKg7crQ5jyjIxYMku_g491BBfw06YwM4")

TOKEN = "1173396580:AAEnKg7crQ5jyjIxYMku_g491BBfw06YwM4"  # Берем токен из переменной окружения, которую добавили ранее
WEBHOOK_HOST = 'https://courseraalfbot.herokuapp.com'  # Здесь указываем https://<название_приложения>.herokuapp.com
WEBAPP_HOST = '0.0.0.0'  # Слушаем все подключения к нашему приложению
WEBAPP_PORT = os.environ.get('PORT')  # тк в Procfile мы указали process_type web, heroku сгенерирует нам нужный порт, его достаточно взять из переменной окружения

try:
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="irinaalferova",
      port="3306",
      database='coursera'
    )
    print(db)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    sys.exit()
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    sys.exit()
  else:
    print(err)
    sys.exit()



cursor = db.cursor()

# cursor.execute("CREATE DATABASE coursera")
#
# cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)


#cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255))")

# cursor.execute("SHOW TABLES")

# for x in cursor:
#   print(x)


# cursor.execute("ALTER TABLE users ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT UNIQUE)")

# sql = "INSERT INTO users (id, location) VALUES (%s, %s)"
# val = (1, "105.678")
# cursor.execute(sql, val)
# db.commit()

# print(cursor.rowcount, "запись добавлена.")

# sql = "INSERT INTO users (first_name, last_name, user_id) VALUES (%s, %s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4', 2),
#   ('Amy', 'Apple st 652', 3),
#   ('Hannah', 'Mountain 21', 4),
# ]

# cursor.executemany(sql, val)
# db.commit()

# print(cursor.rowcount, "записи были добавлены.")

####################################################################
# cursor.execute("CREATE TABLE categories (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), description VARCHAR(255))")
# sql = "INSERT INTO categories (title, description) VALUES (%s, %s)"
# val = [
#   ('Телефоны', 'Описание телефонов'),
#   ('Ноутбуки', 'Описание ноутбуков'),
#   ('Ноутбуки другие', 'Описание других ноутбуков'),
# ]

# cursor.executemany(sql, val)
# db.commit()


# SELECT
# cursor.execute("SELECT * FROM categories")
# categories = cursor.fetchall()

# for category in categories:
#     print(category[1])

# SELECT COLUMN
# cursor.execute("SELECT title FROM categories")
# categories = cursor.fetchall()

# for nameCategory in categories:
#     print(nameCategory)

# SELECT ONE RECORD
# cursor.execute("SELECT * FROM categories")
# category = cursor.fetchone()
# print(category)

user_data = {}

# FILTER
# cursor.execute("SELECT * FROM categories WHERE title = 'Ноутбуки'")
# categories = cursor.fetchall()

# for category in categories:
#     print(category)

# FILTER 2
# cursor.execute("SELECT * FROM categories WHERE title LIKE '%Ноутбуки%'")
# categories = cursor.fetchall()

# for category in categories:
#     print(category)

# FILTER 1 SQL защита
# sql = "SELECT * FROM categories WHERE title = %s"
# val = ("Ноутбуки", )

# cursor.execute(sql, val)
# categories = cursor.fetchall()

# for category in categories:
#     print(category)


# FILTER 2 SQL защита
# sql = "SELECT * FROM categories WHERE title LIKE %s"
# val = ("%Ноутбуки%", )

# cursor.execute(sql, val)
# categories = cursor.fetchall()

# for category in categories:
#     print(category)


# ORDER ASC
# cursor.execute("SELECT * FROM categories ORDER BY title")
# categories = cursor.fetchall()

# for category in categories:
#     print(category)

# ORDER DESC
# cursor.execute("SELECT * FROM categories ORDER BY title DESC")
# categories = cursor.fetchall()

# for category in categories:
#     print(category)

###############################################################

# DELETE RECORD
# cursor.execute("DELETE FROM categories WHERE title = 'Ноутбуки'")
# db.commit()
# print('Запись удалена!')

# DELETE ALL RECORDS
# cursor.execute("DELETE FROM categories")
# db.commit()
# print('Записи удалены!')

# DELETE RECORD защита SQL
# sql = "DELETE FROM categories WHERE title = %s"
# val = ("Ноутбуки", )
# cursor.execute(sql, val)

# db.commit()
# print('Запись удалена!')

# DROP TABLE
# cursor.execute("DROP TABLE categories")
# print('Таблица удалена!')

# DROP TABLE если существует
# cursor.execute("DROP TABLE IF EXISTS categories")
# print('Таблица удалена!')

# UPDATE RECORD
# cursor.execute("UPDATE users SET first_name = 'Андрей' \
#                 WHERE user_id = 2 ")
# db.commit()
# print('Запись обновлена!')

# UPDATE RECORD защита SQL
# sql = "UPDATE users SET first_name = %s \
#                 WHERE user_id = %s"
# val = ("Влад", 2)

# cursor.execute(sql, val)
# db.commit()
# print('Запись обновлена!')

# LIMIT
# cursor.execute("SELECT * FROM users LIMIT 2")
# users = cursor.fetchall()

# for user in users:
#     print(user)

# LIMIT OFFSET
# cursor.execute("SELECT * FROM users LIMIT 2 OFFSET 1")
# users = cursor.fetchall()

# for user in users:
#     print(user)

######### JOIN ############################
# cursor.execute("CREATE TABLE user_groups (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))")
# sql = "INSERT INTO user_groups (title) VALUES (%s)"
# val = [('Администратор', ), ('Модератор', ), ('Пользователь', )]

# cursor.executemany(sql, val)
# db.commit()

# cursor.execute("ALTER TABLE users ADD COLUMN (user_group_id INT)")


# sql = "SELECT \
#     users.first_name AS user, \
#     user_groups.title AS user_group \
#     FROM users \
#     JOIN user_groups ON users.user_group_id = user_groups.id"

# cursor.execute(sql)
# users = cursor.fetchall()

# for user in users:
#     print(user)

###### LEFT JOIN #############
# sql = "SELECT \
#     users.first_name AS user, \
#     user_groups.title AS user_group \
#     FROM users \
#     LEFT JOIN user_groups ON users.user_group_id = user_groups.id"

# cursor.execute(sql)
# users = cursor.fetchall()

# for user in users:
#     print(user)

##### RIGHT JOIN #############
# sql = "SELECT \
#     users.first_name AS user, \
#     user_groups.title AS user_group \
#     FROM users \
#     RIGHT JOIN user_groups ON users.user_group_id = user_groups.id"

# cursor.execute(sql)
# users = cursor.fetchall()

# for user in users:
#     print(user)



class User:
    def __init__(self, name):
        self.name = name
        self.locations = []

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        msg = bot.send_message(message.chat.id, "Здравствуйте, ведите своё имя на латинице.")
        bot.register_next_step_handler(msg, process_firstname_step)


def process_firstname_step(message):
    user_id = message.from_user.id
    user_data[user_id] = User(message.text)
    sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
    val = (user_id, message.text)
    cursor.execute(sql, val)
    db.commit()
    msg = bot.send_message(message.chat.id, message.text+", "+"приятно познакомиться! Теперь вы можете воспользоваться командами /add, /list, /reset.")


@bot.message_handler(commands=['add'])
def send_welcome(message):
        msg = bot.send_message(message.chat.id, "Пришлите мне геолокацию, которую Вы хотите сохранить.")
        bot.register_next_step_handler(msg, step)


def step(message):
    user_id = message.from_user.id


    sql = "INSERT INTO locations (id, location) \
                              VALUES (%s, %s)"
    val = (user_id, str(message.location.longitude)+" "+str(message.location.latitude))
    cursor.execute(sql, val)
    db.commit()

    bot.send_message(message.chat.id, "Местоположение успешно добавлено!")


@bot.message_handler(commands=['list'])
def process_lastname_step(message):
    user_id = message.from_user.id


    sql = "SELECT location from locations where id = %s"
    val = (user_id,)
    cursor.execute(sql, val)
    locations = cursor.fetchall()[:10]

    locations = [i[0] for i in locations]
    print(locations)
    db.commit()

    if locations:
        bot.send_message(message.chat.id, "Вот список Ваших сохраненных мест!")
        for location in locations:
            bot.send_location(message.chat.id, location.split()[1], location.split()[0])
    else:
        bot.send_message(message.chat.id, "Сохраненных мест нет!")


@bot.message_handler(commands=['reset'])
def process_lastname_step(message):
    user_id = message.from_user.id


    sql = "DELETE from locations where id = %s"
    val = (user_id,)
    cursor.execute(sql, val)


    bot.send_message(message.chat.id, "Сохраненные места удалены!!")

if __name__ == '__main__':
    bot.polling(none_stop=True)
