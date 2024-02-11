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
# query = "INSERT INTO web_command VALUES (null,'messenger', 'https://www.messenger.com/')"
# cursor.execute(query)
# conn.commit()


