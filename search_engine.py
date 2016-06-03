import psycopg2
connection = psycopg2.connect('dbname=sports_statistics user=gingeredmink')
cursor = connection.cursor()
cursor.execute('select * from players_table;')
table = cursor.fetchall()
connection.commit()

cursor.close()
connection.close()
table_list = list(table)
for row in table_list:
    pass


def search_username():
    while True:
        username_search = input('Search for player username: ')
        username_match = []
        for row in table_list:
            if username_search in row:
                username_match.append(row)

        if len(username_match) < 1:
            print('No matches found')
        else:
            print('{} matche(s) found.'.format(len(username_match)))
            print('Username, Current Team, Position, MMR, Main Hero, Pub Winrate')
            print(username_match)
        exit = input('Enter "e" to return to search menu ').lower
        if exit == 'e'.lower:
            break


def search_team():
    while True:
        team_search = input('Search for team: ')
        team_match = []
        for row in table_list:
            if team_search in row:
                team_match.append(row)
        # print('{} matches found.'.format('NUMBER OF ITEMS IN LIST'))
        # UNCOMPLETE
        for row in team_match:
            print(row)
        break


def search_engine():
    while True:
        player_name = 'u'
        team = 't'
        mmr = 'm'
        question = input('''How would you like to search for the player?\n
    (u) - Username
    (t) - Current Team
    (m) - MMR
    (e) - exit
    ''').lower()
        # Search by player name
        if question == player_name:
            search_username()
            # search_username()
        # Search by team name
        elif question == team:
            search_team()
            # Search by mmr
        elif question == mmr:
            print('Search by mmr')
            # put function to search list by mmr here
        else:
            break

search_engine()
