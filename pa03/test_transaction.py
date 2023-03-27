######################################################################################################################################################################
'''
    Description from mastery app
'''
######################################################################################################################################################################

# Addtests to it for each method in the Transaction class. 
# It is a good idea to add a test each time you implement a feature. 
# You are testing the Transaction class, not the tracker.py user interface code.
import pytest
import os
from transactions import Transaction

## Xiaoran - create a temporary database for testing
@pytest.fixture(scope="module")
def db():
    filename = 'test.db'
    db = Transaction(filename)
    yield db
    os.remove(filename)

## Xiaoran - test select_all function
def test_select_all(db):
    transactions = db.select_all()
    assert isinstance(transactions, list)
    assert len(transactions) == 0

## Xiaoran - test add function
def test_add(db):
    item = {'amount':10, 'category':'Food', 'date':'2022-03-22', 'description':'Sherman Dining Hall'}
    db.add(item)
    transactions = db.select_all()
    assert len(transactions) == 1
    assert transactions[0]['amount'] == 10
    assert transactions[0]['category'] == 'Food'
    assert transactions[0]['date'] == '2022-03-22'
    assert transactions[0]['description'] == 'Sherman Dining Hall'

## Xiaoran - test delete function
def test_delete(db):
    item = {'amount': 5.68, 'category': 'Shopping', 'date': '2022-03-22', 'description': 'Tape'}
    db.add(item)
    transactions = db.select_all()
    assert len(transactions) == 2
    rowid = transactions[1]['rowid']
    db.delete(rowid)
    transactions = db.select_all()
    assert len(transactions) == 1
    assert transactions[0]['amount'] == 10
    assert transactions[0]['category'] == 'Food'
    assert transactions[0]['date'] == '2022-03-22'
    assert transactions[0]['description'] == 'Sherman Dining Hall'

## Xiaoran - test select_category function
def test_select_category(db):
    '''Tests the selecting row by category'''
    item = {'amount': 1.70, 'category': 'Transportation', 'date': '2023-04-25', 'description': 'MBTA Local Bus'}
    db.add(item)
    transactions = db.select_category('Transportation')
    assert len(transactions) == 1
    assert transactions[0]['amount'] == 1.70
    assert transactions[0]['category'] == 'Transportation'
    assert transactions[0]['date'] == '2023-04-25'
    assert transactions[0]['description'] == 'MBTA Local Bus'

def test_sum_by_day(db):
    '''Tests the selection by day'''
    transactions = db.sum_by_day('2023-04-25')
    assert len(transactions) == 1
    assert transactions[0]['amount'] == 1.70
    assert transactions[0]['category'] == 'Transportation'
    assert transactions[0]['date'] == '2023-04-25'
    assert transactions[0]['description'] == 'MBTA Local Bus'
    
def test_sum_by_month(db):
    '''Tests the selection by month'''
    transactions = db.sum_by_month('2023-04')
    assert len(transactions) == 1
    assert transactions[0]['amount'] == 1.70
    assert transactions[0]['category'] == 'Transportation'
    assert transactions[0]['date'] == '2023-04-25'
    assert transactions[0]['description'] == 'MBTA Local Bus'

def test_sum_by_year(db):
    '''Tests the selection by year'''
    transactions = db.sum_by_year('2023')
    assert len(transactions) == 1
    assert transactions[0]['amount'] == 1.70
    assert transactions[0]['category'] == 'Transportation'
    assert transactions[0]['date'] == '2023-04-25'
    assert transactions[0]['description'] == 'MBTA Local Bus'