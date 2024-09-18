filename = "test.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: file '{filename}' not founded.")
