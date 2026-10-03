def greet_customer():
    print("Welcome to the lemonade stand")
    print("Fresh lemonades just for you")

greet_customer()                          

price_per_cup = float(input("Enter the price per cup in dollars"))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price,cups):
    total = price * cups
    return total

total_price = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_price,2)
print("Total_cost: ", rounded_total)

print("Price per cup :", price_per_cup)
print("Cups Sold: ", cups_sold)
print("Total cost: ", rounded_total)