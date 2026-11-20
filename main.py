import array_utils

def main():
    number_of_elements = array_utils.get_integer(
        "Please give the number of elements to be stored: ",
        minimum=1,
        maximum=array_utils.MAX_ELEMENTS,
    )

    for i in range(number_of_elements):
        element = array_utils.get_integer(f"Please enter number {i + 1}: ")
        array_utils.numbers.append(element)

    print("\nNumber of elements:", number_of_elements)
    print("Array:", array_utils.numbers)
    array_utils.reverse(array_utils.numbers)
    print("Reversed Array:", array_utils.numbers)

try:
    main()

except (KeyboardInterrupt, EOFError):
    pass

except Exception as e:
    print("Unexpected error:", e)