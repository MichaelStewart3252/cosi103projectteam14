######################################################################################################################################################################
'''
    Description from mastery app
'''
######################################################################################################################################################################

# Addtests to it for each method in the Transaction class. 
# It is a good idea to add a test each time you implement a feature. 
# You are testing the Transaction class, not the tracker.py user interface code.
import os
import pytest
from transactions import Transaction


ITEM1 = {'amount':10, 'category':'Food', 'date':'2022-03-22', 'description':'Sherman Dining Hall'}
ITEM2 = {'amount':10, 'category':'Food', 'date':'2020-02-22', 'description':'Sherman Dining Hall'}
ITEM3 = {'amount':10, 'category':'Food', 'date':'2021-03-21', 'description':'Sherman Dining Hall'}
ITEM4 = {'amount': 1.70, 'category': 'Transportation', 'date': '2023-04-25', 'description': 'MBTA Local Bus'}
ITEM5 = {'amount': 5.68, 'category': 'Shopping', 'date': '2022-01-22', 'description': 'Tape'}



@pytest.fixture(scope="module")
def data_base():
    ''' Xiaoran -create a temporary data_base for testing '''
    filename = 'test.db'
    data_base = Transaction(filename)
    yield data_base
    os.remove(filename)

def test_select_all(data_base):
    ''' Xiaoran - test select_all function'''
    transactions = data_base.select_all()
    assert isinstance(transactions, list)
    assert len(transactions) == 0

def test_add(data_base):
    '''Xiaoran - test add function'''
    data_base.add(ITEM1)
    data_base.add(ITEM2)
    data_base.add(ITEM3)
    data_base.add(ITEM4)
    data_base.add(ITEM5)
    transactions = data_base.select_all()
    assert len(transactions) == 5
    assert transactions[0]['amount'] == 10
    assert transactions[0]['category'] == 'Food'
    assert transactions[0]['date'] == '2022-03-22'
    assert transactions[0]['description'] == 'Sherman Dining Hall'
    assert transactions[1]['amount'] == 10
    assert transactions[1]['category'] == 'Food'
    assert transactions[1]['date'] == '2020-02-22'
    assert transactions[1]['description'] == 'Sherman Dining Hall'
    assert transactions[2]['amount'] == 10
    assert transactions[2]['category'] == 'Food'
    assert transactions[2]['date'] == '2021-03-21'
    assert transactions[2]['description'] == 'Sherman Dining Hall'
    assert transactions[3]['amount'] == 1.70
    assert transactions[3]['category'] == 'Transportation'
    assert transactions[3]['date'] == '2023-04-25'
    assert transactions[3]['description'] == 'MBTA Local Bus'
    assert transactions[4]['amount'] == 5.68
    assert transactions[4]['category'] == 'Shopping'
    assert transactions[4]['date'] == '2022-01-22'
    assert transactions[4]['description'] == 'Tape'


def test_select_category(data_base):
    '''Xiaoran Tests the selecting row by category'''
    transactions = data_base.select_category('Transportation')
    assert len(transactions) == 1
    assert transactions[0]['category'] == 'Transportation'


def test_sum_by_day(data_base):
    '''Michael Tests the summarize by date'''
    transactions = data_base.sum_by_date()
    assert transactions[0]['date'] == '2020-02-22'
    assert transactions[1]['date'] == '2021-03-21'
    assert transactions[2]['date'] == '2022-01-22'
    assert transactions[3]['date'] == '2022-03-22'
    assert transactions[4]['date'] == '2023-04-25'

    
def test_sum_by_month(data_base):
    '''Michael Tests the selection by month'''
    transactions = data_base.sum_by_month('04')
    assert transactions[0]['date'] == '2023-04-25'

def test_sum_by_year(data_base):
    '''Michael Tests the selection by year'''
    transactions = data_base.sum_by_year('2023')
    assert transactions[0]['date'] == '2023-04-25'

def test_delete(data_base):
    '''Xiaoran - test delete function'''
    transactions = data_base.select_category('Shopping')
    rowid = transactions[0]['rowid']
    data_base.delete(rowid)
    transactions = data_base.select_category('Shopping')
    assert len(transactions) == 0
