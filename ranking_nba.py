

teams = ("Los Angeles Clippers,Dallas Mavericks,New York Knicks,Atlanta Hawks,Indiana Pacers,Memphis Grizzlies,"
         "Los Angeles Lakers,Minnesota Timberwolves,Phoenix Suns,Portland Trail Blazers,New Orleans Pelicans,"
         "Sacramento Kings,Los Angeles Clippers,Houston Rockets,Denver Nuggets,Cleveland Cavaliers,Milwaukee Bucks,"
         "Oklahoma City Thunder,San Antonio Spurs,Boston Celtics,Philadelphia 76ers,Brooklyn Nets,Chicago Bulls,"
         "Detroit Pistons,Utah Jazz,Miami Heat,Charlotte Hornets,Toronto Raptors,Orlando Magic,Washington Wizards,"
         "Golden State Warriors")

r = ("Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,"
     "Los Angeles Lakers 111 Minnesota Timberwolves 112,Phoenix Suns 95 Dallas Mavericks 111,Portland Trail Blazers 112 New Orleans Pelicans 94,"
     "Sacramento Kings 104 Los Angeles Clippers 111,Houston Rockets 85 Denver Nuggets 105,Memphis Grizzlies 76 Cleveland Cavaliers 106,"
     "Milwaukee Bucks 97 New York Knicks 122,Oklahoma City Thunder 112 San Antonio Spurs 106,Boston Celtics 112 Philadelphia 76ers 95,"
     "Brooklyn Nets 100 Chicago Bulls 115,Detroit Pistons 92 Utah Jazz 87,Miami Heat 104 Charlotte Hornets 94,"
     "Toronto Raptors 106 Indiana Pacers 99,Orlando Magic 87 Washington Wizards 88,Golden State Warriors 111 New Orleans Pelicans 95,"
     "Atlanta Hawks 94 Detroit Pistons 106,Chicago Bulls 97 Cleveland Cavaliers 95,"
     "San Antonio Spurs 111 Houston Rockets 86,Chicago Bulls 103 Dallas Mavericks 102,Minnesota Timberwolves 112 Milwaukee Bucks 108,"
     "New Orleans Pelicans 93 Miami Heat 90,Boston Celtics 81 Philadelphia 76ers 65,Detroit Pistons 115 Atlanta Hawks 87,"
     "Toronto Raptors 92 Washington Wizards 82,Orlando Magic 86 Memphis Grizzlies 76,Los Angeles Clippers 115 Portland Trail Blazers 109,"
     "Los Angeles Lakers 97 Golden State Warriors 136,Utah Jazz 98 Denver Nuggets 78,Boston Celtics 99 New York Knicks 85,"
     "Indiana Pacers 98 Charlotte Hornets 86,Dallas Mavericks 87 Phoenix Suns 99,Atlanta Hawks 81 Memphis Grizzlies 82,"
     "Miami Heat 110 Washington Wizards 105,Detroit Pistons 94 Charlotte Hornets 99,Orlando Magic 110 New Orleans Pelicans 107,"
     "Los Angeles Clippers 130 Golden State Warriors 95,Utah Jazz 102 Oklahoma City Thunder 113,San Antonio Spurs 84 Phoenix Suns 104,"
     "Chicago Bulls 103 Indiana Pacers 94,Milwaukee Bucks 106 Minnesota Timberwolves 88,Los Angeles Lakers 104 Portland Trail Blazers 102,"
     "Houston Rockets 120 New Orleans Pelicans 100,Boston Celtics 111 Brooklyn Nets 105,Charlotte Hornets 94 Chicago Bulls 86,"
     "Cleveland Cavaliers 103 Dallas Mavericks 97")

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

import itertools

teams = teams.split(",")

dict_teams_points = dict(zip(teams, itertools.repeat(0)))
dict_teams_loss = dict(zip(teams, itertools.repeat(0)))
dict_teams_wins = dict(zip(teams, itertools.repeat(0)))
dict_teams_total_points = dict(zip(teams, itertools.repeat(0)))
dict_teams_total_points_conceded = dict(zip(teams, itertools.repeat(0)))

lst1 = r.split(",")

new_list = []

for x in lst1:
    x = x.split()
    new_list.append(x)


num = []
team = []
for i in new_list:
    n_lst = []
    for u in i:
        if RepresentsInt(u) == False:
            n_lst.append(u)




        elif RepresentsInt(u) == True:
            num.append(u)

            team.append(" ".join(n_lst))
            del n_lst[:]


num2 = []
team_win = []
team_tie = []
team_loss = []
for number in num:
    num2.append(int(number))


for item in range(0, len(num), 2):
    if num2[item] > num2[item+1]:
        team_win.append(team[item])
        team_loss.append(team[item+1])

    elif num2[item] < num2[item+1]:
        team_win.append(team[item+1])
        team_loss.append(team[item])

    elif num2[item] == num2[item+1]:
        team_tie.append(team[item])
        team_tie.append(team[item+1])

    dict_teams_total_points[team[item]] += num2[item]
    dict_teams_total_points[team[item+1]] += num2[item+1]
    dict_teams_total_points_conceded[team[item]] -= num2[item+1]
    dict_teams_total_points_conceded[team[item+1]] -= num2[item]



for tn in team_win:
    dict_teams_points[tn] += 3
    dict_teams_wins[tn] +=1

for tm in team_tie:
    dict_teams_points[tm] += 1

for tl in team_loss:
    dict_teams_loss[tl] += 1

for nba_team in teams:
    print (nba_team  + "- Wins: %d, Losses: %d, Points: %d, Points scored: %d, Points conceded: %d" %  (dict_teams_wins[nba_team], dict_teams_loss[nba_team], dict_teams_points[nba_team], dict_teams_total_points[nba_team], dict_teams_total_points_conceded[nba_team]))
