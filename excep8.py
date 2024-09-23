def value_processing():


    try:
        user_input = input("Enter cortege of elements:")
        num_list = [int(num.strip()) for num in user_input.split(',')]
        print(f" List of numbers{num_list}")
        return num_list
    except ValueError:
        print("Error: incorrect input of numbers or entered values contain non-integer numbers.")
        return None


def exception_handling(lst: [list]):


    try:
        index = int(input("Enter index of the number you want to get:"))
        element = lst[index]
        print(f"Element on index {index}: {element}")
    except IndexError:
        print(f"Error: value by index {index} goes beyond the list.")
    except ValueError:
        print("Error: index must be an integer!")


num_list = value_processing()
if num_list is not None:
    exception_handling(num_list)
