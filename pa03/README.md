# Finance Tracker: SQL, pytest, and pylint

This is a simple terminal finance tracker that allows user to store their transaction and analyze them, similar to a stock website.

## Running pylint
### tracker.py
```
tracker.py:46:10: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
tracker.py:50:14: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
tracker.py:52:0: R0912: Too many branches (15/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.48/10 (previous run: 8.28/10, +1.20)
```
### transactions.py
These are all neccessary for readability
```
transactions.py:27:0: C0301: Line too long (112/100) (line-too-long)
transactions.py:43:26: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:45:31: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:46:20: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:47:19: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:49:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:56:0: C0301: Line too long (140/100) (line-too-long)
transactions.py:65:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:73:0: C0301: Line too long (115/100) (line-too-long)
transactions.py:74:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:78:0: C0301: Line too long (115/100) (line-too-long)
transactions.py:79:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:80:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:81:0: C0305: Trailing newlines (trailing-newlines)
transactions.py:38:29: W0622: Redefining built-in 'tuple' (redefined-builtin)

------------------------------------------------------------------
Your code has been rated at 5.31/10 (previous run: 5.31/10, +0.00)
```
## Running pytest
```
======================================= test session starts =======================================
platform darwin -- Python 3.9.6, pytest-7.2.1, pluggy-1.0.0
rootdir: [User PATH]
plugins: anyio-3.6.2
collected 7 items                                                                                                                                               

test_transaction.py .......                                                                [100%]
======================================= 7 passed in 0.03s ======================================= 
```
## Project Demonstration
```
usage:
            0. quit
            1. show transactions (command: show)
            2. add transaction (command: add [amount] [category] [yyyy-mm-dd] [description])
            3. delete transaction (command: delete [transaction ID])
            4. summarize transaction by day (command: sum_d [dd])
            5. summarize transaction by month (command: money sum_m [mm])
            6. summarize transactions by year (command: sum_y [yyyy])
            7. summarize transactions by category (command: sum_cat [catagories])
            8. print this menu (command: print_usage)
            
command> add transaction 10 test 2023-03-26 test
--------------------------------------------------------------------------------



command> add transaction 10 test 2023-03-26 test1
--------------------------------------------------------------------------------



command> add transaction 10 test 2023-03-25 test2
--------------------------------------------------------------------------------



command> show


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          transaction 10         test            2023-03-26 test               
2          transaction 10         test            2023-03-26 test1              
3          transaction 10         test            2023-03-25 test2              
--------------------------------------------------------------------------------



command> sum_d


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          transaction 10         test            2023-03-26 test               
2          transaction 10         test            2023-03-26 test1              
3          transaction 10         test            2023-03-25 test2              
--------------------------------------------------------------------------------



command> add transaction 10 test 2023-04-26 test        
--------------------------------------------------------------------------------



command> show  


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          transaction 10         test            2023-03-26 test               
2          transaction 10         test            2023-03-26 test1              
3          transaction 10         test            2023-03-25 test2              
4          transaction 10         test            2023-04-26 test               
--------------------------------------------------------------------------------



command> sum_m 03
no tasks to print
--------------------------------------------------------------------------------



command> delete 1
--------------------------------------------------------------------------------



command> show  


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
2          transaction 10         test            2023-03-26 test1              
3          transaction 10         test            2023-03-25 test2              
4          transaction 10         test            2023-04-26 test               
--------------------------------------------------------------------------------



command> delete 2
--------------------------------------------------------------------------------



command> delete 3
--------------------------------------------------------------------------------


minstonewang@minstones-air pa03 % /usr/bin/python3 /Users/minstonewang/Desktop/SPRING_2023/COSI_103/team/cosi103projectteam14/pa03/tracker.py
usage:
            0. quit
            1. show transactions (command: show)
            2. add transaction (command: add [amount] [category] [yyyy-mm-dd] [description])
            3. delete transaction (command: delete [transaction ID])
            4. summarize transaction by day (command: sum_d [dd])
            5. summarize transaction by month (command: money sum_m [mm])
            6. summarize transactions by year (command: sum_y [yyyy])
            7. summarize transactions by category (command: sum_cat [catagories])
            8. print this menu (command: print_usage)
            
command> add 10 test 2023-01-01 test
--------------------------------------------------------------------------------



command> add 10 test 2023-02-02 test2   
--------------------------------------------------------------------------------



command> sum_d


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          10         test       2023-01-01      test                          
2          10         test       2023-02-02      test2                         
--------------------------------------------------------------------------------



command> sum_m 01


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          10         test       2023-01-01      test                          
--------------------------------------------------------------------------------



command> sum_y 2023


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          10         test       2023-01-01      test                          
2          10         test       2023-02-02      test2                         
--------------------------------------------------------------------------------



command> add 10 test 2022-01-01 test3   
--------------------------------------------------------------------------------



command> show


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          10         test       2023-01-01      test                          
2          10         test       2023-02-02      test2                         
3          10         test       2022-01-01      test3                         
--------------------------------------------------------------------------------



command> sum_y 2023


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
1          10         test       2023-01-01      test                          
2          10         test       2023-02-02      test2                         
--------------------------------------------------------------------------------



command> delete 1
--------------------------------------------------------------------------------



command> show


item #     amount     category   date            description                   
--------------------------------------------------------------------------------
2          10         test       2023-02-02      test2                         
3          10         test       2022-01-01      test3                         
--------------------------------------------------------------------------------



command> quit
```