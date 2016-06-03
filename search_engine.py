# open the database as a list that can be read


def search_engine():
    while True:
        player_name = 'n'
        team = 't'
        mmr = 'm'
        question = input('''How would you like to search for the player?\n
    (n) - Username
    (t) - Current Team
    (m) - MMR''').lower()
        if question == player_name:
            pass
            # put function to search list by player name here
        elif question == team:
            pass
            # put function to search list by current team here
        elif question == mmr:
            pass
            # put function to search list by mmr here
        else:
            break


def search_username():
    search = input('Search for player username: ').lower
    # while true
    # go over the list to check if input == any names within database
    # print row with matching username
    # if none found, print nothing found
    # hit enter to return to search menu


def search_team():
    results_list = []
    # compare list row to

