

lst = [i+1 for i in range(10)]

print(lst)

def reverse_list(l):
    l2 = []
    for i in range(len(l)-1, -1, -1):
        l2.append(l[i])
    return l2

if __name__ == '__main__':
    lst = [i+1 for i in range(10)]

    # list reverse
    lst.reverse()
    print(lst)
    lst.reverse()
    print(lst)
    print(reverse_list(lst))
