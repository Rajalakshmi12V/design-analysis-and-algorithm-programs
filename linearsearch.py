

arr = [10, 25, 30, 45, 50, 65, 80]
target = 50

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")