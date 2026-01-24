def show_tasks(tasks):
    return tasks

def add_task(tasks, title):
    if title:
        tasks.append({"title": title, "done": False})

def mark_done(tasks, idx):
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
   

def delete_task(tasks, idx):
    if 0 <= idx < len(tasks):
        tasks.pop(idx)