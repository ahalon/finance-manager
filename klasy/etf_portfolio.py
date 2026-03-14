import sqlite3

class ETF:
    def __init__(self, name, ticker, price, quantity):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print(f"ERROR: {value} is not a correct price.")
    
    def __str__(self):
        return f'ETF {self.name} ({self.ticker}) - Price: {self.price}, Quantity: {self.quantity}'
    
class Portfolio:
    def __init__(self, owner):
        self.__assets = []
        self.owner = owner

    def add_asset(self, asset):
        self.__assets.append(asset)

    def total_value(self):
        return sum(etf.price * etf.quantity for etf in self.__assets)
    
    def get_best_asset(self):
        if not self.__assets:
            return None
        return max(self.__assets, key=lambda asset: asset.price * asset.quantity)
    
    def generate_report(self):
        assets_details = "\n".join([f"- {str(asset)}" for asset in self.__assets])
        best = self.get_best_asset()
        
        return (
            f"--- PORTFOLIO REPORT: {self.owner} ---\n"
            f"{assets_details}\n"
            f"----------------------------------------\n"
            f"TOTAL VALUE: {self.total_value()} PLN\n"
            f"BEST PERFORMER: {best.name if best else 'None'}\n"
        )
    

class GlobalETF(ETF):
    def __init__(self, name, ticker, price, quantity, countries_count):
        super().__init__(name, ticker, price, quantity)
        self.countries_count = countries_count

    def __str__(self):
        return f"{super().__str__()} [Global Exposure: {self.countries_count} countries]"

#TEST

# Adam = Portfolio("Adam")

# etf1 = ETF("Vanguard S&P 500", "VOO", 400, 10)
# etf2 = ETF("iShares Core MSCI EAFE", "IEFA", 70, 20)
# etf3 = GlobalETF("iShares MSCI World", "IXJ", 100, 15, 50)
# Adam.add_asset(etf1)
# Adam.add_asset(etf2)
# Adam.add_asset(etf3)
# print(Adam.total_value())
# print(30*"*")
# print(f'{etf1} \n{etf2} \n{etf3}')
# print(30*"+")
# print(Adam.generate_report())


# 1. Połączenie i stworzenie tabeli (jeśli jej nie ma)
def init_db():
    conn = sqlite3.connect('moje_inwestycje.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS etfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ticker TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# 2. Funkcja, która zapisuje obiekt klasy ETF do bazy
def save_etf_to_db(etf_obj):
    conn = sqlite3.connect('moje_inwestycje.db')
    cursor = conn.cursor()
    
    # Używamy ? jako bezpiecznych placeholderów
    cursor.execute('''
        INSERT INTO etfs (name, ticker, price, quantity) 
        VALUES (?, ?, ?, ?)
    ''', (etf_obj.name, etf_obj.ticker, etf_obj.price, etf_obj.quantity))
    
    conn.commit()
    conn.close()
    print(f"Pomyślnie zapisano {etf_obj.name} ({etf_obj.ticker}) do bazy danych!")

def clear_db():
    conn = sqlite3.connect('moje_inwestycje.db')
    cursor = conn.cursor()
    
    # Usuwamy wszystkie wiersze z tabeli
    cursor.execute('DELETE FROM etfs')
    
    conn.commit()
    conn.close()
    print("Baza wyczyszczona. Możesz testować od nowa.")

def load_all_etfs():
    conn = sqlite3.connect('moje_inwestycje.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, ticker, price, quantity FROM etfs')
    rows = cursor.fetchall()
    
    etfs = []
    for row in rows:
        nowy_etf = ETF(name=row[0], ticker=row[1], price=row[2], quantity=row[3])
        etfs.append(nowy_etf)
        
    conn.close()
    return etfs

# --- TEST ---
init_db() # Najpierw tworzymy tabelę

clear_db()

# Tworzysz obiekt swojej klasy
acwi = ETF("iShares ACWI", "SSAC", 350.5, 12)
sp500 = ETF("Vanguard S&P 500", "VOO", 400, 10)



# Zapisujesz go do bazy
save_etf_to_db(acwi)
save_etf_to_db(sp500)


lista_z_bazy = load_all_etfs()
moje_portfolio = Portfolio("Adam")
for etf in lista_z_bazy:
    moje_portfolio.add_asset(etf)

print(str(moje_portfolio.generate_report()))