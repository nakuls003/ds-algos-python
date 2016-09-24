def binary_search(data, target, low, high):
    """Search for target value in data and if found, return it's index"""

    if low > high:
        return -1
    mid = (low+high)//2
    if target  == data[mid]:
        return mid
    elif target > data[mid]:
        return binary_search(data, target, mid+1, high)
    else:
        return binary_search(data, target, low, mid-1)

if __name__ == '__main__':
    data = input("Enter space separated values in the list(sorted in ascending order):\n ").split()
    target = input("Enter target value to search for:\n ")
    print(binary_search(data, target, 0, len(data)-1))