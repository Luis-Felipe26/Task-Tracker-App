import tkinter as tk
import tasks 
from tkinter import ttk

visible_tasks = []

def readEntry():
    description = entry.get()
    
    if not description.strip():
        print('Please provide a task.')
        return
    
    tasks.add(description)
    
    
    refreshListbox()
    entry.delete(0, tk.END)

def deleteTask():
    selection = listbox.curselection()

    if not selection:
        print('Please select a task.')
        return

    index = selection[0]
    selected_task = visible_tasks[index]
    task_id = selected_task['id']
    tasks.delete(task_id)
    
    refreshListbox()

def updateTask():
    selection = listbox.curselection()
    
    if not selection:
        print('Please select a task.')
        return
    
    index = selection[0]
    new_description = entry.get()
    
    if not new_description.strip():
        print('Please provide the update.')
        return
    
    selected_task = visible_tasks[index]
    task_id = selected_task['id']
    tasks.update(task_id, new_description)
    
    refreshListbox()
    entry.delete(0, tk.END)

def markStatus(new_status):
    selection = listbox.curselection()
    
    if not selection:
        print('Please select a task.')
        return
    
    index = selection[0]
    
    selected_task = visible_tasks[index]
    task_id = selected_task['id']
    tasks.mark_status(task_id, new_status)
    
    refreshListbox()

def refreshListbox():
    global visible_tasks
    
    selected_filter = filter_box.get()
    
    status_map ={
        'To Do': 'todo',
        'In Progress': 'in-progress',
        'Done': 'done'    
    }
    
    if selected_filter == 'All':
        visible_tasks = tasks.data['tasks']
    else:
        visible_tasks = []
        selected_status = status_map[selected_filter]
        
        for task in tasks.data['tasks']:
            if task['status'] == selected_status:
                visible_tasks.append(task)
    
    listbox.delete(0, tk.END)
    for task in visible_tasks:
        listbox.insert(tk.END, f"{task['description']}   ({task['status']})")

def onFilterChange(event):
    refreshListbox()

root = tk.Tk()
root.title('Task Tracker')
root.geometry("800x500")
root.resizable(False, False)

label = tk.Label(root, text="My Tasks", font=("Arial", 26, "bold"))
label.pack(pady=20)
entry = tk.Entry(root, width=60)
entry.pack()
button1 = tk.Button(root, text="Add Task", command=readEntry)
button1.pack(pady=5)

filter_box = ttk.Combobox(
    root,
    values =['All', 'To Do', 'In Progress', 'Done'],
    state= 'readonly'
)
filter_box.bind('<<ComboboxSelected>>', onFilterChange)
filter_box.current(0)
filter_box.pack(pady=5)

listbox = tk.Listbox(root,width= 100)
listbox.pack(pady=5)

button2 = tk.Button(root, text="Delete Task", command=deleteTask)
button2.pack(pady=5)
button3 = tk.Button(root, text="Update Task", command=updateTask)
button3.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)
button4 = tk.Button(button_frame, text="Mark as Done", command=lambda: markStatus('done'))
button4.pack(side=tk.LEFT, padx=5)
button5 = tk.Button(button_frame, text="Mark as In Progress", command=lambda: markStatus('in-progress'))
button5.pack(side=tk.RIGHT, padx=5)

refreshListbox()

root.mainloop()