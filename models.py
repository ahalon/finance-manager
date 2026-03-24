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
            f"TOTAL VALUE: {self.total_value()}\n"
            f"BEST PERFORMER: {best.name if best else 'None'}\n"
        )
    
    def remove_by_ticker(self, ticker):
        self.__assets = [asset for asset in self.__assets if asset.ticker != ticker]

# MSCI_ACWI = ETF("MSCI ACWI", "ACWI", 100, 10)

# Adam_IKE = Portfolio("Adam IKE")

# Adam_IKE.add_asset(MSCI_ACWI)

# print(Adam_IKE.generate_report())