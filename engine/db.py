import csv
import sqlite3

conn = sqlite3.connect("clara.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# > INSERTION OF APPS WITHIN THE LOCAL STORAGE MUST COMMENT THIS OR THE DATABASE WILL NOT FETCH
# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# > INSERTION OF WEBSITES WITHIN THE INTERNET MUST COMMENT THIS OR THE DATABASE WILL NOT FETCH
# query = "INSERT INTO web_command VALUES (null,'chat gpt', 'https://chat.openai.com/')"
# cursor.execute(query)
# conn.commit()

# > DELETE A ROW IN A SQLITE3 DATABASE
# cursor.execute("DELETE FROM web_command WHERE id = ")
# conn.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 32] # WHATEVER YOU GOT FROM THE EXCEL COMMAND =COLUMN(LASTCOLUMN+1) = MINUS THE RESULT TO 1

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()

# INSERTING A SINGLE ROW FOR A NEW CONTACT
# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890', 'null')"
# cursor.execute(query)
# conn.commit()

# query = 'kunal'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0]) # INDEX OUT OF RANGE
