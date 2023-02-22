class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        if self.next == None:
            return str(self.data)
        return str(self.data) + " " + str(self.next)

#implement this function
def count_evens(head):
        if head == None:
            return 0
        if head.data % 2 == 0:
            return 1 + count_evens(head.next)
        else:
            return count_evens(head.next)

def unknown_function_A(head):
    your_answer = """
    
        name: biggest_number
        short description: finds the largest number in a LL and counts the instances of the number

    """

class DLL_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = DLL_Node("head node")
        self.tail = DLL_Node("tail node")
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, value):
        new_node = DLL_Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node
        self.head.next.next.prev = new_node

    def print_forwards(self):
        print_string = ""
        node = self.head.next
        while node != self.tail:
            print_string += str(node.data) + " "
            node = node.next
        print(print_string)

    def print_backwards(self):
        print_string = ""
        node = self.tail.prev
        while node != self.head:
            print_string += str(node.data) + " "
            node = node.prev
        print(print_string)

    #implement this function
    def move_from_index_to_front(self, index):
        node = self.head.next
        count = 0
        while node != self.tail:
            if count == index:
                self.add_front(node.data)
                node = node.next
                count += 1
            else:
                node = node.next
                count += 1

            

    def unknown_function_B(self):
        your_answer = """
        
            name: is_ordered
            short description: checks the list if the numbers are ordered i.e if the previous number is smaller than the next(1,2,3
                                returns True if the list is ordered and False if not)

        """

    #implement this function
    def remove_in_range(self, index_from, index_to):
        pass

#implement this function
def combine_sll_dll_into_list(sll_head, dll):
    a_list = []
    node = dll.head.next
    while sll_head != None:
        a_list.append(sll_head.data)
        sll_head = sll_head.next
    while node.next != None:
        a_list.append(node.data)
        node = node.next
    return a_list

if __name__ == "__main__":
    # print("testing sll recursion")
    # print("testing count_evens")
    # head = SLL_Node(5, SLL_Node(4, SLL_Node(4, SLL_Node(9, SLL_Node(7, SLL_Node(5, SLL_Node(10, SLL_Node(16))))))))
    # print(head)
    # print(count_evens(head))
    # head = SLL_Node(2, SLL_Node(1, SLL_Node(4, SLL_Node(3, SLL_Node(5, SLL_Node(10, SLL_Node(7, SLL_Node(11))))))))
    # print(head)
    # print(count_evens(head))
    # head = SLL_Node(7, SLL_Node(6, SLL_Node(3, SLL_Node(1, SLL_Node(2, SLL_Node(0, SLL_Node(2, SLL_Node(1))))))))
    # print(head)
    # print(count_evens(head))
    
    print("testing dll")
    print("testing move_from_index_to_front")
    dll = DLL()
    dll.add_front(7)
    dll.add_front(2)
    dll.add_front(6)
    dll.add_front(4)
    dll.add_front(1)
    dll.add_front(0)
    dll.add_front(5)
    dll.add_front(9)
    dll.print_forwards()
    dll.print_backwards()
    index = 4
    print("index: " + str(index))
    dll.move_from_index_to_front(index)
    dll.print_forwards()
    dll.print_backwards()
    # dll = DLL()
    # dll.add_front(7)
    # dll.add_front(2)
    # dll.add_front(6)
    # dll.add_front(4)
    # dll.add_front(1)
    # dll.add_front(0)
    # dll.add_front(5)
    # dll.add_front(9)
    # dll.print_forwards()
    # dll.print_backwards()
    # index = 7
    # print("index: " + str(index))
    # dll.move_from_index_to_front(index)
    # dll.print_forwards()
    # dll.print_backwards()
    # dll = DLL()
    # dll.add_front(7)
    # dll.add_front(2)
    # dll.add_front(6)
    # dll.add_front(4)
    # dll.add_front(1)
    # dll.add_front(0)
    # dll.add_front(5)
    # dll.add_front(9)
    # dll.print_forwards()
    # dll.print_backwards()
    # index = 0
    # print("index: " + str(index))
    # dll.move_from_index_to_front(index)
    # dll.print_forwards()
    # dll.print_backwards()
    # dll = DLL()
    # dll.add_front(7)
    # dll.add_front(2)
    # dll.add_front(6)
    # dll.add_front(4)
    # dll.add_front(1)
    # dll.add_front(0)
    # dll.add_front(5)
    # dll.add_front(9)
    # dll.print_forwards()
    # dll.print_backwards()
    # index = 1
    # print("index: " + str(index))
    # dll.move_from_index_to_front(index)
    # dll.print_forwards()
    # dll.print_backwards()
    # print("testing remove_in_range")
    # dll = DLL()
    # dll.add_front(7)
    # dll.add_front(2)
    # dll.add_front(6)
    # dll.add_front(4)
    # dll.add_front(1)
    # dll.add_front(0)
    # dll.add_front(5)
    # dll.add_front(9)
    # dll.print_forwards()
    # dll.print_backwards()
    # index_from = 0
    # index_to = 2
    # print("index_from: " + str(index_from))
    # print("index_to: " + str(index_to))
    # dll.remove_in_range(index_from, index_to)
    # dll.print_forwards()
    # dll.print_backwards()
    # dll = DLL()
    # dll.add_front(7)
    # dll.add_front(2)
    # dll.add_front(6)
    # dll.add_front(4)
    # dll.add_front(1)
    # dll.add_front(0)
    # dll.add_front(5)
    # dll.add_front(9)
    # dll.print_forwards()
    # dll.print_backwards()
    # index_from = 3
    # index_to = 7
    # print("index_from: " + str(index_from))
    # print("index_to: " + str(index_to))
    # dll.remove_in_range(index_from, index_to)
    # dll.print_forwards()
    # dll.print_backwards()
    
    # print("testing general programming")
    # print("testing combine_sll_dll_into_list")
    # head = SLL_Node(5, SLL_Node(4, SLL_Node(4, SLL_Node(9, SLL_Node(7, SLL_Node(5, SLL_Node(10, SLL_Node(16))))))))
    # print("sll: " + str(head))
    # dll = DLL()
    # dll.add_front(7)
    # dll.add_front(2)
    # dll.add_front(6)
    # dll.add_front(4)
    # dll.add_front(1)
    # dll.add_front(0)
    # dll.add_front(5)
    # dll.add_front(9)
    # print("dll: ", end="")
    # dll.print_forwards()
    # print(combine_sll_dll_into_list(head, dll))    