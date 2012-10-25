class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

node1 = Node("Luke")
node2 = Node("Thomas")

print(node1)
print(node2)
