# Rotate a list to the right by k positions
lst = [1, 2, 3, 4, 5]
k = 2

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]

print("Rotated list:", rotated)