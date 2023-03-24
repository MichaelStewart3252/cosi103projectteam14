######################################################################################################################################################################
'''
    Description from mastery app
'''
######################################################################################################################################################################

# create a Python class Transaction in a new file transaction.py which will store financial transactions with the fields. 
# It should have an __init__ method where you pass in the filename for the database to be used (e.g. tracker.db) 
# and each transaction should have the following fields stored in a SQL table called transactions.

# 'item #',                                                                                                                     
# 'amount',
# 'category',
# 'date',
# 'description'

# It should be similar to the Todolist ORM from Lesson 19 in class. It will allow the user to read and update the database as need.
# The transaction class should not do any printing!! 


######################################################################################################################################################################
'''
    I only copied the functions that we will defintely be using and modified them to fit our PA. Still need more functions
'''
######################################################################################################################################################################

import sqlite3

# completed
def toDict(t):
    ''' t is a tuple (rowid, item, amount, category, date, description)'''
    print('t='+str(t))
    transaction = {'rowid':t[0], 'item':t[1], 'amount':t[2], 'category':t[3], 'date':t[4], 'description':t[5]}
    return transaction

# Need more functions
class Transaction():
    global filename
    def __init__(self, filename) -> None:
        self.filename = filename
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item num, amount num, category text, date text, description text)''',())
     
    def runQuery(self,query,tuple):
        ''' return all of the transactions
          as a list of dicts.'''
        con = sqlite3.connect(filename)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
    def selectAll(self):
        ''' return all the transactions as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transaction",())

    def add(self,item):
        ''' create a transaction item and add it to the transaction table '''
        return self.runQuery("INSERT INTO transaction VALUES(?,?,?,?,?)",(item['item'],item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        ''' delete a transaction item '''
        return self.runQuery("DELETE FROM transaction WHERE rowid=(?)",(rowid,))

    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))
