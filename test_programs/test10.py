

from sys import prefix


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

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__"
        print(prefix + self.data if self.parent else self.data)
        for child in self.children:
            child.print_tree()
            

root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
tv = TreeNode("TV")
fridge = TreeNode("Fridge")

root.add_child(laptop)
root.add_child(tv)
root.add_child(fridge)

mac = TreeNode("Macbook")
dell = TreeNode("Dell")
hp = TreeNode("HP")

laptop.add_child(mac)
laptop.add_child(dell)
laptop.add_child(hp)

lg = TreeNode("LG")
samsung = TreeNode("Samsung")
sony = TreeNode("Sony")
whirlpool = TreeNode("Whirlpool")

tv.add_child(lg)
tv.add_child(samsung)
tv.add_child(sony)

fridge.add_child(lg)
fridge.add_child(samsung)
fridge.add_child(whirlpool)

root.print_tree()