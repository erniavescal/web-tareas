"""
usar funcion para eliminar una tarea
"""
import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    # todo_local = st.session_state["new_todo"].strip().capitalize()
    todo_local = st.session_state["new_todo"].strip().capitalize()
    if todo_local == '' or todo_local == ' ':
        return
    todo_local = todo_local + '\n'
    print(todo_local)
    # evitar error de duplicate widget si usuario
    # introduce nueva tarea con mismo nombre que otra existente
    if todo_local not in todos:
        todos.append(todo_local)
        functions.write_todos(todos)
        # borramos la tarea añadida del text_input
        st.session_state["new_todo"] = ""


def complete_todo(key):
    num = int(key)
    st.write(f"Eliminando {todos.pop(num)}")
    functions.write_todos(todos)


st.title("Mi App Tareas")
st.subheader("Esta es mi todo app.")
st.write("Esta app incrementa tu productividad.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index, on_change=complete_todo, args=(str(index)),
                           help="Marca la casilla para eliminar tarea")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Entra una tarea:", placeholder="Añade nueva tarea...",
              on_change=add_todo, key='new_todo')

st.session_state
