##This is a to-do list started on Thursday, May 28th, 2026
##Lists
task_dictionary = {}
tasks_to_do = []
crossed_off = []
## Methods 
def add_tasks(first_name, tasks_to_do):
    while True:
        try:
            if first_name == 'n':
                task_number = int(input(f"How many tasks do you have to do today? "))
            else: 
                task_number = int(input(f"How many tasks do you have to do today, {first_name.title()} ? "))
    
            if task_number <= 0:
                print("It must be more than 0. ")
            else:
                print("Ok, let's store the task(s) in a list. \n")
                break
        except ValueError:
            print("It must be a number!\n")
            continue

    while task_number:
        try:
            print("---------")
            task_name = input("What task do you have to add? ")
            task_dictionary["task"] = task_name
            task_priority = int(input("What is the priority of this task? (1 = high, 2 = medium, 3 = low) "))
            if task_priority == 1:
                task_dictionary["priority"] = "high priority"
                task_number -= 1
                tasks_to_do.append(task_dictionary)
            elif task_priority == 2:
                task_dictionary["priority"] = "medium priority"
                task_number -=1
                tasks_to_do.append(task_dictionary)
            elif task_priority == 3:
                task_dictionary["priority"] = "low priority "
                tasks_to_do.append(task_dictionary)
                task_number -= 1
        except ValueError:
            print("It must be a number! ")


def show_tasks(tasks_to_do, crossed_off):
    if not tasks_to_do and not crossed_off :
        print("You have to have a task to do first!")
            
    else:
        print("Ok, here are the tasks shown.")

        for task in tasks_to_do:
            for actual_task, priority in task.items():
                print(actual_task, " - ", priority)
        
        for task in crossed_off:
            print(f"{task} = completed")


def cross_off_tasks(tasks_to_do, crossed_off):
    for number in enumerate(tasks_to_do, start= 1):
        print(number)
    try:
        cross_off = int(input("Which one would you like to cross off? "))
        if cross_off <= 0:
            print("It must be a number greater than zero!")
        elif cross_off > len(tasks_to_do):
            print("It must be within range!")
        else:
            print("Ok, we will cross off, ", cross_off)
            chosen_to_pop = tasks_to_do.pop(cross_off - 1)
            crossed_off.append(chosen_to_pop)
        
    except ValueError:
        print("Must be a number!")
## Main Loop

def main():    
    print("Welcome to my to-do list.\n")
    first_name = input("What is your first name so we can customize this list for you? Enter (n) if you don't want your name to be considered: ").strip().lower()
    if first_name == 'n':
        print("Ok, we won't set a name for your list.\n")
    else:
        print(f"\nOk, {first_name.title()}, it is nice to meet you.\n")
    while True:
        if not tasks_to_do and not crossed_off:
            try:
                print("Choose '1' to store some tasks or '9' to quit")
                ask_for_choice = int(input("\nWhat would you like to do? "))
            except ValueError:
                print("It must be a number!")
                continue
        
        else:

            print("\n")
            print("Choice '1' to store some tasks.") 
            print("Choice '2' to see those tasks.")
            print("Choice '3' to cross off the task")
            print("Choice '9' to exit the program.")
            print("\n")
            try:
                ask_for_choice = int(input("What would you like to do? "))
            except ValueError:
                print("You must provide a number!")
                continue
        if ask_for_choice == 1:
            add_tasks(first_name, tasks_to_do)

        elif ask_for_choice == 2:
            show_tasks(tasks_to_do, crossed_off)
 
        elif ask_for_choice == 3:
           cross_off_tasks(tasks_to_do, crossed_off)

        elif ask_for_choice == 9:
            print("Ok, we will exit the program.")
            break


main()