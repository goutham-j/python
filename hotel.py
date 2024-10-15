import sqlite3

try:
    # create connection by using object
    connection = sqlite3.connect('hotel_data.db')
 
    # query to create a table named FOOD1
    connection.execute('''CREATE TABLE IF NOT EXISTS hotel
        (FID    INT   NOT NULL,
        FNAME   TEXT  NOT NULL,
        COST    INT   NOT NULL,
        WEIGHT  INT);
        ''')
 
    # insert query to insert food  details in 
    # the above table
    connection.execute("INSERT INTO hotel VALUES (1, 'cakes',   800,    10 )")
    connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,    20 )")
    connection.execute("INSERT INTO hotel VALUES (3, 'chocos',  1000,   30 )")
 
    # create a cousor object for select query
    cursor = connection.execute("SELECT * from hotel")
 
    # display all data from hotel table
    for row in cursor:
        print(row)
 
    # Close the cursor
    cursor.close()
 
# Handle errors
except sqlite3.Error as error:
    print('DB Error: ', error)
 
# Close DB Connection
finally:
    if connection:
        connection.close()
