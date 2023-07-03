import functions
import PySimpleGUI as sg
import time

# Create theme
sg.theme("DarkPurple")
# Create label
label = sg.Text("Type in a to-do")

# Create time
clock = sg.Text("", key='clock')

# Create add input and add button
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)

# Create box include a list of to do
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(44, 15))

# Create edit button
edit_button = sg.Button("Edit", size=10)

# Create complete button
complete_button = sg.Button("Complete", size=15)

# Create exit button
exit_button = sg.Button("Exit", size=10)

# Create window
window = sg.Window("My to-do app",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [complete_button, exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=900)  # read after 10 ms
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todos = functions.get_todos()

                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit !!!", font=('Helvetica', 15))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item to complete !!!", font=('Helvetica', 15))

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break

window.close()
