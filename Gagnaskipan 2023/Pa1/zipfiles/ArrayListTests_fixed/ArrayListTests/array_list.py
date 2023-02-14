class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        a_str = ""
        for i in range(self.size):
            if i < self.size -1:
                a_str += str(self.arr[i]) + ", "
            else:
                a_str += str(self.arr[i])
        return a_str

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        if self.size >= self.capacity:
            self.resize()
        arr2 = [0] * self.capacity
        arr2[0] = value
        self.size += 1
        for i in range(self.size - 1):
            arr2[i + 1] = self.arr[i]
        arr2[0] = value
        self.arr = arr2
         




    '''Þarf að klára outside of bounds'''
    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if self.size == self.capacity:
            self.resize()
        arr2 = [0] * self.capacity
        if index > self.size:
            raise IndexOutOfBounds("index out of bounds")
        else:
            for i in range(self.size):
                if i < index:
                    arr2[i] = self.arr[i]
                elif i >= index:
                    arr2[i + 1] = self.arr[i]
            self.size += 1
            arr2[index] = value
            self.arr = arr2


    #Time complexity: O(1) - constant time
    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index > self.size:
            raise IndexOutOfBounds("Index out of bounds")
        if index <= self.size -1:
            return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        return self.arr[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity += self.capacity
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        arr2 = [0] * self.capacity
        if index <= self.size-1:
            for i in range(self.size):
                if i < index:
                    arr2[i] = self.arr[i]
                elif i == index:
                    pass
                else:
                    arr2[i-1] = self.arr[i]
            self.arr = arr2
            self.size -= 1


    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.prepend(23)
    arr_lis.prepend(21)
    arr_lis.prepend(19)
    arr_lis.insert(20, 1)
    arr_lis.insert(22, 3)
    arr_lis.insert(89, 6)
    # arr_lis.append(24)
    # arr_lis.set_at(1, 0)
    # arr_lis.set_at(2, 1)
    # arr_lis.set_at(3, 2)
    # arr_lis.set_at(4, 3)
    # arr_lis.remove_at(1)
    # arr_lis.remove_at(5)
    print(str(arr_lis))
    # # print(arr_lis.get_first())
    # print(arr_lis.get_at(5))
    # # print(arr_lis.get_last())
