#!/usr/bin/python3
import MySQLdb
from sys import argv

#the code sould not be executed when imported
if __name__ == "__main_":
    
    #make a connection to the db
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    #it gives us the ability to have multiple sperate working env
    #through the same conn to the db

    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    #clean up the process
    cur.close()
    db.close()
