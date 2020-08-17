def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_dict = {}
    for (index, weight) in enumerate(weights):
        weights_dict[weight] = index
    for index, weight in enumerate(weights):
        find_weight = limit - weight
        if find_weight in weights_dict:
            if index > weights_dict[find_weight]:
                return (index, weights_dict[find_weight])
            else:
                return (weights_dict[find_weight], index)
    return None