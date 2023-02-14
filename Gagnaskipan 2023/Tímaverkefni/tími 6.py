class ArreyList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    def resize(array_list):
        pass



    def append(array_list, value):
        array_list.arr[array_list.size] = value
        array_list.size += 1

    def print_array(array_list):
        str_val = ","
        for i in range(array_list.size):
            str_val += (array_list.arr[i])
        print(str_val)  


array_list = ArreyList()
array_list.append(array_list, 4)
array_list.print_array(array_list)








# list1 = [1,2,3,4,5]
list1 = [0] * 5

list1[0] = 4
list1[1] = 2
list1[2] = 6
list1[3] = 4
list1[4] = 8


