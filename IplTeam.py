import random
number = int(input("Enter your  number of team : "))
teams = []
for i in range (number):
    d =input("Enter your team name : ")
    teams.append(d)
meeting = int(input("Enter your meeting : "))

for i in range  (number*meeting):
    team1 = random.choice(teams)
    team2 = random.choice(teams)
    while(team1 == team2):
        team2 = random.choice(teams)
    print(f"Match {i+1} : {team1} VS {team2}")