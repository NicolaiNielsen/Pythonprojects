def is_leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leapyear")
            else:
                print("not a leapyear")
        else: 
            print("leapyear")
    else:
        print("not leap year")

is_leapyear(2020)