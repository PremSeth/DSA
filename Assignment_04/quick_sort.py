def quick_sort(values):
    """Best/average Θ(n log n); worst Θ(n²) with uneven partitions.
    Space Θ(n) for the copy; stack Θ(log n) average, Θ(n) worst.
    """
    items = list(values)

    def sort(low, high):
        if low >= high:
            return
        pivot = items[(low + high) // 2]
        left, right = low, high
        while left <= right:
            while items[left] < pivot:
                left += 1
            while items[right] > pivot:
                right -= 1
            if left <= right:
                items[left], items[right] = items[right], items[left]
                left += 1
                right -= 1
        sort(low, right)
        sort(left, high)

    sort(0, len(items) - 1)
    return items
