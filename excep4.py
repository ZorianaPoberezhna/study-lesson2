file1_path = input("Enter the path to the first file: ")
file2_path = input("Enter the path to the second file: ")

with open(file1_path, 'r') as file1:
    lines_file1 = file1.readlines()

with open(file2_path, 'r') as file2:
    lines_file2 = file2.readlines()

lines_file1 = [line.strip() for line in lines_file1]
lines_file2 = [line.strip() for line in lines_file2]

unique_lines = [line for line in lines_file1 if line not in lines_file2]

if unique_lines:
    print("Lines that are present in the first file but not in the second:")
    for line in unique_lines:
        print(line)
else:
    print("All lines from the first file are in the second file.")
