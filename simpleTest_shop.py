from shop import Product, find_by_name

products = [
    Product("A1", "Mouse", 1000),
    Product("B2", "Keyboard", 2500)
]

print([p.sku for p in find_by_name(products, "Mouse")])
print([p.sku for p in find_by_name(products, "Keyboard")])
print([p.sku for p in find_by_name(products, "Monitor")])