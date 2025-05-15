# Writing data to the file
write_data = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(write_data)
print("Data successfully written to output.txt.\n")

# Appending additional data
append_data = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write("\n" + append_data)
print("Data successfully appended.\n")

# Reading and displaying final content
print("Final content of output.txt:")
with open('output.txt', 'r') as file:
    print(file.read())