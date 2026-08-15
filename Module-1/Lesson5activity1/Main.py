temperature = int(input("Enter todays temperature"))
if temperature < 20:
    outfit = "jacket"
    print("its cold today")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("its warm today")
    print("Wear a", outfit)

is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over you", outfit)
else:
    needs_windbreaker = "No"
    print("It is calm today")
    print("No windbreaker needed over you", outfit)

    print("Weather check complete!")
    print("Tempereature:", temperature)
    print("Outfit chosen:", outfit)
    print("Raining:", is_raining)
    print("Windbreaker needed:", needs_windbreaker)
    

