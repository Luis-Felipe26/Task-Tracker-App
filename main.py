import sys
import tasks

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a command.")
    else:
        command = sys.argv[1]

        if command == 'add':
            if len(sys.argv) != 3:
                print('Usage: python main.py add "description"')
            elif not sys.argv[2].strip():
                print('Please provide a valid task description.')
            else:
                tasks.add(sys.argv[2].strip())
                
        elif command == 'update':
            if len(sys.argv) != 4:
                print('Usage: python main.py update ID "new description"')
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) < 1:
                print('Invalid ID. Please provide a positive number.')
            elif not sys.argv[3].strip():
                print('Please provide a valid task description.')
            else:
                tasks.update(int(sys.argv[2]), sys.argv[3].strip())
                
        elif command == 'delete':
            if len(sys.argv) != 3:
                print('Usage: python main.py delete ID')
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) < 1:
                print('Invalid ID. Please provide a positive number.')
            else:
                tasks.delete(int(sys.argv[2]))
                
        elif command == 'mark-in-progress':
            if len(sys.argv) != 3:
                print('Usage: python main.py mark-in-progress ID')
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) < 1:
                print('Invalid ID. Please provide a positive number.')
            else:
                tasks.mark_status(int(sys.argv[2]), 'in-progress')
                
        elif command == 'mark-done':
            if len(sys.argv) != 3:
                print('Usage: python main.py mark-done ID')
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) < 1:
                print('Invalid ID. Please provide a positive number.')
            else:
                tasks.mark_status(int(sys.argv[2]), 'done')
                
        elif command == 'list':
            if len(sys.argv) > 3:
                print('Usage: python main.py list [status]')
            elif len(sys.argv) == 2:
                tasks.list_tasks('all')
            elif sys.argv[2] not in ['all', 'todo', 'in-progress', 'done']:
                print('Invalid status. Please provide a valid status [todo, in-progress, done]')
            else:
                tasks.list_tasks(sys.argv[2])
                
        else:
            print("Invalid command.")
