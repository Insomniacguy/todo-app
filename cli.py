# from functions import get_todos, write_todos
import functions # custom module
import time  # standard module

now = time.strftime("%b %m %y, %H:%M:%S")
print("it is", now)

while True:
    user_action = input("Type add, show,edit,complete or exit:\n")
    user_action = user_action.strip()  # stripping out the trailing space

    if user_action.startswith('add'):  # we are assuming user will type add todo
        todo = user_action[4:] + "\n"

        # file = open('files/subfiles/todos.txt', 'r')
        # todos = file.readlines()  # creating a list with file object. file.readlines() returns a list
        # file.close()

        todos = functions.get_todos()  # function call

        todos.append(todo.title())
        #
        # file = open('files/subfiles/todos.txt', 'w')
        # file.writelines(todos)  # method available for file object
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # file = open('files/subfiles/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()  # function call

        # print(todos)
        # new_todos = []
        # for item in todos:
        #     item = item.strip("\n")
        #     new_todos.append(item)

        # new_todos = [item.strip('\n') for item in todos]  # list-comprehension( it is a quicker way of for loop )
        for index, item in enumerate(todos):  # we used for loop to get rid of brackets present in list
            item = item.title().strip("\n")
            # print(index+1,"-",item)
            row = f"{index + 1}.{item}"
            print(row)
            # print(todos)
        # print(f"Length of todos is {index+1}")
        print(f"The length of the todo is {len(todos)}")
    elif user_action.startswith('edit'):
        try:
            # we are assuming user will type "edit 1 or edit 2 or edit any number"
            # number = int(input("number of todo to edit?"))
            # number = number - 1
            number = int(user_action[5:])
            print(number)
            number = number - 1  # decrease the number by 1 to adjust the index system

            todos = functions.get_todos()
            print("Here is the existing todo-list", todos)

            new_todo = input('enter a new todo\n')
            # current_todo = todos[number]
            todos[number] = new_todo + "\n"
            print("Here is the modified to-do list", todos)

            # write a modified list back to the list
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            #  the below code is repetitive so we replace it with "continue"
            # user_action = input("Type add, show,edit,complete or exit:\n")
            # user_action = user_action.strip()
            continue  # opposite of break and will continue back to the beginning of the loop. it will execute input()
    elif user_action.startswith('complete'):
        try:
            # assuming user will type complete 1 or any number etc
            # number = int(input("number of todo to remove"))
            number = int(user_action[9:])
            number = number - 1  # because list indexing starts from 0 so we subtract 1

            todos = functions.get_todos()
            print("Here is the existing todo-list", todos)

            deleted = todos[number].strip()
            todos.pop(number)
            print("Here is the modified list", todos)

            functions.write_todos(todos)

            message = f"{deleted} was removed from the list"
            print(message)
        except IndexError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not found")

print("bye!")
