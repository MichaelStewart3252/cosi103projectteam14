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
    # print('t='+str(t))
    transaction = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

# Need more functions
class Transaction():
    global filename
    def __init__(self, file) -> None:
        self.filename = file
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (amount num, category text, date text, description text)''',())
     
    def runQuery(self,query,tuple):
        ''' return all of the transactions
          as a list of dicts.'''
        con = sqlite3.connect(self.filename)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall() 
        con.commit() 
        con.close() 
        return [toDict(t) for t in tuples]
    
    def selectAll(self):
        ''' return all the transactions as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transactions",())

    def add(self,item):
        ''' create a transaction item and add it to the transaction table '''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        ''' delete a transaction item '''
        return self.runQuery("DELETE FROM transactions WHERE rowid=(?)",(rowid,))

    def selectCategory(self,category):
        ''' return all of the transactions of specifc date.'''
        return self.runQuery("SELECT rowid,* FROM transactions WHERE category=(?)",(category,))
    
    def selectDate(self,date):
        ''' return all of the transactions of specifc date.'''
        pattern = date + '-__-' + '____'
        return self.runQuery("SELECT rowid,* FROM transactions WHERE date LIKE (?)",(pattern,))

    def selectMonth(self,month):
        ''' return all of the transactions of specifc month.'''
        pattern = '__-' + month + '-____'
        return self.runQuery("SELECT rowid,* FROM transactions WHERE date LIKE (?)",(pattern,))
    
    def selectYear(self,year):
        ''' return all of the transactions of specifc year.'''
        pattern = '__' + '-__-' + year
        return self.runQuery("SELECT rowid,* FROM transactions WHERE date LIKE (?)",(pattern,))
