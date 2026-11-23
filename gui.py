import tasks
import customtkinter as ctk
from safe_tooltip import SafeToolTip

def refreshTasks():
    status_names = {
        'done': 'Done',
        'todo': 'To Do',
        'in-progress': 'In Progress'}

    status_name_colors = {
        'done': '#86EFAC',
        'todo': '#FCD34D',
        'in-progress': '#93C5FD'}

    status_background_colors = {
        'done': '#14532D',
        'todo': '#713F12',
        'in-progress': '#1E3A5F'}

    for widget in task_frame.winfo_children():
        widget.destroy()

    for task in tasks.data['tasks']:
        status_name = status_names[task['status']]
        status_name_color = status_name_colors[task['status']]
        status_background_color = status_background_colors[task['status']]

        task_card = ctk.CTkFrame(
            task_frame,
            fg_color='gray22',
            corner_radius=30,
            height=60)
        task_card.pack_propagate(False)
        task_card.pack(fill='x', pady=2.5)

        task_label = ctk.CTkLabel(
            task_card,
            text=task['description'],
            fg_color='transparent')
        task_label.pack(side=ctk.LEFT, padx=(10, 0), pady=5)

        button_delete = ctk.CTkButton(
            task_card,
            text='X',
            text_color='gray',
            fg_color='transparent',
            hover_color='gray25',
            corner_radius=10,
            width=10,
            height=20,
            command = lambda task_id=task['id']: deleteTask(task_id))
        button_delete.pack(side=ctk.RIGHT, pady=5, padx=(2.5,5))
        tooltip_delete = SafeToolTip(button_delete, message="Delete Task", delay=0.3)
            
        status_label = ctk.CTkLabel(
            task_card,
            text=status_name,
            corner_radius=10,
            fg_color=status_background_color,
            text_color=status_name_color,
            height=20)
        status_label.pack(side=ctk.RIGHT, pady=5)
        
        if task['status'] !='done':
            button_done = ctk.CTkButton(
                task_card,
                text='✔',
                text_color='gray',
                fg_color='transparent',
                hover_color='gray25',
                corner_radius=10,
                width=10,
                height=20,
                command= lambda task_id=task['id'], new_status='done': changeStatus(task_id, new_status))
            button_done.pack(side=ctk.RIGHT, pady=5, padx=2.5)
            tooltip_done = SafeToolTip(button_done, message="Mark as Done", delay=0.3)
        
        if task['status'] == 'todo':
            button_inProgress = ctk.CTkButton(
                task_card,
                text='⧖',
                font=('Arial', 15),
                text_color='gray',
                fg_color='transparent',
                hover_color='gray25',
                corner_radius=10,
                width=10,
                height=20,
                command= lambda task_id=task['id'], new_status='in-progress': changeStatus(task_id, new_status))
            button_inProgress .pack(side=ctk.RIGHT, pady=5, padx=2.5)
            tooltip_inprogress = SafeToolTip(button_inProgress , message="Mark as In Progress", delay=0.3)
        
        if task['status'] == 'done':
            button_reopen = ctk.CTkButton(
                task_card,
                text='⟲',
                font=('Arial', 15),
                text_color='gray',
                fg_color='transparent',
                hover_color='gray25',
                corner_radius=10,
                width=10,
                height=20,
                command= lambda task_id=task['id'], new_status='todo': changeStatus(task_id, new_status))
            button_reopen.pack(side=ctk.RIGHT, pady=5, padx=2.5)
            tooltip_reopen = SafeToolTip(button_reopen, message="Re-open Task", delay=0.3)

def readEntry():
    description = entry.get()

    if not description.strip():
        print('Please provide a task.')
        return

    tasks.add(description)

    refreshTasks()
    entry.delete(0, ctk.END)

def deleteTask(task_id):
    tasks.delete(task_id)
    
    refreshTasks()

def changeStatus(task_id, new_status):
    tasks.mark_status(task_id, new_status)
    
    refreshTasks()

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
root.title('Task Tracker')
root.geometry('800x500')
root.resizable(False, False)

main_frame = ctk.CTkFrame(
    root,
    corner_radius=15)
main_frame.pack(
    padx=20,
    pady=20,
    fill='both',
    expand=True)

label1 = ctk.CTkLabel(
    main_frame,
    text='My Tasks',
    font=('Arial', 36, 'bold'))
label1.pack(pady=10, padx=10, anchor='n')

entry_frame = ctk.CTkFrame(
    main_frame,
    fg_color='transparent')
entry_frame.pack()

entry = ctk.CTkEntry(
    entry_frame,
    width=400,
    height=30,
    corner_radius=15)
entry.pack(
    side='left',
    fill='x',
    expand=True,
    padx=(0, 10),
    pady=30)

button1 = ctk.CTkButton(
    entry_frame,
    text='Add Task',
    width=40,
    height=30,
    corner_radius=15,
    command=readEntry)
button1.pack(side=ctk.RIGHT)

task_frame = ctk.CTkScrollableFrame(
    main_frame,
    corner_radius=15,
    fg_color='transparent')
task_frame.pack(fill='both', expand=True, padx=20)

refreshTasks()

root.mainloop()
