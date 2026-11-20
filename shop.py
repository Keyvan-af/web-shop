class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price
        
    def find_by_name(products, text):
        return [p for p in products if text.lower() in p.name.lower()]
        
    def total(prices):
        """Return the sum of a sequence of prices (0 for an empty sequence)."""
        return sum(prices)

    def apply_discount(price, percent):
        return price * (100 - percent) / 100 

    def add_tax(price, rate=0.15):
        return price * (1 + rate)  # feature: add tax to price, default rate is 20%

    def search_by_name(products, text):
        return [p for p in products if text.lower() in p.name.lower()]

def add_tax(price, rate=0.25):
    return price * (1 + rate)

def apply_coupon(price):
    return price - 5 
p1 = Product(sku="2", name="apple", price="3000")
print(p1.price)

def sort_by_price(products):
    return sorted(products, key=lambda p: p.price)

def in_stock(stock, sku):
    return stock.get(sku, 0) > 0
