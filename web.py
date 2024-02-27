import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''

st.title('My Todo App')
st.subheader("Hello.")
match len(todos):
    case 0:
        text="WELL DONE ITS EMPTY!"
    case _:
        text =f'hihi - {len(todos)} more to go!'
st.write(text)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] # delete that session state key
        st.rerun()


st.text_input(label='Input text here:', placeholder = 'Add a new todo',
              on_change=add_todo, key='new_todo') # key for text input in session_state

print('Hello')
st.session_state

print(st.session_state)
