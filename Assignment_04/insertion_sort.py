def insertion_sort(values):
    """Best Θ(n) when sorted; average/worst Θ(n²) from shifting values.
    Space Θ(n) for the copy, with Θ(1) extra.
    """
    items = list(values)
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current
    return items
