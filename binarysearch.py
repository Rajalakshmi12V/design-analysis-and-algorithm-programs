

arr = [5, 10, 15, 20, 25, 30, 35]
target = 25

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Target found at index:", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if low > high:
    print("Target not found")