# Benchmark

I ran benchmark.py with 3 random matrix pairs at each size. The times are in benchmark_results.csv.

I thought Strassen would be faster, but regular multiplication beat pure Strassen at every size I tried. At size 128, regular took about 186 ms and pure Strassen took about 2802 ms. I feel like making all the smaller matrices takes too much time in Python.

I tried switching to regular multiplication once the pieces got small. At size 256, regular took about 1488 ms. A cutoff of 32 took about 1170 ms, compared with 1254 ms for 64 and 1359 ms for 128. I think 32 is the best cutoff from these runs. At size 64 the two methods were almost tied, and by 128 the hybrid was a little faster.
