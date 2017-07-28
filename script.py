import sqlite3

def create_table():
    connection = sqlite3.connect("lib.db")
    curs = connection.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, \
    quantity INTEGER, price REAL)")

    connection.commit() #committing the changes
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("lib.db")
    curs = connection.cursor()

    #curs.execute("INSERT INTO store VALUES(item, quality, price)")
    #this line is sufficient but very bad online, as it's exposed to sql injection
    curs.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))

    connection.commit()
    connection.close()


def get():
    connection = sqlite3.connect("lib.db")
    curs = connection.cursor()

    #curs.execute("INSERT INTO store VALUES(item, quality, price)")
    #this line is sufficient but very bad online, as it's exposed to sql injection
    curs.execute("SELECT * FROM store")
    rows=curs.fetchall() #fetch all for rows

    connection.close()
    return rows


def delete(item):
    connection = sqlite3.connect("lib.db")
    curs = connection.cursor()

    #curs.execute("INSERT INTO store VALUES(item, quality, price)")
    #this line is sufficient but very bad online, as it's exposed to sql injection
    curs.execute("DELETE FROM store WHERE item = ?", (item,)) #the item, is important

    connection.commit()
    connection.close()



create_table()
insert("Water Glass", 10, 5)
insert("Coffee Mug", 15, 10)
print(get())
delete("Water Glass")
print(get())
