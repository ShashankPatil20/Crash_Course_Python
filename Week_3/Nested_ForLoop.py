for left in range(7):
    for right in range(left, 7):
        print("[" +str(left) + "|" + str(right) + "]", end=" ")
    print()

teams =["RCB", "CSK", "MI", "KXIP"]
for home_team in teams:
    for away_team in teams:
        if home_team!=away_team:
            print(home_team + " vs " + away_team)