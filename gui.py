# front-end

import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter a todo")
button = Sg.Button("Add")

window = Sg.Window('To-do App', layout=[[label], [input_box, button]]) # layout arg requires a list
window.read()  # read is a third-party method of third party obj Window of third party library PySimpleGUI
window.close()  # close is a third-party method of third party obj Window of third party library PySimpleGUI
