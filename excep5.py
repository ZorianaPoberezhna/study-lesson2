source_file_path = input("Enter the path to the file you want to copy: ")
destination_file_path = input("Enter the path to the file where you want to paste the copy: ")

with open(source_file_path, 'r', encoding='utf-8') as source_file:
    content = source_file.read()

with open(destination_file_path, 'w', encoding='utf-8') as destination_file:
    destination_file.write(content)

print(f"The contents of the file {source_file_path} successfully copied to {destination_file_path}.")