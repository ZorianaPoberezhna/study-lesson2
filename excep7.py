def exception_handling(lst: list, index: int):


    try:
        element = lst[index]
        print(f"Element on index {index}: {element}")
    except IndexError:
        print(f"Error: value by index {index} goes beyond the list.")


my_list =  [1, 2, 3, 4, 5, 6]

exception_handling(my_list, 6)
