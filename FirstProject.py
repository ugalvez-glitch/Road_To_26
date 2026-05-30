#This is a to-do list
##Lists
tasks_to_do = []
crossed_off = []
## Methods 
def add_tasks(first_name, tasks_to_do):
    print("Ok, we are going to store some tasks.")
    while True:
        try:
            if first_name == 'n':
                task_number = int(input(f"How many tasks do you have to do today? "))
            else: 
                task_number = int(input(f"How many tasks do you have to do today, {first_name.title()} ? "))
    
            if task_number <= 0:
                print("It must be more than 0. ")
            else:
                print("Ok, let's store the task(s) in a list.")
                break
        except ValueError:
            print("It must be a number!")
            continue

    while task_number:
        task_asking = input("What do you have to do? ")
        tasks_to_do.append(task_asking)
        task_number -= 1

def show_tasks(tasks_to_do, crossed_off):
    if not tasks_to_do:
        print("You have to have a task to do first!")
            
    else:
        print("Ok, here are the tasks shown.")

        for number, task in enumerate(tasks_to_do, start = 1):
            print(number, task + " = to-do")
        if crossed_off:
            for task in crossed_off:
                print(task + " = completed")

def cross_off_tasks(tasks_to_do, crossed_off):
    for number, task in enumerate(tasks_to_do, start = 1):
                print(number, task)
    try:
        cross_off = int(input("Which one would you like to cross off?"))
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
def main():    
    print("Welcome to my to-do list.")
    first_name = input("What is your first name so we can customize this list for you? Enter (n) if you don't want your name to be considered: ").strip().lower()
    if first_name == 'n':
        print("Ok, we won't set a name for your list.\n")
    else:
        print(f"Ok, {first_name.title()}, it is nice to meet you.\n")
    while True:
        if not tasks_to_do:
            try:
                print("Choice '1' to store some tasks or '9' to quit")
                ask_for_choice = int(input("What would you like to do?"))
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