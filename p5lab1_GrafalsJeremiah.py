def laps_to_miles(user_laps):
    miles = user_laps * .25
    return miles

if __name__ == '__main__':
    laps = float(input())
    miles = laps_to_miles(laps)
    print(format(miles,'.2f'))