def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    total_arrays = len(arrays)
    numbers_dict = {}
    result = []
    for array in arrays:
        for num in array:
            numbers_dict[num] = 1 if num not in numbers_dict else numbers_dict[num] + 1

               
    for (num, num_occurrence) in numbers_dict.items():
        if num_occurrence == total_arrays:
            result.append(num)
    return result

if __name__ == "__main__":
    arrays = []
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    print(intersection(arrays))
