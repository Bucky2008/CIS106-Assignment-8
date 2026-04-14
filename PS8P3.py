def compute_mpg(miles, gallons):
    mpg = miles / gallons
    return mpg


trip_count = 0
choice = "Yes"

while choice.lower() == "yes":

    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = compute_mpg(miles, gallons)

    print("City:", city)
    print("Miles:", miles)
    print("MPG:", round(mpg, 2))

    trip_count += 1

    choice = input("Do you want to enter another trip? (Yes/No): ")

print("Number of entries made:", trip_count)