try:
    with open('sample.txt', 'r') as file:
        print("reading the file content:")
        for line_number, line in enumerate(file, 1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file sample.txt was not found.")




