# Flatten a list of lists (without libraries).
def flatten_list(nested):
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat

print(flatten_list([[1, 2], [3, 4], [5, 6]]))