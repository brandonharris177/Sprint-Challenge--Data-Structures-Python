import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

    # Insert the given value into the tree
    # def insert(self, value):
    #     self_value_len = len(self.value)
    #     valuelen = len(value)
    #     if valuelen < self_value_len:
    #         if self.left is None:
    #             self.left = BSTNode(value)
    #         else:
    #             self.left.insert(value)
    #     elif valuelen >= self_value_len:
    #         if self.right is None:
    #             self.right = BSTNode(value)
    #         else:
    #             self.right.insert(value)

    # def contains(self, target):
    #     self_value_len = len(self.value)
    #     targetlen = len(target)
    #     if self.value == target:
    #         duplicates.append(self.value)
    #     elif self.right != None and targetlen > self_value_len:
    #         return self.right.contains(targetlen)
    #     elif self.left != None and targetlen < self_value_len:
    #         return self.left.contains(targetlen)
    #     else:
    #         pass

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.right != None and target > self.value:
            return self.right.contains(target)
        elif self.left != None and target < self.value:
            return self.left.contains(target)
        else:
            return False
        
tree = BSTNode("mmmmm")

# tree.insert("steve")
# tree.insert("dave")
# print(tree)

for name1 in names_1:
    tree.insert(name1)

for name2 in names_2:
    if tree.contains(name2): 
        duplicates.append(name2)
        

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
