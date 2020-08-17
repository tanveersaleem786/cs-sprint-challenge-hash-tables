def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_dict = {}
    result = []
    for num in a:
        num_dict[num] = None
    for num in num_dict:
        if num > 0 and -num in num_dict:
            result.append(num)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))