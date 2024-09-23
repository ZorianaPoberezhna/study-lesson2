def count_words_in_file(filename: str):


    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The number of words in the file: {word_count}")
    except FileNotFoundError:
        print(f"Error: file '{filename}' not founded.")
    except Exception as e:
        print(f"Error: {e}")


filename = "file1.txt"
count_words_in_file(filename)