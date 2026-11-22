import sys
import json
from datetime import datetime
from pathlib import Path

def add(description):
    now = datetime.now().isoformat()

    task = {
        'id': data['next_id'],
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }

    data['tasks'].append(task)
    data['next_id'] += 1

    save_tasks()
    print(f"Task successfully added (ID: {task['id']})")

def update(task_id, new_description):
    for task in data['tasks']:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()

            save_tasks()
            print(f'Task {task_id} updated successfully.')
            return

    print(f'Task with ID {task_id} not found.')

def delete(task_id):
    for task in data['tasks']:
        if task['id'] == task_id:
            data['tasks'].remove(task)

            save_tasks()
            print(f'Task with ID {task_id} removed successfully.')
            return

    print(f'Task with ID {task_id} not found.')

def mark_status(task_id, new_status):
    for task in data['tasks']:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = datetime.now().isoformat()

            save_tasks()
            print(f'Task with ID {task_id} status updated successfully.')
            return

    print(f'Task with ID {task_id} not found.')

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_tasks():
    if Path("tasks.json").exists():
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, UnicodeDecodeError):
            print("Error: tasks.json contains invalid JSON.")
            sys.exit(1)

        if isinstance(data, list):
            next_id = max((task['id'] for task in data), default=0) + 1
            return {
                'next_id': next_id,
                'tasks': data
            }

        if not isinstance(data, dict) or 'next_id' not in data or not isinstance(data.get('tasks'), list):
            print("Error: tasks.json has an invalid structure.")
            sys.exit(1)

        return data

    return {
        'next_id': 1,
        'tasks': []
    }

def list_tasks(param):
    if not data['tasks']:
        print('No tasks found.')
        return

    found = False
    for task in data['tasks']:
        if param == 'all' or task['status'] == param:
            print(f"{task['id']} | {task['description']} | {task['status']}")
            found = True

    if not found:
        print('No tasks found.')
        
data = load_tasks()
