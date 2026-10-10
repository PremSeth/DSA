# Sorting benchmarks

I tested the four sorts on lists of 10, 100, 1,000, and 10,000 numbers. I made three random lists for each size using seed 2026, with numbers from 0 to 99,999. I also made three new lists and sorted them first to see what happens when the input is already in order. Every algorithm got the same lists. I used `time.perf_counter()` and took the median of the three runs in milliseconds. I only timed the sort itself, including the copy each function makes. I checked the answers afterward.

| Input | Size | Insertion | Selection | Merge | Quick |
| --- | ---: | ---: | ---: | ---: | ---: |
| Random | 10 | 0.0060 | 0.0062 | 0.0127 | 0.0071 |
| Random | 100 | 0.1877 | 0.1876 | 0.1584 | 0.0799 |
| Random | 1,000 | 21.5812 | 21.9279 | 1.4732 | 0.8456 |
| Random | 10,000 | 1527.0180 | 1511.2177 | 15.2318 | 9.3764 |
| Sorted | 10 | 0.0016 | 0.0045 | 0.0090 | 0.0039 |
| Sorted | 100 | 0.0092 | 0.1703 | 0.1152 | 0.0430 |
| Sorted | 1,000 | 0.0866 | 18.0625 | 1.0307 | 0.4421 |
| Sorted | 10,000 | 0.7950 | 1546.3967 | 10.7199 | 5.0306 |

Quick sort was the fastest on random lists once the size got past 10, and merge sort was next. The difference got pretty big at 10,000 values: insertion and selection each took about 1.5 seconds, while quick sort took about 9 ms. The interesting thing with sorted lists was insertion sort. It was the fastest because it barely had to move anything. Selection sort stayed slow because it still checked the rest of the list each time. The times for 10 values are very small, so I would not draw much from those alone.

