
import sqlite3

# Устанавливаем соединение с базой данных (если ее нет, то она будет создана)
conn = sqlite3.connect('example.db')

# Создаем курсор для работы с базой данных
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Вставляем данные
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 25))

cursor.execute('''
    INSERT INTO users (name, age) VALUES (:name, :age)
''', {'name': 'Bob', 'age': 30})

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()