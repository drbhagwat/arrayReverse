# initialize the array with no elements
numbers = []

# maximum number of elements that can be stored in the array
MAX_ELEMENTS = 100000

def get_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Please enter a number >= {minimum}")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number <= {maximum}")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted. Exiting program.")
            raise

def swap(data, i, j) :
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

def reverse(data) :
    left = 0
    right = len(data) - 1

    while left < right :
        swap(data, left, right)
        left = left + 1
        right = right -1