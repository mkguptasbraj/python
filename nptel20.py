def remdup(l):
    """
    Removes duplicates from a list, keeping only the first occurrence of each number.

    Args:
    l (list): A nonempty list of integers.

    Returns:
    list: A new list with duplicates removed.
    """
    seen = set()
    result = []
    for num in l:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
print(remdup([1,2,2,3,3,45,5,5]))
print(remdup([1,1,12,2,3,32,2,2,3,5,4,6,7,7,8]))