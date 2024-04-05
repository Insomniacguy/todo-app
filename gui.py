# front-end

import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.Input(tooltip="Enter a todo", key='todo')
button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), size=(50, 10), key='lb', enable_events=True)
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
# layout = [[label], [input_box, button], [list_box, edit_button]]  # Dynamically creating layout
exit_button = Sg.Button("Exit")
window = Sg.Window('To-do App',
                   layout=[[label],
                           [input_box, button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))  # layout arg requires a list

while True:
    event, values = window.read()  # read is a third-party method of third party type/class Window of third party
    # library PySimpleGUI
    print(event)
    # print(type(event))  # read() returns a tuple
    print(values)
    # print(type(values))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            list_box.update(values=todos)
        case "Edit":
            edited_todo = values['lb'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            # print(type(todos))
            # print(todos)
            # index = todos.index(edited_todo)
            index = todos.index(edited_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            list_box.update(values=todos)
        case 'Complete':
            completed_todo = values['lb'][0]
            todos = functions.get_todos()
            deleted_todo = todos.remove(completed_todo)
            functions.write_todos(todos)
            window['lb'].update(values=todos)
            input_box.update(value='')
        case "lb":
            input_box.update(value=values['lb'][0])
            # value is an arg of elements such as buttons, input box in PySimpleGUI.
            # values is a variable we created above
        case "Exit":
            break
        case Sg.WIN_CLOSED:  # variable defined in PySimpleGUI module
            break
            # exit()
print("bye")
window.close()  # close is a third-party method of third party type/class Window of third party library PySimpleGUI
