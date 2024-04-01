# front-end

import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.Input(tooltip="Enter a todo", key='todo')
button = Sg.Button("Add")

window = Sg.Window('To-do App',
                   layout=[[label], [input_box, button]],
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
        case Sg.WIN_CLOSED: # variable defined in PySimpleGUI module
            break

window.close()  # close is a third-party method of third party type/class Window of third party library PySimpleGUI
