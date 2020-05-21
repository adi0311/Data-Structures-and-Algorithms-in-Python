from collections import defaultdict as dd


def update(index, value):
    while index <= n:
        fenwick[index] += value
        index += index & -index


def query(index):
    answer = 0
    while index:
        answer += fenwick[index]
        index -= index & -index
    return answer


arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
fenwick = dd(int)
for i in range(n):
    update(i+1, arr[i])
print(query(3))
print(query(6))
update(3, 6)
print(query(3))
print(query(6))
from collections import defaultdict as dd


def update(index, value):
    while index <= n:
        fenwick[index] += value
        index += index & -index


def query(index):
    answer = 0
    while index:
        answer += fenwick[index]
        index -= index & -index
    return answer


arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
fenwick = dd(int)
for i in range(n):
    update(i+1, arr[i])
print(query(3))
print(query(6))
update(3, 6)
print(query(3))
print(query(6))
