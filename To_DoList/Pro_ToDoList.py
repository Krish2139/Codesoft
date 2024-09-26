def task():
    tasks = []
    print("------To-Do List-------")

    total_task = int(input("Enter how many task you want to add : "))
    for i in range(1, total_task + 1):
        task_name = input("Enter the task {} : ".format(i))
        tasks.append(task_name)

    print("Today's tasks are\n{}".format(tasks))

    while True:
        operation = int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/ : "))
        if operation == 1:
            add = input("Enter task you want to add : ")
            tasks.append(add)
            print("Task {} has been sucessfully added.".format(add))

        elif operation == 2:
            updated_val = input("Enter the task name you want to update : ")
            if updated_val in tasks:
                newtask = input("Enter new task : ")
                oldtask = tasks.index(updated_val)
                tasks[oldtask] = newtask
                print("Updated task {}.".format(newtask))
        
        elif operation == 3:
            del_val = input("Enter the task you want to delete : ")
            if del_val in tasks:
                deltask = tasks.index(del_val)
                del tasks[deltask]
                print("Task {} has been deleted...".format(del_val))

        elif operation == 4:
            print("Total Tasks : {}".format(tasks))

        elif operation == 5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid Input")

task()