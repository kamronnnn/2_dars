# 1 - masala

# import sqlite3
#
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         lastname TEXT,
#         age INTEGER,
#         address TEXT,
#         email TEXT,
#         phone TEXT
#     )
# ''')
# conn.commit()
#
# def add_user(name, lastname, age, address, email, phone):
#     cursor.execute('''
#         insert into users(name, lastname, age, address, email, phone)
#         values (?, ?, ?, ?, ?, ?)
#     ''', (name, lastname, age, address, email, phone))
#     conn.commit()
#
# def main():
#
#     while True:
#         name = input('Ismingizni kiriting: ')
#         lastname = input('Familiyangizni kiriting: ')
#         age = int(input('Yoshingizni kiriting: '))
#         address = input('Manzilingizni kiriting: ')
#         email = input('Email manzilingizni kiriting: ')
#         phone = input('Telefon raqamingizni kiriting: ')
#
#         add_user(name, lastname, age, address, email, phone)
#
#         yana_user_qoshish = input('Yana foydalanuvchi qoshmoqchimisiz? (ha/yoq): ')
#         if yana_user_qoshish.lower() != 'ha':
#             break
#
#     print("Barcha foydalanuvchilar: ")
#     cursor.execute('select * from users')
#     users = cursor.fetchall()
#     for user in users:
#         print(user)
#
#     conn.close()
#
#
# if __name__ == "__main__":
#     main()

#----------------------------------------

# 2 - masala


