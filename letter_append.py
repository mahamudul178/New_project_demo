
todos=[]
while True:
    user_action=input("Type add, show, edit or exit: ")
    user_action=user_action.strip()
    print(user_action)
    match user_action:
        case 'add':
            todo=input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos: 
                print(item)
            # print(todos)
        case 'edit':
            number=input("Number of the code to edit: ")
            edit_todes=todos[number]
            print(edit_todes)
        case exit:
            break