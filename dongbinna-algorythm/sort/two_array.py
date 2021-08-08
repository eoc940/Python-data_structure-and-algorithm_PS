# 두 배열의 원소 교체

import sys

n,k = map(int, sys.stdin.readline().split())
arr_a = list(map(int, sys.stdin.readline().split()))
arr_b = list(map(int ,sys.stdin.readline().split()))

arr_a.sort()
arr_b.sort(reverse=True)

slice_a = arr_a[:k]
slice_b = arr_b[:k]
arr_a[:k] = slice_b
arr_b[:k] = slice_a

print(sum(arr_a))
