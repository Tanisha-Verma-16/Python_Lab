def count_elements_in_range(input_list, start_range, end_range):
    count = 0
    for element in input_list:
        if start_range <= element <= end_range:
            count += 1
    return count

# Example usage
my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
start_range = 3
end_range = 7

result = count_elements_in_range(my_list, start_range, end_range)

print(f"The number of elements in the range [{start_range}, {end_range}] is: {result}")
