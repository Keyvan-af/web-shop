class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price
        
def find_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]
    