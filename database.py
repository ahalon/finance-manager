import sqlite3
from models import ETF, Portfolio


def init_db():
    con = sqlite3.connect('finance_manager.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS etfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ticker TEXT NOT NULL,
            price REAL NOT NULL,
            quantity REAL NOT NULL
        )
    ''')
    con.commit()
    con.close()

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