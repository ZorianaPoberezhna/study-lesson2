def file_recording(file1: str):


    user_input = input("Enter text:")

    with open(file1, 'w') as file:
        file.write(user_input)
    print(f"Your text in {file1}")
    file.close()


file_recording("file1.txt")
