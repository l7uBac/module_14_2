import sqlite3

connect = sqlite3.connect("not_telegram.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

# for i in range(10):
#     if i % 2 != 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", ("500", f"{i}"))

# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))

# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# cursor.execute('DELETE FROM Users WHERE id=?', (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
print(f'Общее количество записей - {total1}')

cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(f'Общий баланс - {total2}')
print(f'Средний баланс - {total2 / total1}')

cursor.execute("SELECT AVG(balance) FROM Users")
total3 = cursor.fetchone()[0]
print(total3)

connect.commit()
connect.close()
