FILEPATH =  'todo_functions_data.txt'
#for read functions
def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#for write functions
def write_todos(todos_arg,filepath = FILEPATH):
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)