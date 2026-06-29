# Initialize the array
arr = [10, 12, 14, 16, 8, 6, 4]

print("Original Array:", arr)

print("\nPress:")
print("1 - Ascending Order")
print("2 - Descending Order")

choice = input("Enter your choice: ")

if choice == "1":
    arr.sort()
    print("Ascending Order:", arr)

elif choice == "2":
    arr.sort(reverse=True)
    print("Descending Order:", arr)

else:
    print("Invalid Choice!")