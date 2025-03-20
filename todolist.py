tasks = []

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def info(self):
        print(f"  - {self.name}: {self.description}")

class Task:
    _id_counter = 1

    def __init__(self, name):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def info(self):
        print(f"\nTâche ID {self.id}: {self.name}")
        if not self.items:
            print("  Aucun item.")
        for element in self.items:
            element.info()

def add_task():
    name = input("\n--Nom de la nouvelle tâche : ")
    new_task = Task(name)

    while True:
        print("\n--Ajouter des items (0 pour quitter)--")
        item_name = input("1--Nom du nouvel item : ")

        if item_name == "0":
            break

        item_description = input("2--Description du nouvel item : ")

        if item_description == "0":
            break

        new_item = Item(item_name, item_description)
        new_task.add_item(new_item)

    tasks.append(new_task)

def show_task():
    if not tasks:
        print("\nAucune tâche enregistrée.")
        return

    for task_obj in tasks:
        task_obj.info()

def delete_task():
    show_task()

    delete = input("Id de la tâche : ")

    for each_task in tasks:
        if each_task.id == int(delete):
            tasks.remove(each_task)
            print("Tâche supprimé avec succès")

def program():
    while True:
        print("\n--Programme de tâches--")
        print("\n1- Ajouter une tâche")
        print("2- Voir les tâches")
        print("3- Supprimer une tâche")
        print("0- Quitter")

        choice = input("Faites votre choix : ")

        if choice == "1":
            add_task()
        if choice == "2":
            show_task()
        if choice == "3":
            delete_task()
        if choice == "0":
            print("Programme terminé.")
            break

        if choice not in ["1","2","3","0"]:
            print("Choix invalide.")

if __name__ == "__main__":
    program()
