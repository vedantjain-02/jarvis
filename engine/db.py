import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'urban vpn','C:\\Program Files (x86)\\UrbanVPN\\bin\\urban-vpn-app.exe')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100),url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'Canva','https://www.canva.com')"
# cursor.execute(query)
# con.commit()

# app_name = "urban vpn"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)',(app_name,))
# results = cursor.fetchall()
# print(results)

"""   REATING TABLE OF CONTACTS   """
# Create a table with the desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')



"""   FOR ADDING CONTACTS IN DATABASE   """

    # # Specify the column indices you want to import (0-based index)
    # # Example: Importing the 1st and 3rd columns
    # desired_columns_indices = [0, 20]

    # # Read data from CSV and insert into SQLite table for the desired columns
    # with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    #     csvreader = csv.reader(csvfile)
    #     for row in csvreader:
    #         selected_data = [row[i] for i in desired_columns_indices]
    #         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

    # # Commit changes and close connection
    # con.commit()
    # con.close()


"""   INSERTING A SINGLE CONTACT IN DATABASE   """

    # query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890')"
    # cursor.execute(query)
    # con.commit()


"""   SEARCH CONTACTS IN DATABASE   """

    # query = 'Aaryan BCA'
    # query = query.strip().lower()

    # cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
    # results = cursor.fetchall()
    # print(results[0][0])