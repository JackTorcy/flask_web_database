import sqlite3 as sql

def resetTable():
    dbCon = sql.connect('filmflix.db')
    dbCursor = dbCon.cursor()

    with open('data.sql') as file:
        dbCon.executescript(file.read())

if __name__ == '__main__':
    resetTable()
