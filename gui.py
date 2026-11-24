import tasks
import customtkinter as ctk
from safe_tooltip import SafeToolTip

current_filter = 'all'

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
        if current_filter != 'all' and task['status'] != current_filter:
            continue
        
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

def changeFilter(new_filter):
    global current_filter
    current_filter = new_filter

    updateFilterButtons()
    refreshTasks()

def updateFilterButtons():
    for filter_name, button in filter_buttons.items():
        if filter_name == current_filter:
            button.configure(
                border_width=2,
                border_color=button.cget('text_color'),
                text_color_disabled=button.cget('text_color'),
                state='disabled')
        else:
            button.configure(
                border_width=0,
                state='normal')
            
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
label1.pack(pady=(10,0), padx=10, anchor='n')

entry_frame = ctk.CTkFrame(
    main_frame,
    fg_color='transparent')
entry_frame.pack(pady=(10,0))

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
    pady=(15,0))

button_add = ctk.CTkButton(
    entry_frame,
    text='Add Task',
    width=40,
    height=30,
    corner_radius=15,
    command=readEntry)
button_add.pack(side=ctk.RIGHT, pady=(15,0))

filter_frame = ctk.CTkFrame(
    main_frame,
    height=60,
    corner_radius=20,
    fg_color='transparent')
filter_frame.pack(fill='x', pady=(30,0), padx=20)

button_all = ctk.CTkButton(
    filter_frame,
    text='All',
    corner_radius=20,
    height=30,
    width=170,
    fg_color='gray25',
    text_color='#F9FAFB',
    hover_color='#4B5563',
    command= lambda: changeFilter('all'))
button_all.pack(side=ctk.LEFT, padx=(18,0))

button_todo = ctk.CTkButton(
    filter_frame,
    text='To Do',
    corner_radius=20,
    height=30,
    width=170,
    fg_color='#713F12',
    text_color='#FCD34D',
    hover_color='#854D0E',
    command= lambda: changeFilter('todo'))
button_todo.pack(side=ctk.LEFT)

button_inProgress = ctk.CTkButton(
    filter_frame,
    text='In Progress',
    corner_radius=20,
    height=30,
    width=170,
    fg_color='#1E3A5F',
    text_color='#93C5FD',
    hover_color='#1D4E80',
    command= lambda: changeFilter('in-progress'))
button_inProgress.pack(side=ctk.LEFT)

button_done = ctk.CTkButton(
    filter_frame,
    text='Done',
    corner_radius=20,
    height=30,
    width=170,
    fg_color='#14532D',
    text_color='#86EFAC',
    hover_color='#166534',
    command= lambda: changeFilter('done'))
button_done.pack(side=ctk.LEFT, padx=(0,18))

filter_buttons = {
    'all': button_all,
    'todo': button_todo,
    'in-progress': button_inProgress,
    'done': button_done
}

task_frame = ctk.CTkScrollableFrame(
    main_frame,
    corner_radius=15,
    fg_color='transparent')
task_frame.pack(fill='both', expand=True, padx=20)

updateFilterButtons()
refreshTasks()

root.mainloop()
