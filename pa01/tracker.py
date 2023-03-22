# Create a file tracker.py which offers the user the following options and makes calls to the Transaction class to update the database.

# 1 - 3 are removed by hickey
# 0. quit
# 1. show categories
# 2. add category
# 3. modify category
# 4. show transactions
# 5. add transaction
# 6. delete transaction
# 7. summarize transactions by date
# 8. summarize transactions by month
# 9. summarize transactions by year
# 10. summarize transactions by category
# 11. print this menu

# The tracker.py program should not have any SQL calls and should be similar is structure to the todo2.py program from Lesson19


######################################################################################################################################################################
'''
    I copied pasted everything from the toDo list example in class, so the functions still need modifications to complete this PA. 
    The ones that still need modifications are commented with need modification.
'''
######################################################################################################################################################################

from transactions import Transaction
import sys

# Completed
def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage t = "transactions", [argument]:
            0. quit
            1. show_t
            2. add_t
            3. delete_t
            4. sum_t [date]
            5. sum_t [month]
            6. sum_t [year]
            7. sum_t [catagories]
            8. print_usage
            '''
            )

# Need modication 
def print_todos(todos):
    ''' print the transactions '''
    if len(todos)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-30s %-10s"%('item #','title','desc','completed'))
    print('-'*40)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-30s %2d"%values)

# Need modication 
def process_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    transaction = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_todos(todolist.selectActive())
    elif arglist[0]=="showall":
        print_todos(todos = todolist.selectAll())
    elif arglist[0]=="showcomplete":
        print_todos(todolist.selectCompleted())
    elif arglist[0]=='add':
        if len(arglist)!=3:
            print_usage()
        else:
            todo = {'title':arglist[1],'desc':arglist[2],'completed':0}
            todolist.add(todo)
    elif arglist[0]=='complete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.setComplete(arglist[1])
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.delete(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_usage()

# Need modication 
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
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()