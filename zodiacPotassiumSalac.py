def zodiacYear(birthYear):
    if birthYear < 1900:
        print("Invalid year. Birth year must not be earlier than year 1900.")
        return

    remainder = (birthYear - 1900) % 12

    if remainder == 0:
        zodiac = "Rat"
    elif remainder == 1:
        zodiac = "Ox"
    elif remainder == 2:
            zodiac = "Tiger"
    elif remainder == 3:
            zodiac = "Rabbit"
    elif remainder == 4:
            zodiac = "Dragon"
    elif remainder == 5:
            zodiac = "Snake"
    elif remainder == 6:
            zodiac = "Horse"
    elif remainder == 7:
            zodiac = "Goat"
    elif remainder == 8:
            zodiac = "Monkey"
    elif remainder == 9:
            zodiac = "Rooster"
    elif remainder == 10:
            zodiac = "Dog"
    else:
           zodiac == "Pig"

    print("Your Chinese Zodiac Sign is: ",zodiac)

birth_year = int(input("Enter your birth year: "))
zodiacYear(birth_year)