from xml.dom.minidom import Element


class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
        
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if not self.left:
                return False
            return self.left.search(data)
        else:
            if not self.right:
                return False
            return self.right.search(data)

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements += [self.data]

        return elements


    # def delete(self, data):
    #     if self.data == data:
    #         if not (self.right or self.left):
    #             self.data = None
    #             return
    #         if self.right:
    #             min = self.right.find_min()
    #             self.data = min
    #             self.right.delete(min)
    #             return
    #         if self.left:
    #             max = self.left.find_max()
    #             self.data = max
    #             self.left.delete(max)
    #             return
    #     elif data < self.data:
    #         if self.left:
    #             return self.left.delete(data)
    #     else:
    #         if self.right:
    #             return self.right.delete(data)

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
        
            max = self.left.find_max()
            self.data = max
            self.left = self.left.delete(max)
        
        return self

root = BinarySearchTree(15)
root.add_child(12) 
root.add_child(27)
root.add_child(7)
root.add_child(14)
root.add_child(20)
root.add_child(88)
root.add_child(23)
root.add_child(19)




# print(root.in_order_traversal())
# print(root.pre_order_traversal())
# print(root.post_order_traversal())
# print(root.find_min())
# print(root.find_max())
# print(root.search(12))


print(root.in_order_traversal())
root.delete(12)
print(root.in_order_traversal())


