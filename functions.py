FILE_PATH = "todos.txt"


def get_todos(file_path=FILE_PATH):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_local, file_path=FILE_PATH):
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_local)
