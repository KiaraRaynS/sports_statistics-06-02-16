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
    print(row)


def search_engine():
    while True:
        player_name = 'n'
        team = 't'
        mmr = 'm'
        question = input('''How would you like to search for the player?\n
    (n) - Username
    (t) - Current Team
    (m) - MMR''').lower()
        # Search by player name
        if question == player_name:
            search_username()
        # Search by team name
        elif question == team:
            search_team = input('Search by team name: ')
            team_match = []
            for row in table_list:
                if search_team in row:
                    team_match.append(row)
            print('{} matches found: '.format('NUMBER OF ITEMS IN LIST'))
        # Search by mmr
        elif question == mmr:
            pass
            # put function to search list by mmr here
        else:
            break


def search_username():
    while True:
        username_search = input('Search for player username: ').lower()
        username_match = []
        for row in table_list:
            if username_search in row:
                username_match.append(row)
        print('{} matches found.'.format('NUMBER OF ITEMS IN USERNAME_MATCH'))
        # UNCOMPLETE
        print(username_match)
        # if user enters e or hits esc they will return to menu
        break


def search_team():
    team_search = input('Search for team: ').lower()
    team_match = []
    for row in table_list:
        if team_search in row:
            team_match.append(row)
    print('{} matches found.'.format('NUMBER OF ITEMS IN LIST'))
    # UNCOMPLETE
    print(team_match)
