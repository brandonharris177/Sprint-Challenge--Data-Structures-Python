class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # previous = None
        # current = self.head
        # following = self.head

        # while current is not None:
        #     following = following.next_node
        #     current.next_node = previous
        #     previous = current
        #     current = following
        # self.head = previous
        # return previous

        if node is None:
            return 
        elif node.next_node is None:
            self.head = node 
            return
        else:
            self.reverse_list(node.next_node, None) 
            node.next_node.next_node = node 
            node.next_node = None



    # LList = LinkedList()
    # LList.add_to_head(1)
    # LList.add_to_head(2)
    # LList.add_to_head(3)
    # LList.add_to_head(4)
    # LList.add_to_head(5)
    # print(LList.head.value, 5)
    # LList.reverse_list(LList.head, None)
    # print(LList)
    # assertEqual(list.head.value, 1)
    # assertEqual(list.head.get_next().value, 2)
    # assertEqual(list.head.get_next().get_next().value, 3)