homework_time = int(input("How many minutes of homework do you have? "))

if homework_time > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

free_time = input("Is there free time after homework? (yes/no): ")

if free_time == "yes":
    print("Don't forget to pick a hobby!")

print("\n===== DAILY PLAN =====")
print(f"Homework time: {homework_time} minutes")
print(f"Your plan: {plan}")
print(f"Free time available: {free_time}")
