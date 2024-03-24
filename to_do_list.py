class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.is_completed = False

    def to_string(self):
        print (f"The task with ID {self.id} has the description {self.description} with completion status of {self.is_completed}")



class TaskManager:
    counter = 0
    def __init__(self):
        self.to_do_list = []

    def create(self, description):
        self.to_do_list.append(Task(self.counter, description))
        self.counter += 1 

    def edit(self, id):
        for task in self.to_do_list:
            if task.id == id:
                task.is_completed = True

    def view(self):
        for task in self.to_do_list:
            task.to_string()
            

    def delete(self, id):
        for task in (self.to_do_list):
            if task.id == id:
                self.to_do_list.remove(task)

def main():
    
    task_manager = TaskManager()
    print("Welcome to the to do list App")
    while True:
        options = input("Please select one of the following Create/Edit/View/Delete or Quit ").lower()
        if options == 'create':
            description = input("What is the description? ")
            task_manager.create(description)
        elif options == 'edit':
            id = int(input("What is the id of your task."))
            task_manager.edit(id)
        elif options == 'view':
            task_manager.view()
        elif options == 'delete':
            id = int(input("What task would you like to delete?"))
            task_manager.delete(id)
        elif options == 'quit':
            break
        else:
            print("Wrong input.")

main()
