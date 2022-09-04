

class TreeNode:

    def __init__(self, name, designation):
        self.parent = None
        self.name = name
        self.designation = designation
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

    def print_tree(self, type):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__"
        if type == "name":
            print(prefix + self.name if self.parent else self.name)
        elif type == "designation":
            print(prefix + self.designation if self.parent else self.designation)
        else:
            print(prefix + f"{self.name} ({self.designation})" if self.parent else f"{self.name} ({self.designation})")
        if self.children:
            for child in self.children:
                child.print_tree(type)



nilupul = TreeNode("Nilupul", "CEO")

chinmay = TreeNode("Chinmay", "CTO")

nilupul.add_child(chinmay)

vishwa = TreeNode("Vishwa", "Infra Head")
chinmay.add_child(vishwa)

dhaval = TreeNode("Dhaval", "Cloud Manager")
abhijeet = TreeNode("Abhijeet", "App Manager")

vishwa.add_child(dhaval)
vishwa.add_child(abhijeet)

amir = TreeNode("Amir", "Application Head")
chinmay.add_child(amir)

gels = TreeNode("Gels", "HR Head")
nilupul.add_child(gels)

peter = TreeNode("Peter", "Recruitment Manager")
waqas = TreeNode("Waqas", "Policy Manager")

gels.add_child(peter)
gels.add_child(waqas)


nilupul.print_tree("designation")