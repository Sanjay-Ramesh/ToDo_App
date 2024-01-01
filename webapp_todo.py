import streamlit as st
import todo_functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    todo_functions.write_todos(todos)

todos = todo_functions.get_todos()

st.title("MyTodo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        todo_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Hello", placeholder="Add New Todo:",
              on_change=add_todo, key="new_todo" )