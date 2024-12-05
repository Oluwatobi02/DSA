


def get_last_odd(arr):
    if len(arr) == 0: return 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] %2 == 1:
            return arr[i]

    return 0

print(get_last_odd([8,6,5,6,7]))