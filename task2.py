import json

def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        mid_value = sorted_array[mid]

        if mid_value < target:
            left = mid + 1
        else:
            upper_bound = mid_value
            right = mid - 1

    return (iterations, upper_bound)

if __name__ == "__main__":
    with open('./data/task2.json', 'r') as file:
        array = json.load(file)

        min_value = min(array)
        max_value = max(array)

        bound_element = float(input(f"Enter bound element in [{min_value}...{max_value}]: "))

        if min_value <= bound_element <= max_value:
            iterations, upper_bound = binary_search(array, bound_element)
            print(f"Number of iterations: {iterations}")

            if upper_bound is not None:
                print(f"Upper bound for {bound_element} is {upper_bound}")
            else:
                print(f"No upper bound found for {bound_element} in the array.")
        else:
            print("The bound element is out of the range of the array.")


        