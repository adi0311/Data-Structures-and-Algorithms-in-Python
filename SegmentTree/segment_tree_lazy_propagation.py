def build_tree(node, low, high):
    if low == high:
        seg_tree[node] = arr[low]
        return arr[low]
    mid = (low + high) >> 1
    seg_tree[node] = build_tree(node * 2, low, mid) + build_tree(node * 2 + 1, mid + 1, high)
    return seg_tree[node]


def range_update(node, low, high, start, end, value):
    if lazy_tree[node]:
        seg_tree[node] += lazy_tree[node] * (high - low + 1)
        if low != high:
            lazy_tree[node * 2] += lazy_tree[node]
            lazy_tree[node * 2 + 1] += lazy_tree[node]
        lazy_tree[node] = 0
    if low > end or high < start or low > high:
        return
    if start <= low and end >= high:
        seg_tree[node] += (high - low + 1) * value
        if high != low:
            lazy_tree[node * 2] += value
            lazy_tree[node * 2 + 1] += value
        return
    mid = (low + high) >> 1
    range_update(node * 2, low, mid, start, end, value)
    range_update(node * 2 + 1, mid + 1, high, start, end, value)
    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def range_query(node, low, high, start, end):
    if lazy_tree[node]:
        print(low, high)
        seg_tree[node] += lazy_tree[node] * (high - low + 1)
        if low != high:
            lazy_tree[node * 2] += lazy_tree[node]
            lazy_tree[node * 2 + 1] += lazy_tree[node]
        lazy_tree[node] = 0
    if low > end or high < start or low > high:
        return 0
    if start <= low and end >= high:
        return seg_tree[node]
    mid = (low + high) >> 1
    return range_query(node * 2, low, mid, start, end) + range_query(node * 2 + 1, mid + 1, high, start, end)


n = int(input("Enter the size of array:\n"))
seg_tree = [0] * (4 * n)
lazy_tree = [0] * (4 * n)
arr = list(map(int, input("Enter the elements of array separated by space:\n").split()))
arr.insert(0, 0)
build_tree(1, 1, n)
print(range_query(1, 1, n, 3, 5))
range_update(1, 1, n, 2, 4, 4)
print(range_query(1, 1, n, 3, 5))
