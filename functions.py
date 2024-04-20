FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Lee un archivo de texto y
     retorna un lista de objetos hacer.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))

def write_todos(todos_arg, filepath=FILEPATH):
    """ Escribe lista de tareas en archivo de texto,
    borra archivo y vuelve a pegar lista completa """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# bloque condicional: no se ejecuta en dia14.py,
# pero si se ejecuta si se ejecuta functions.py
# usado para probar las funciones
if __name__ == "__main__":
    print("Hola desde functions.py")
    print(get_todos("../todos.txt"))

# imprime __main__ si ejecutamos functions.py
# pero imprime modules.functions si se ejecuta dia14.py
print(__name__)
