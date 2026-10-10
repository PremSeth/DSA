def selection_sort(values):
    """Best/average/worst Θ(n²): it scans the remaining items each time.
    Space Θ(n) for the copy, with Θ(1) extra.
    """
    items = list(values)
    for i in range(len(items)):
        smallest = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
    return items
