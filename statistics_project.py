# TO BEGIN THE TABLE
# createdb 'name_of_database'
# psql -d table_name
# carry out the steps to create a table.
# ###########
# Begin project
# step 1 - Connecting to the database
# step 2 - Create cursor to database [the cursor is what executes commands given within the database]
# step 3 - Pull results from command into a tuple using Cursor
# step 4 - Close the curser and connection

import psycopg2

connection = psycopg2.connect('dbname=test_table user=Gingeredmink')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS person_data;')

create_table_command = '''CREATE TABLE person_data (
  full_name varchar(30),
    best_friend varchar(30),
      age numeric(3),
        birth_year numeric(4)
        );
'''
cursor.execute(create_table_command)
cursor.execute("INSERT INTO person_data VALUES ('full name', 'best friend', 20, 1997);")

name = 'User Name'
best_friend = 'Delok'
age = 14
year = 1996

# cursor.execute('Insert INTO person_data VALUES('{}', '{}',' {}', '{}').format(variables)')
# DO NOT DO THIS, this will result in an instant unsatisfactory mark on the assidnment.
cursor.execute('INSERT ONTO person_data VALUES(%s, %s, %s, %s);'), (name, best_friend, age, year)
connection.commit()

# cursor.execute('select * from person_data;')
# issues a command form python for the cursor to go and interact with the database which is operating elsewhere

# results = cursor.fetchall()
# for row in results:
#    print(row)
# [row for row in results]

cursor.close()
connection.close()

