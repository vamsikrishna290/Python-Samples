def set_creation():
    """Demonstrates various ways to create sets."""
    # Creating an empty set
    empty_set = set()
    print(f"Empty set: {empty_set}")

    # Creating a set from a list
    my_list = [1, 2, 3, 2, 1]
    set_from_list = set(my_list)
    print(f"Set from list {my_list}: {set_from_list}")

    # Creating a set with curly braces
    my_set = {1, 2, 3, 'apple', True}
    print(f"Set with curly braces: {my_set}")

    # Creating a set from a string
    set_from_string = set("hello")
    print(f"Set from string 'hello': {set_from_string}")

def set_add_remove_elements():
    """Demonstrates adding and removing elements from a set."""
    my_set = {1, 2, 3}
    print(f"Initial set: {my_set}")

    # Adding an element
    my_set.add(4)
    print(f"After adding 4: {my_set}")

    # Adding an existing element (no change)
    my_set.add(2)
    print(f"After adding 2 (again): {my_set}")

    # Adding multiple elements using update()
    my_set.update([5, 6, 7])
    print(f"After updating with [5, 6, 7]: {my_set}")

    # Removing an element using remove()
    my_set.remove(3)
    print(f"After removing 3: {my_set}")

    # Trying to remove a non-existent element with remove() raises KeyError
    try:
        my_set.remove(10)
    except KeyError:
        print("KeyError caught when removing non-existent element with remove().")

    # Removing an element using discard()
    my_set.discard(4)
    print(f"After discarding 4: {my_set}")

    # Trying to remove a non-existent element with discard() does nothing
    my_set.discard(10)
    print(f"After discarding 10 (non-existent): {my_set}")

    # Removing and returning an arbitrary element using pop()
    if my_set:
        popped_element = my_set.pop()
        print(f"Popped element: {popped_element}, Set after pop: {my_set}")
    else:
        print("Set is empty, cannot pop.")

    # Clearing all elements
    my_set.clear()
    print(f"After clearing the set: {my_set}")

def set_operations():
    """Demonstrates common set operations."""
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    set_c = {1, 2}

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Set C: {set_c}")

    # Union: elements in either set_a or set_b or both
    union_set = set_a.union(set_b)
    # union_set = set_a | set_b
    print(f"Union (A | B): {union_set}")

    # Intersection: elements common to both set_a and set_b
    intersection_set = set_a.intersection(set_b)
    # intersection_set = set_a & set_b
    print(f"Intersection (A & B): {intersection_set}")

    # Difference: elements in set_a but not in set_b
    difference_set_ab = set_a.difference(set_b)
    # difference_set_ab = set_a - set_b
    print(f"Difference (A - B): {difference_set_ab}")

    # Symmetric Difference: elements in either set_a or set_b but not in both
    symmetric_difference_set = set_a.symmetric_difference(set_b)
    # symmetric_difference_set = set_a ^ set_b
    print(f"Symmetric Difference (A ^ B): {symmetric_difference_set}")

    # Subset check: Is set_c a subset of set_a?
    is_subset = set_c.issubset(set_a)
    # is_subset = set_c <= set_a
    print(f"Is C a subset of A? {is_subset}")

    # Superset check: Is set_a a superset of set_c?
    is_superset = set_a.issuperset(set_c)
    # is_superset = set_a >= set_c
    print(f"Is A a superset of C? {is_superset}")

    # Disjoint check: Do set_a and set_c have no elements in common?
    is_disjoint = set_a.isdisjoint(set_c)
    print(f"Are A and C disjoint? {is_disjoint}")

    is_disjoint_ab = set_a.isdisjoint(set_b)
    print(f"Are A and B disjoint? {is_disjoint_ab}")


if __name__ == '__main__':
    print("--- Set Creation ---")
    set_creation()
    print("\n--- Add/Remove Elements ---")
    set_add_remove_elements()
    print("\n--- Set Operations ---")
    set_operations()
