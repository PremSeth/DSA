import csv
import random
import statistics
import time
from pathlib import Path

from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

sorts = (insertion_sort, selection_sort, merge_sort, quick_sort)
sizes = (10, 100, 1000, 10000)
trials = 3


def run_benchmarks():
    rng = random.Random(2026)
    results = []
    for size in sizes:
        for order in ('random', 'sorted'):
            samples = []
            for _ in range(trials):
                values = [rng.randrange(100000) for _ in range(size)]
                if order == 'sorted':
                    values.sort()
                samples.append(values)

            for sort in sorts:
                times = []
                for values in samples:
                    start = time.perf_counter()
                    result = sort(values)
                    times.append((time.perf_counter() - start) * 1000)
                    if result != sorted(values):
                        raise ValueError(f'{sort.__name__} returned the wrong result')
                results.append((order, size, sort.__name__, statistics.median(times)))

    output = Path(__file__).with_name('benchmark_results.csv')
    with output.open('w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('order', 'size', 'algorithm', 'median_ms'))
        for order, size, name, median_ms in results:
            writer.writerow((order, size, name, f'{median_ms:.4f}'))
    return results


if __name__ == '__main__':
    run_benchmarks()
