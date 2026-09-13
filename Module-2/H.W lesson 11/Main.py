TotalHomeworks = 4
originalcount = TotalHomeworks
print(f"You have {originalcount} homework assignments to complete today.")

complete_count = 0
homework_number = 1

while homework_number <= TotalHomeworks:
    # Match the homework title to the current number
    if homework_number == 1: 
        next_homework = "Math exercises"
    elif homework_number == 2: 
        next_homework = "Science reading"
    elif homework_number == 3: 
        next_homework = "History essay"
    else: 
        next_homework = "English vocabulary"

    # Ask the user for input and display the specific homework
    answer = input(f"Have you finished your {next_homework}? (yes/no): ").strip().lower()
    
    if answer == "yes":
        complete_count += 1
        homework_number += 1
        print("Great job! Homework completed.\n")
    else:
        print("Okay, work on it and check back when you are done!\n")

    # Display remaining homework left in the queue
    print("Homework assignments remaining:", TotalHomeworks - complete_count)
    print("-" * 30)

# Final summary text
print("\n=== Homework Checklist Summary ===")
print("Homework assigned today:", TotalHomeworks)
print("Homework completed:", complete_count)
print("Homework remaining:", TotalHomeworks - complete_count)
