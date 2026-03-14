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

Adam = Portfolio("Adam")

etf1 = ETF("Vanguard S&P 500", "VOO", 400, 10)
etf2 = ETF("iShares Core MSCI EAFE", "IEFA", 70, 20)
etf3 = GlobalETF("iShares MSCI World", "IXJ", 100, 15, 50)
Adam.add_asset(etf1)
Adam.add_asset(etf2)
Adam.add_asset(etf3)
print(Adam.total_value())
print(30*"*")
print(f'{etf1} \n{etf2} \n{etf3}')
print(30*"+")
print(Adam.generate_report())