field1 = 129
field2 = 18
field3 = 135
field4 = 73
field5 = 509




total = field1 + field2 + field3 + field4 + field5
average = total/5
print("Total harvested value       :-", total, "kg" )
print("average harvested value       :-", average,"kg")
price_per_kg = 15  
earning = total * price_per_kg
print("total earning", earning )

bags = total//25
leftover = total%25

print("full bags packed     :-", bags)
print("leftover grain       :-", leftover)

last_year = 500
print(total>last_year)
print(total==last_year)
print(total>=last_year)

total +=30
print(total)