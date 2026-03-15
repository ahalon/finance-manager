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
    
    def remove_by_ticker(self, ticker):
        self.__assets = [asset for asset in self.__assets if asset.ticker != ticker]

class GlobalETF(ETF):
    def __init__(self, name, ticker, price, quantity, countries_count):
        super().__init__(name, ticker, price, quantity)
        self.countries_count = countries_count

    def __str__(self):
        return f"{super().__str__()} [Global Exposure: {self.countries_count} countries]"



### --- BAZA DANYCH ---
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

def delete_etf_by_ticker(ticker):
    conn = sqlite3.connect('moje_inwestycje.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM etfs WHERE ticker = ?', (ticker,))
    conn.commit()
    conn.close()

# --- TEST ---
# init_db() # Najpierw tworzymy tabelę

# clear_db()

# # Tworzysz obiekt swojej klasy
# acwi = ETF("iShares ACWI", "SSAC", 350.5, 12)
# sp500 = ETF("Vanguard S&P 500", "VOO", 400, 10)



# # Zapisujesz go do bazy
# save_etf_to_db(acwi)
# save_etf_to_db(sp500)


# lista_z_bazy = load_all_etfs()
# moje_portfolio = Portfolio("Adam")
# for etf in lista_z_bazy:
#     moje_portfolio.add_asset(etf)

# print(str(moje_portfolio.generate_report()))
def get_numeric_input(prompt, float_type = True):
            while True:
                try:
                    return float(input(prompt)) if float_type else int(input(prompt))
                except ValueError:
                    print(f"Invalid input. Please enter a valid number.")

def main_menu():
    init_db()  # Upewniamy się, że tabela istnieje
    portfolio = Portfolio("Adam")
    
    # Ładujemy dane z bazy na starcie programu
    assets = load_all_etfs()
    for asset in assets:
        portfolio.add_asset(asset)



    while True:
        print("\n--- MANAGER ETF ACWI & OTHERS ---")
        print("1. Add new ETF to portfolio") # Dodajemy nowy ETF do portfela (i bazy)
        print("2. Show wallet report")
        print("3. Clear wallet (and database)")
        print("4. Delete ETF by ticker")
        print("0. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("ETF Name: ")
            ticker = input("Ticker: ")
            price = get_numeric_input("Price: ")
            qty = get_numeric_input("Quantity: ", float_type=False)
           

            new_etf = ETF(name, ticker, price, qty)
            save_etf_to_db(new_etf)
            portfolio.add_asset(new_etf) # Dodajemy też do obiektu w RAMie
            
        elif choice == "2":
            print(portfolio.generate_report())
            
        elif choice == "3":
            clear_db()
            portfolio = Portfolio("Adam") # Resetujemy też obiekt w pamięci
            print("Wallet cleared.")

        elif choice == "4":
            ticker = input("Enter ETF ticker to delete: ").upper()
            delete_etf_by_ticker(ticker)
            portfolio.remove_by_ticker(ticker) # Usuwamy też z obiektu w RAM
            print(f"ETF {ticker} has been deleted.")
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Odpalenie menu
if __name__ == "__main__":
    main_menu()


