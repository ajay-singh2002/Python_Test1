# Merge two dictionaries into one without using update().
def merge_dicts(d1, d2):
    merged = {}
    for key in d1:
        merged[key] = d1[key]
    for key in d2:
        merged[key] = d2[key]
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))