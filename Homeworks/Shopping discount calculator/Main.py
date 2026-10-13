valid = False

while not valid:
    try:
        bill = float(input("Enter the total bill amount: $"))
        discount_percent = float(input("Enter the discount percentage (e.g., 15 for 15%): "))
        people = int(input("Enter the number of people splitting the bill: "))
        
        discount_amount = bill * (discount_percent / 100)
        final_bill = bill - discount_amount
        per_person = final_bill / people

    except ValueError:
        print("❌ Error: Invalid input! Please type numbers only (and whole numbers for people).\n")
        
    except ZeroDivisionError:
        print("❌ Error: The number of people splitting the bill cannot be 0.\n")

    else:
        print("\n--- Final Calculation ---")
        print(f"Original Bill:  ${bill:.2f}")
        print(f"Discount saved: ${discount_amount:.2f}")
        print(f"Final Bill:     ${final_bill:.2f}")
        print(f"Each Person Pays: ${per_person:.2f}")
        
        valid = True
        
    finally:
        print("💡 Attempt finished.")
