Totalchores = 4
originalcount = Totalchores
print(f"you have {originalcount} chores to complete today")

complete_count = 0
chore_number = 1

while chore_number <= Totalchores:
    if chore_number == 1: next_chore = "Make your bed"
    elif chore_number == 2: next_chore = "Feed your pet"
    elif chore_number == 3: next_chore = "Water the plants"
    else: next_chore = "Clean your room"

    answer = ("Have your finished your chores? : (yes/no)")
    if answer == "yes":
        complete_count = +1
        chore_number = +1
        print("Great job! Chore completed")

    else:
        print("Okay, finish it and check again")

    print("Chores completed", Totalchores - complete_count)

print("Chore checklist summary")
print("Chores assigned today", Totalchores)
print("Chores completed", complete_count )
print("Chores remaining", Totalchores - complete_count)

