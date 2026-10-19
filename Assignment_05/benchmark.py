import csv
import random
import statistics
import time
from pathlib import Path

from strassen_matrix import Matrix

sizes = (8, 16, 32, 64, 128, 256)
cutoffs = (1, 8, 16, 32, 64, 128)
trials = 3


def run_benchmarks():
    rng = random.Random(2026)
    results = []
    for size in sizes:
        samples = []
        for _ in range(trials):
            a = Matrix(size, [[rng.randrange(10) for _ in range(size)] for _ in range(size)])
            b = Matrix(size, [[rng.randrange(10) for _ in range(size)] for _ in range(size)])
            samples.append((a, b))

        for cutoff in (0,) + cutoffs:
            if cutoff >= size or (size > 128 and cutoff < 32 and cutoff != 0):
                continue
            name = 'conventional' if cutoff == 0 else f'strassen_{cutoff}'
            times = []
            for a, b in samples:
                start = time.perf_counter()
                if cutoff == 0:
                    result = a.multiply(b)
                else:
                    result = a.strassenMultiply(b, cutoff)
                times.append((time.perf_counter() - start) * 1000)
                if result.data != a.multiply(b).data:
                    raise ValueError(f'{name} returned the wrong result')
            results.append((size, name, statistics.median(times)))

    with Path(__file__).with_name('benchmark_results.csv').open('w', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(('size', 'algorithm', 'median_ms'))
        for size, name, median_ms in results:
            writer.writerow((size, name, f'{median_ms:.4f}'))
    return results


if __name__ == '__main__':
    run_benchmarks()
