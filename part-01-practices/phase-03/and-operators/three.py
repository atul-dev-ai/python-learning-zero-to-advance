is_weather = False
is_weekend = True
if is_weather and is_weekend:
    print("You can go outside and enjoy the weather.")
elif is_weather and not is_weekend:
    print("You can go outside but you have to work.")
elif not is_weather and is_weekend:
    print("You can't go outside but you can relax at home.")
elif not is_weather and not is_weekend:
    print("You can't go outside and you have to work.")
else:
    print("Invalid input.")