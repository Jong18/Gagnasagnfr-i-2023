def length_of_string(a_string, length):
    if len(a_string) == 0:
        return length
    else:
        return length_of_string(a_string[1:], length + 1)


a_string = "abcd"
length = 0
print(length_of_string(a_string, length))

def linear_search(lis:list, value):
    if len(lis) == 0:
        return False
    if lis[0] == value:
        return True
    else:
        return linear_search(lis[1:], value)


value = 'b'
a_lis = ['q', 1, 'b', 5]
print(linear_search(a_lis, value))


def count_instances(lis:list, value):
    if len(lis) == 0:
        return 0
    elif lis[0] == value:
        return 1 + count_instances(lis[1:], value)
    else:
        return count_instances(lis[1:], value)


count = 0
a_lis = [1,1,1,1,1,4]
value = 1
print(count_instances(a_lis, value))

def cheack_duplicates(lis:list):
    if len(lis) == 0:
        return False
    elif lis[0] in lis[1:]:
        return True
    else:
        return cheack_duplicates(lis[1:])

a_lis = [1,2,3,4,5,3]
print(cheack_duplicates(a_lis))

def remove_duplicates(a_lis):

    if len(a_lis) == 1:
        return a_lis
    is_duplicates = linear_search(a_lis[1:], a_lis[0])
    if is_duplicates == True:
        return remove_duplicates(a_lis[1:])
    else:
        return [a_lis[0]] + remove_duplicates(a_lis[1:])

a_lis = [1,2,3,4,5,3,5]
print(remove_duplicates(a_lis))

def foo(a_str, n):
    if n == 0:
        return 0
    n -= 1
    if a_str[n] == 'a':
        return 1 + foo(a_str, n)
    return foo(a_str, n)


a_string = 'abcsa'
n = 5
print(foo(a_string, n))

def bar(n):
    if n == 1:
        return n
    return n + bar(n-1)

print(bar(6))

def bar(n, m):
    if m == 0:
        return 1
    return n * bar(n, m-1)

print(bar(2, 3))