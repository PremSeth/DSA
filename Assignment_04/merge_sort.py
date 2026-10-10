def merge_sort(values):
    """Best/average/worst Θ(n log n): merge Θ(n) work at each split level.
    Space Θ(n) for the copied and merged lists.
    """
    items = list(values)
    if len(items) < 2:
        return items

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
