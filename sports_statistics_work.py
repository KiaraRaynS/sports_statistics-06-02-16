import psycopg2

connection = psycopg2.connect('dbname=sports_statistics user=gingeredmink')
cursor = connection.cursor()
# cursor and connection opened

cursor.execute('DROP TABLE IF EXISTS players_table;')
generate_table = '''CREATE TABLE players_table (
name varchar (30),
team varchar (30),
position numeric(1),
mmr numeric (4),
main varchar (30),
winrate varchar (6)
);
'''
cursor.execute(generate_table)
# Team.Secret players
cursor.execute("INSERT INTO players_table VALUES ('Arteezy', 'Team Secret', 1, 8720, 'Shadow Fiend', '56.07%');")
cursor.execute("INSERT INTO players_table VALUES ('EternaLEnVy', 'Team Secret', 2, 7841, 'Storm Spirit', '56.41%');")
cursor.execute("INSERT INTO players_table VALUES ('UNiVeRsE', 'Team Secret', 3, 7775, 'Dark Seer', '69.70%');")
cursor.execute("INSERT INTO players_table VALUES ('Puppey', 'Team Secret', 4, 7000, 'Chen', '70.80%');")
cursor.execute("INSERT INTO players_table VALUES ('pieliedie', 'Team Secret', 5, 7757, 'Bounty Hunter', '64.52');")

# Natus Vincere

# Evil Geniuses
cursor.execute("INSERT INTO players_table VALUES ('Aui_2000', 'Evil Geniuses', 1, 7628, 'Morphling', '72.70%');")
cursor.execute("INSERT INTO players_table VALUES ('SumaiL', 'Evil Geniuses', 2, 7487, 'Storm Spirit', '52.71%');")
cursor.execute("INSERT INTO players_table VALUES ('BuLba', 'Evil Geniuses', 3, 7858, 'Clockwerk', '66.83%');")
cursor.execute("INSERT INTO players_table VALUES ('Fear', 'Evil Geniuses', 4, 6587, 'Enigma', '60.15%');")
cursor.execute("INSERT INTO players_table VALUES ('ppd', 'Evil Geniuses', 5, 7512, 'Treant Protector', '56.10%');")

connection.commit()
# close connection and cursor
cursor.close()
connection.close()
