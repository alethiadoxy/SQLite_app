# Originallt a set of subroutines that I realised were becoming ubiquitous to the exploring_sqlite project
# moved here and with additions for better functionality
import sqlite3


def printa():
    print('aaaaaaaaaaaaaaaaaa')

def pretty_print(items):
    bar= "-----" + "\t-------" + "\t\t\t-------"
    print(bar)
    print("Rowid"+ "\tNAME " + "\t\t\tEMAIL")
    print(bar)
    for item in items:
        print(str(item[0]) + "\t\t" + item[1] + " " + item[2] + "\t\t" + item[3])
    print(bar)

def show_all(c):
    #quite often we want to retrieve and view the
    # whole db that the cursor c is within. This does that.
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    pretty_print(items)

def execute_n_print(c,command):
    #prints and executes command before retrieving the resultant db
    # and doing a pretty print of it
    print(command)
    c.execute(command)
    items = c.fetchall()
    pretty_print(items)

def create_cursor_n_show_all():
    #connect to db
    conn = sqlite3.connect('customer.db')
    #create cursor
    c = conn.cursor()

    #print out everything
    show_all(c)

    #commit and close
    conn.commit()
    conn.close()

def add_entry(first,last,email):
    #add a new record to the table

    #connect to db
    conn = sqlite3.connect('customer.db')
    #create cursor
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES(?,?,?)",(first,last,email))

    #commit and close
    conn.commit()
    conn.close()