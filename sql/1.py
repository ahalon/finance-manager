import sqlite3

# 1. Łączymy się (jeśli pliku nie ma, Python go stworzy)
conn = sqlite3.connect('moje_inwestycje.db')
cursor = conn.cursor()

# 2. Wykonujemy polecenie SQL
cursor.execute('''
CREATE TABLE IF NOT EXISTS etfs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ticker TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')

# 3. Zamykamy połączenie
conn.close()
print("Tabela gotowa. Baza 'moje_inwestycje.db' czeka na dane.")