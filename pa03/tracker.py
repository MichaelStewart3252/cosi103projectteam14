'''
offers the user the following options and makes calls to the Transaction class to update the database.

1 - 3 removed by hickey
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''
import sys
from transactions import Transaction

DASH_NUM = 80 

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            0. quit
            1. show
            2. add [amount] [category] [dd-mm-yyyy] [description]
            3. delete [transaction ID]
            4. sum_d [dd]
            5. sum_m [mm]
            6. sum_y [yyyy]
            7. sum [catagories]
            8. print_usage
            '''
            )

def print_transactions(transactions):
    ''' print the transactions '''
    if len(transactions)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-15s %-30s"%('item #','amount','category','date', 'description'))
    print('-'*DASH_NUM)
    for item in transactions:
        values = tuple(item.values()) #(item #, amount, category, date, description)
        print("%-10s %-10s %-10s %-15s %-30s"%values) 

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    transaction = Transaction('test.db')
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_transactions(transaction.select_all())
    elif arglist[0]=='add':
        if len(arglist)!=5:
            print_usage()
        else:
            trans = {'amount':arglist[1],'category':arglist[2],'date':arglist[3], 'description':arglist[4]}
            transaction.add(trans)
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            transaction.delete(arglist[1])
    elif arglist[0]=='quit':
        sys.exit()
    else:
        print(arglist,"is not implemented")
        print_usage()

# completed 
def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the date as a string
                args = ['add',args[1],args[2],args[3], " ".join(args[4:])]
            process_args(args)
            print('-'*DASH_NUM+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*DASH_NUM+'\n'*3)

    

toplevel()