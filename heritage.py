import random
from abc import ABC
from typing import final

class Life(ABC):
    def __init__(self, description, size, age):
        self.description = description
        self.size = size
        self.age = age

class Green(Life):
    def __init__(self, species, color, age, description, size):
        super().__init__(description, size, age)
        self.species = species
        self.color = color
        self.age = age

@final
class Tree(Green):
    def __init__(self, species, color, age, description, size):
        super().__init__(description, size, age, species, color)

    def info(self):
        print(self.species, self.color, self.age, self.description, self.size)

class Flower(Green):
    def __init__(self, species, color, age, description, size, sent):
        super().__init__(description, size, age, species, color)
        self.sent = sent


def main():
    nb_trees = random.randint(5,50)
    print(f"You garden contain: {nb_trees} trees.")

    trees = []

    for _ in range(nb_trees):
        tree = Tree("Oak", "Green", str(random.randint(5, 100)) + " inches", "A big oak tree", "Large")
        trees.append(tree)


    for tree in trees:
        tree.info()

if __name__ == '__main__':
    main()