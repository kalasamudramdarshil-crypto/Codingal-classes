name = input("Enter member name: ")
club = input("Enter club name: ")

member_number = 8
points = 9.5
is_active = True

print(member_number, type(member_number))
print(points, type(points))
print(is_active, type(is_active))

badge_code = name[:3] + club[-1] + str(member_number)
print(badge_code)

print("===== CLUB BADGE =====")
print("Member: " + name)
print("Club: " + club)
print("Code: " + badge_code)
print("Points | Active: " + str(points) + " | " + str(is_active))
