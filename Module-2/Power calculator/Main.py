print("=== Power Calculator ===")

base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))

abs_exponent = abs(exponent)
result = 1

for i in range(1, abs_exponent + 1):
    result = result * base
    print("Step", i, ": running total =", result)

if exponent < 0:
    if base == 0:
        final_answer = "Undefined"
    else:
        final_answer = 1 / result
else:
    final_answer = result

print("\nAnswer:", base, "to the power", exponent, "=", final_answer)
print ("Check the answer by yourself, and improve your calculatuons") 
