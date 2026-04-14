def batting_average(hits, at_bats):
    return hits / at_bats


count = 0
choice = input("Do you want to enter a player? (Yes/No): ")

while choice.lower() == "yes":
    
    last_name = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    avg = batting_average(hits, at_bats)

    print("Player:", last_name)
    print("Batting Average:", round(avg, 3))

    count += 1

    choice = input("Do you want to enter another player? (Yes/No): ")

print("Number of players entered:", count)