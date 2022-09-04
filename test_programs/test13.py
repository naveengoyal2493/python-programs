
from operator import le


class TreeNode:

    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__"
        print(prefix + self.data if self.parent else self.data)
        for child in self.children:
            child.print_tree(level)


glbl = TreeNode("Global")
india = TreeNode("India")
gujarat = TreeNode("Gujarat")
ahmedabad = TreeNode("Ahmedabad")
baroda = TreeNode("Baroda")
karnataka = TreeNode("Karnataka")
bangaluru = TreeNode("Bengaluru")
mysore = TreeNode("Mysore")
usa = TreeNode("USA")
new_jersey = TreeNode("New Jersey")
princeton = TreeNode("Princeton")
trenton = TreeNode("Trenton")
california = TreeNode("California")
san_fransisco = TreeNode("San Fransisco")
mountain_view = TreeNode("Mountain View")
palo_alto = TreeNode("Palo Alto")

glbl.add_child(india)
india.add_child(gujarat)
gujarat.add_child(ahmedabad)
gujarat.add_child(baroda)
india.add_child(karnataka)
karnataka.add_child(bangaluru)
karnataka.add_child(mysore)
glbl.add_child(usa)
usa.add_child(new_jersey)
new_jersey.add_child(princeton)
new_jersey.add_child(trenton)
usa.add_child(california)
california.add_child(san_fransisco)
california.add_child(mountain_view)
california.add_child(palo_alto)

glbl.print_tree(3)


