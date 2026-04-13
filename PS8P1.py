def compute_total(qty, price):
    total = qty * price
    
    if total > 10000:
        total = total * 0.90   # apply 10% discount
    
    return total


extended_price = 0

while True:
    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    total = compute_total(qty, price)
    
    print("Quantity:", qty)
    print("Price:", price)
    print("Total:", total)
    
    extended_price += total
    
    answer = input("Do you want to enter another item? (Yes/No): ")
    
    if answer.lower() != "yes":
        break

print("Extended price:", extended_price)