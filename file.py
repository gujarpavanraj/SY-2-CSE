file = open("sample.txt", "w")

data = input("Enter text to write into the file: ")

file.write(data)

file.close()

print("Data written successfully.")