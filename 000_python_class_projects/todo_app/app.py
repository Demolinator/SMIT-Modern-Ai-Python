import streamlit as st
from src.storage import load_tasks, save_tasks
from src.core import add_task, mark_done, delete_task 



st.title("Todo APPLICATION")

# Load Tasks once
if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()


tasks = st.session_state.tasks


# Add Task
st.subheader("Add New Task")
title = st.text_input("Task Name")

if st.button("Add Task"):
    add_task(tasks, title)
    save_tasks(tasks)
    st.success("Task Added...")


# Show Task
st.subheader("Tasks")

if not tasks:
    st.info("No tasks yet.")
else:
    for i, task in enumerate(tasks):
        col1, col2, col3 = st.columns([6, 2, 2])

        col1.write(
            f"completed {task["title"]}" if task["done"] else f"{task["title"]}"
        )

        if col2.button("Done", key=f"done-{i}"):
            mark_done(tasks, i)
            save_tasks(tasks)

        if col3.button("Delete", key=f"del-{i}"):
            delete_task(tasks, i)
            save_tasks(tasks)   