def compare_tuple_elements(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        print("Tuples have different lengths.")
        return

    for elem1, elem2 in zip(tuple1, tuple2):
        if elem1 == elem2:
            print(f"Element {elem1} is equal to {elem2}")
        else:
            print(f"Element {elem1} is not equal to {elem2}")

# Example usage
tuple_a = (1, 2, 3, 4)
tuple_b = (1, 2, 5, 4)

compare_tuple_elements(tuple_a, tuple_b)