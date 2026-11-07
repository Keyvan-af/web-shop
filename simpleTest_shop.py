from shop import Product, find_by_name, total

products = [
    Product("A1", "Mouse", 1000),
    Product("B2", "Keyboard", 2500)
]

print([p.sku for p in find_by_name(products, "Mouse")])
print([p.sku for p in find_by_name(products, "Keyboard")])
print([p.sku for p in find_by_name(products, "Monitor")])

# ---------------- total() tests ----------------
print(total([1000, 2500]))          # 3500
print(total([]))                    # 0
print(total([42]))                  # 42
print(total([1.5, 2.5, 3.0]))       # 7.0
print(total(p.price for p in products))   # 3500 (works with generators too)