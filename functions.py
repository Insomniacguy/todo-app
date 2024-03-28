FILEPATH = 'files/subfiles/todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list to the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(help(write_todos))
print(__name__)
if __name__ == "__main__":
    print("hello from functions module")
    print(get_todos())
