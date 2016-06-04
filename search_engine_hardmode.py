import psycopg2
connection = psycopg2.connect('dbname=sports_statistics user=gingeredmink')
cursor = connection.cursor()
cursor.execute('select * from players_table;')
table = cursor.fetchall()
connection.commit()

cursor.close()
connection.close()
table_list = list(table)
table_no_decimal = []

# Check input for letters


def int_check(string_to_check):
    try:
        int(string_to_check)
        return True
    except ValueError:
        return False


#  Search functions
# __________________________________________________________________


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
        if len(team_match) < 1:
            print('No matches found.')
        else:
            print('{} matches found.'.format(len(team_match)))
            print('Username, Current Team, Position, MMR, Main Hero, Pub Winrate')
            for row in team_match:
                print(row)
        break_loop = input('Enter "e" to return to search menu.\n').lower()
        if break_loop == 'e':
            break


def search_mmr():
    while True:
        mmr_search = input('Search for MMR: ')
        mmr_match = []
        for row in table_list:
            print(row)
            print(mmr_search)
            if mmr_search in str(row[3]):
                mmr_match.append(row)
        if len(mmr_match) < 1:
            print('No matches found.')
        else:
            print('{} matches found.'.format(len(mmr_match)))
            for row in mmr_match:
                print(row)
        exit_results = input('Enter "e" to return to search menu.\n').lower()
        if exit_results == 'e':
            break


# Insert new player into database
# ____________________________________________


def insert_new_player():
    while True:
        print('Enter "e" to exit.')
        n = input('Username: ')
        team = input('Team Name: ')
        spot = input('Position(1-5): ')
        mmr = input('MMR(four numbers): ')
        main = input('Main Hero: ')
        pub = input('Pub Winrate: ')
        verify_information = input('''{}, {}, {}, {}, {}, {}.
                Does this appear correct? Y/N\n'''.format(n, team, spot, mmr, main, pub))
        if verify_information == 'y':
            connection = psycopg2.connect('dbname=sports_statistics user=gingeredmink')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO players_table VALUES (%s, %s, %s, %s, %s, %s);", (n, team, spot, mmr, main, pub))
            connection.commit()
            cursor.close()
            connection.close()
            print("User added.")
        elif verify_information == 'n':
            continue
        break


# Update functions
# _______________________________________________________


def update_user():
    while True:
        print('Enter "e" to exit.')
        user_search = input("""Who's information would you like to change?
               Enter username:   """)
        match_found = []
        if user_search == 'e':
            break
        for row in table_list:
            if user_search in row:
                match_found.append(row)
        if len(match_found) < 1:
            print('User not found.')
        else:
            print('User found:')
            print(match_found)
            information_to_update = input("""What would you like to update?
                    (t) - Current Team
                    (p) - Position
                    (m) - MMR
                    (h) - Main Hero
                    (w) - Pub Winrate\n""").lower()
            if information_to_update == 't':
                new_team = input('Enter new team: ')
                if len(new_team) > 30:
                    new_team = input('Enter new team: ')
                connection = psycopg2.connect('dbname=sports_statistics user=gingeredmink')
                cursor = connection.cursor()
                # Error for collumn being returned here
                cursor.execute("UPDATE players_table SET team = 'new_team' WHERE name = 'user_search'")
                connection.commit()
                cursor.close()
                connection.close
                print('User information updated.')
            if information_to_update == 'p':
                new_position = input('Enter new position: ')
                possible_numbers = [1, 2, 3, 4, 5]
                value_check = int_check(new_position)
                if value_check:
                    new_position = int(new_position)
                    while new_position not in possible_numbers:
                        new_position = input('Enter new position: ')
                        int_or_not = int_check(new_position)
                        if int_or_not:
                            new_position = int(new_position)
                else:
                    print('Please enter a numeric value.')
            if information_to_update == 'm':
                new_mmr = input('Enter new MMR: ')
                while len(new_mmr) > 4:
                    new_mmr = input('Enter new MMR: ')
                new_mmr = int(new_mmr)
            if information_to_update == 'h':
                new_hero = input('Enter new main hero: ')
            if information_to_update == 'w':
                new_winrate = input('Enter new winrate: ')


# Main game function
# ___________________________________________________________________


def search_engine():
    while True:
        search = 's'
        input_new_user = 'i'
        update_user_information = 'u'
        operation = input('''What would you like to do?
                (s) - Search for player
                (i) - Input new Player
                (u) - Update player information
                (e) - Exit\n''').lower()
        if operation == search:
            while True:
                player_name = 'u'
                team = 't'
                mmr = 'm'
                print('Players with no given MMR have 0 as MMR.')
                question = input('''How would you like to search for the player?\n
            (u) - Username
            (t) - Current Team
            (m) - MMR
            (e) - exit\n''').lower()
                if question == player_name:
                    search_username()
                elif question == team:
                    search_team()
                elif question == mmr:
                    search_mmr()
                else:
                    break
        if operation == input_new_user:
            insert_new_player()
        if operation == update_user_information:
            update_user()
        if operation == 'e':
            break


search_engine()
'''
def sort_by_mmr():
    connection = psycopg2.connect('dbname=sports_statistics user=gingeredmink')
    cursor = connection.cursor()
    cursor.execute('SELECT * from players_table;')
    cursor.execute('ORDER BY mmr DESC;')
    new_table = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
'''
