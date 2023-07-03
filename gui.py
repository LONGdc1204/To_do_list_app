import functions
import PySimpleGUI as sg

# Create label
label = sg.Text("Type in a to-do")

# Create add input and add button
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# Create box include a list of to do
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(44, 15))

# Create edit button
edit_button = sg.Button("Edit")

# Create complete button
complete_button = sg.Button("Complete")

# Create exit button
exit_button = sg.Button("Exit")

# Create window
window = sg.Window("My to-do app",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [complete_button, exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todos = functions.get_todos()

            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break

window.close()
