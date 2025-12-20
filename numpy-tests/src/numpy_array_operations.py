import numpy as np

if __name__ == '__main__':
    arr = np.array([1, 2, 3, 4, 5])

    print(arr + 10)
    print(arr * 2)
    print(arr ** 2)


    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(a + b)
    print(a * b)

    # filtering
    print(arr[arr > 3])


    print(np.sum(arr))
    print(np.mean(arr))
    print(np.max(arr))
    print(np.min(arr))
    print(np.sort(arr))