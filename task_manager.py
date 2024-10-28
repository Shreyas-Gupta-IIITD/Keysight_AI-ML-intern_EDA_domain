#display the menu to user
def menu():
    print("\n Task Manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as done")
    print("4. Delete Task")
    print("5. Exit")

# add tasks in the list    
def add(tasks):
    task=input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added")

# view the tasks in the list
def view(tasks):
    print("\n Tasks")
    for index, task in enumerate(tasks):
        status="Completed" if task["done"] else "Pending"
        print(f"{index + 1}.{task['task']} - {status}")

# marking the status of the tasks in the list
def marking(tasks):
    task_index=int(input("Enter the task number to mark as complete"))-1
    if(0<=task_index<len(tasks)):
        tasks[task_index]["done"]=True
        print("Task marked done")
    else:
        print("invalid number")

# deleting the task in the list        
def delete(tasks):
    taskk_index=int(input("Enter the task nummber to be deleted"))-1
    if(0<=taskk_index<len(tasks)):
        tasks.pop(taskk_index)
        print("Task deleted")
    else:
        print("invalid number")       
        
# main functions
def main():
    tasks=[]
    
    try:
        with open("TaskManager.txt", "r") as infile:
            for line in infile:
                task, status = line.rstrip("\n").split(",")
                done=status.strip()=="completed"
                tasks.append({"task": task, "done": done})
    except FileNotFoundError:
        print("The <TaskManager.txt> file is not found. Starting a new task manager.")
    
    while True:
        menu()
        choice= input("Enter the choice: ")
        
        if(choice=='1'):
            add(tasks)
            
        elif(choice=='2'):
            view(tasks)
                
        elif(choice=='3'):
            marking(tasks)
                
        elif(choice=='4'):
            delete(tasks) 
                
        elif(choice=='5'):
            print("Program Terminated")
            break
        
        else:
            print("Invalid choice enter a choice between 1-5")
            
    #saving to txt file 
    with open("TaskManager.txt", "w") as outfile:
        for task in tasks:
            status="completed"if task["done"] else "pending"
            outfile.write(f"{task['task']},{status}\n")


if __name__=="__main__":
    main()