print("Smart-School Day Planner")
day = input("What day is it?").strip().capitalize()
weather = input("What is the weather?").strip().lower()
homework = input("Have you done the homework today?").strip().lower()
print(f"=== your plan for {day}===")

if day in ("Saturday", "Sunday"):
    print("Day type : Weekend - Go outside!")
elif day == "Monday":
    print("Day type : First day of the week - Pack your school bag")
elif day == "Friday":
    print("Day type : Last day of the week - Plan for your weekend")
elif day == ("Tuesday", "Wednesday", "Thursday"):
    print("Day type : Regular school days - Do your homework")
else:
    print("Day type : Day not recognized. chek the spelling!")

if weather == "sunny" and homework == "yes":
    print("After school - Head to the park")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip - Pack your umbrella - It might get wet outside")

if not (homework == "yes"):
    print("homework not done yet")

if weather == "rainy" and not ("homework == yes"):
    print("Best plan : Stay in, finish your homework, then watch Tv.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday","Sunday")):
    print("Best plan : All set for a great school day - you are prepared")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan : Perfect weekend weather - head outside and enjoy!")
else:
    print("Best plan : Take is one step at a time - you got this!")

print("Plan Complete! Have a great day!")


