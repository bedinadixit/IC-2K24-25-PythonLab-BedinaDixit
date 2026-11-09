
import time
import random


# Naive Approach
def kth_smallest_naive(arr, K):
    sums = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            sums.append(arr[i] + arr[j])

    sums.sort()

    return sums[K - 1]


# Optimized Approach
def count_pairs(arr, value):
    count = 0
    j = len(arr) - 1

    for i in range(len(arr)):
        while i < j and arr[i] + arr[j] > value:
            j -= 1

        if j > i:
            count += j - i

    return count


def kth_smallest_optimized(arr, K):
    arr.sort()

    low = arr[0] + arr[1]
    high = arr[-2] + arr[-1]

    while low < high:
        mid = (low + high) // 2

        if count_pairs(arr, mid) >= K:
            high = mid
        else:
            low = mid + 1

    return low


# Correctness Testing
print("Naive Approach:")
print(kth_smallest_naive([1, 3, 5, 7], 1))
print(kth_smallest_naive([1, 3, 5, 7], 3))
print(kth_smallest_naive([1, 3, 5, 7], 6))
print(kth_smallest_naive([4, 4, 4], 1))
print(kth_smallest_naive([2, 5, 10], 2))


print("Optimized Approach:")
print(kth_smallest_optimized([1, 3, 5, 7], 1))
print(kth_smallest_optimized([1, 3, 5, 7], 3))
print(kth_smallest_optimized([1, 3, 5, 7], 6))
print(kth_smallest_optimized([4, 4, 4], 1))
print(kth_smallest_optimized([2, 5, 10], 2))


# Performance Testing
random.seed(42)

N = 5000
arr = [random.randint(1, 100000) for _ in range(N)]
K = 1000000

# Optimized timing
start = time.time()
result = kth_smallest_optimized(arr.copy(), K)
end = time.time()

print("Optimized Result:", result)
print("Optimized Time:", end - start)


# Naive timing (memory intensive)
start = time.time()
result = kth_smallest_naive(arr.copy(), K)
end = time.time()

print("Naive Result:", result)
print("Naive Time:", end - start)
