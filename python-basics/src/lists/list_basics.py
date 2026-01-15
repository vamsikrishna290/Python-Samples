# https://www.geeksforgeeks.org/dsa/python-data-structures-and-algorithms/


def list_basics():
    # Lists can be created in several ways, such as using square brackets,
    # the list() constructor or by repeating elements.
    list1 = [1,2,3,4, True, 'Vamsi']
    for i in list1:
        print(i)

    a = list((1, 2, 3, 'apple', 4.5))
    print(a)

    b = list("GFG") # O/P ['G', 'F', 'G']
    print(b)

    # Creating List with Repeated Elements
    a = [2] * 5 # O/P [2, 2, 2, 2, 2]
    b = [0] * 7
    print(a)
    print(b)

def list_access_elements():
    # Accessing List Elements
    a = [10, 20, 30, 40, 50]
    print(a[0])
    print(a[-1])
    print(a[1:4])   # elements from index 1 to 3

def alter_list():
    # We can add elements to a list using the following methods:
    #
    # append(): Adds an element at the end of the list.
    # extend(): Adds multiple elements to the end of the list.
    # insert(): Adds an element at a specific position.
    # clear(): removes all items.
    a = []
    a.append(10)
    print("After append(10):", a)
    a.insert(0, 5)
    print("After insert(0, 5):", a)

    a.extend([15, 20, 25])
    print("After extend([15, 20, 25]):", a)

    a.clear()
    print("After clear():", a)

    # Removing Elements from List
    # We can remove elements from a list using:
    #
    # remove(): Removes the first occurrence of an element.
    # pop(): Removes the element at a specific index or the last element if no index is specified.
    # del statement: Deletes an element at a specified index.

    a = [10, 20, 30, 40, 50]

    a.remove(30)
    print("After remove(30):", a)

    popped_val = a.pop(1)
    print("Popped element:", popped_val)
    print("After pop(1):", a)

    del a[0]
    print("After del a[0]:", a)


def list_comprehension():
    squares = [x**2 for x in range(1, 6)]
    print(squares)

if __name__ == '__main__':
    list_basics()
    list_access_elements()
    alter_list()
    list_comprehension()