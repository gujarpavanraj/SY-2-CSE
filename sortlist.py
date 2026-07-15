numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

numbers.sort()

print("Ascending Order:", numbers)