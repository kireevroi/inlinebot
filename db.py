#Implementing database interaction
#Currently used for gaybot
#NOT INJECTION SAFE YET. USE LOCALLY
#Copyright kireevroi

import sqlite3
import random
#class initializing
class db:

    #connection for sqlite
    connection = None;

    #constructor
    def __init__(self, db_name):
        try:
            self.connection = sqlite3.connect(db_name+'.db', check_same_thread=False)
        except:
            pass
        print("database opened")

    #destructor
    def __del__(self):
        self.connection.close()
        print("database closed")
    #table creation wih NOT EXISTS check
    def createTable(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS chat''' + str(table_name) + '''
                         (NAME TEXT NOT NULL,
                         COCKSIZE INT,
                         GAY INT,
                         UNIQUE(NAME))''')
        self.connection.commit()
        cursor.close()
    #Dropping table with IF EXISTS
    def dropTable(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute('''DROP TABLE IF EXISTS chat''' + table_name)
        self.connection.commit()
        cursor.close()
    #Add Line to table
    def addLine(self, table_name, name, cocksize, gay):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT OR IGNORE INTO chat''' + table_name + '''
                         VALUES (?, ?, ?)''', (name, cocksize, gay))
        self.connection.commit()
        cursor.close()
    #update values in line
    def updateLine(self, table_name, name, cocksize, gay):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE chat''' + table_name + '''
                         SET COCKSIZE = ?, GAY = ?
                         WHERE NAME = ?''', (cocksize, gay, name))
        self.connection.commit()
        cursor.close()
    #get the line
    def getLine(self, table_name, name):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT COCKSIZE, GAY FROM chat''' + table_name + '''
                         WHERE NAME = ?''', (name,))
        self.connection.commit()
        data = cursor.fetchone()
        cursor.close()
        return data
    #get max parameter
    def getMax(self, table_name, column):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT NAME, COCKSIZE, GAY FROM chat''' + table_name +
         ''' WHERE ''' + column + ''' = (SELECT MAX(''' + column + ''') FROM chat'''+ table_name +
         ''')''')
        self.connection.commit()
        data = cursor.fetchone()
        cursor.close()
        return data
    #get min parameter
    def getMin(self, table_name, column):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT NAME, COCKSIZE, GAY FROM chat''' + table_name +
         ''' WHERE ''' + column + ''' = (SELECT MIN(''' + column + ''') FROM chat'''+ table_name +
         ''')''')
        self.connection.commit()
        data = cursor.fetchone()
        cursor.close()
        return data
