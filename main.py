import sqlite3

def create_table():
    conn = sqlite3.connect("sqliteclass.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS contacts(
        first text,
        last text,
        number text

        )"""
        )

    conn.commit()
    conn.close()

def add_one(first, last, number):
    conn = sqlite3.connect("sqliteclass.db")
    c = conn.cursor()

    c.execute(f"SELECT * FROM contacts WHERE first = '{first}' AND last = '{last}' AND number='{number}'")
    result = c.fetchall()

    if len(result) == 0 and first != "" and last != "" and number !="":
        c.execute("INSERT INTO contacts VALUES (?, ?, ?)", (first, last, number))
    conn.commit()
    conn.close()


def show_all():
    conn = sqlite3.connect("sqliteclass.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM contacts")
    result = c.fetchall()

    return result





def delete(id):
    conn = sqlite3.connect("sqliteclass.db")
    c = conn.cursor()
    c.execute(f"DELETE FROM contacts WHERE rowid = '{id}'")
    conn.commit()
    conn.close()



def update(id, first, last, number):
    conn = sqlite3.connect("sqliteclass.db")
    c = conn.cursor()

    if first != "":
        c.execute(f"UPDATE contacts SET first='{first}' WHERE rowid = {id}")

    if last != "":
        c.execute(f"UPDATE contacts SET last='{last}' WHERE rowid = {id}")

    if number != "":
        c.execute(f"UPDATE contacts SET number='{number}' WHERE rowid = {id}")




    conn.commit()
    conn.close()




create_table()