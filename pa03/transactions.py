'''
create a Python class Transaction in a new file transaction.py which will store financial transactions with the fields. 
It should have an __init__ method where you pass in the filename for the database to be used (e.g. tracker.db) 
and each transaction should have the following fields stored in a SQL table called transactions.

'item #',                                                                                                                     
'amount',
'category',
'date',
'description

It should be similar to the Todolist ORM from Lesson 19 in class. It will allow the user to read and update the database as need.
The transaction class should not do any printing!! 
'''
import sqlite3

# completed
def to_dict(t):
    ''' t is a tuple (rowid, item, amount, category, date, description)'''
    # print('t='+str(t))
    transaction = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

# Need more functions
class Transaction():
    global filename
    def __init__(self, file) -> None:
        self.filename = file
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (amount num, category text, date text, description text)''',())
     
    def run_query(self,query,tuple):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.filename)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall() 
        con.commit() 
        con.close() 
        return [to_dict(tuple) for tuple in tuples]
    
    def select_all(self):
        ''' return all the transactions as a list of dicts.'''
        return self.run_query("SELECT rowid,* from transactions",())

    def add(self,item):
        ''' create a transaction item and add it to the transaction table '''
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        ''' delete a transaction item '''
        return self.run_query("DELETE FROM transactions WHERE rowid=(?)",(rowid,))

    def select_category(self,category):
        ''' return all of the transactions of specifc date.'''
        return self.run_query("SELECT rowid,* FROM transactions WHERE category=(?)",(category,))
    
    def select_date(self,date):
        ''' return all of the transactions of specifc date.'''
        pattern = date + '-__-' + '____'
        return self.run_query("SELECT rowid,* FROM transactions WHERE date LIKE (?)",(pattern,))

    def select_month(self,month):
        ''' return all of the transactions of specifc month.'''
        pattern = '__-' + month + '-____'
        return self.run_query("SELECT rowid,* FROM transactions WHERE date LIKE (?)",(pattern,))
    
    def select_year(self,year):
        ''' return all of the transactions of specifc year.'''
        pattern = '__' + '-__-' + year
        return self.run_query("SELECT rowid,* FROM transactions WHERE date LIKE (?)",(pattern,))
