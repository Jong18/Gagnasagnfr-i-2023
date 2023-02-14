class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def put_front(self, data, next):
        new_node = Node(data, next)

    def __str__(self):
        ret_str = ""
        node = self.data
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str




head = Node()
head.data = "string 1"
node = head

for i in range(2, 6):
    head = head.put_front("string " + str(i))

print(head)