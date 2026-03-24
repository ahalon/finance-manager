import sqlite3
from models import ETF, Portfolio


def init_db():
    with sqlite3.connect('finance_manager.db ') as con:
        con.execute('''
            CREATE TABLE IF NOT EXISTS etfs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ticker TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                quantity REAL NOT NULL
            )
        ''')
        con.commit()

def save_etf_to_db(etf):
    with sqlite3.connect('finance_manager.db') as con:
        con.execute('''
                    INSERT INTO etfs (name, ticker, price, quantity) 
                    VALUES (?, ?, ?, ?)
                    ''', (etf.name, etf.ticker, etf.price, etf.quantity))
        con.commit()
        print(f"Saved {etf.name} ({etf.ticker}) to database.")

def remove_etf_by_ticker_or_name(ticker=None, name=None):
    with sqlite3.connect('finance_manager.db') as con:
        cur = con.cursor()
        if ticker:
            con.execute('''
                        DELETE FROM etfs WHERE ticker = ? ''', (ticker.upper(),))
            print(f"Removed ETF with ticker {ticker} from database.")
        elif name:
            con.execute('''
                        DELETE FROM etfs WHERE LOWER(name) = LOWER(?) ''', (name,))
            print(f"Removed ETF with name {name} from database.")
        else:
            print("No ticker or name provided for deletion.")
            return
        if cur.rowcount > 0:
            print(f"Successfully deleted {cur.rowcount} record(s).")
        else:
            print("No matching ETF found in database.")

def clear_db():
    with sqlite3.connect('finance_manager.db') as con:
        con.execute('DELETE FROM etfs')
        print("Cleared all ETFs from database.")

def load_all_etfs():
    with sqlite3.connect('finance_manager.db') as con:
        cur = con.cursor()
        cur.execute('SELECT name, ticker, price, quantity FROM etfs')
        rows = cur.fetchall()
        etfs = [ETF(name=row[0], ticker=row[1], price=row[2], quantity=row[3]) for row in rows]
        return etfs
    
def update_etf_in_db(etf):
    with sqlite3.connect('finance_manager.db') as con:
        con.execute('''
                    UPDATE etfs 
                    SET name = ?, price = ?, quantity = ? 
                    WHERE ticker = ? 
                    ''', (etf.name, etf.price, etf.quantity, etf.ticker.upper()))
        con.commit()
        print(f"Updated {etf.name} ({etf.ticker}) in database.")


