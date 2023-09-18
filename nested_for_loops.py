# for left in range(7):
#     for right in range(left,7):
#         print("[" +str(left) + "|" + str(right) + "]", end = " ")
#     print()

#teams playing against each other PnC
teams = [' Dragons ', ' Wolves  ', ' Pandas  ', ' Unicorns']
for home_teams in teams:
    for away_teams in teams:
        if home_teams!= away_teams:
            print(home_teams + " vs " + away_teams)