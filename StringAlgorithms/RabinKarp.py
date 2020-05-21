mod = pow(10, 9)+7
match = dict()
for i in range(26):
    match[chr(i+97)] = i+1


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if n < m:
        return False
    hash_pattern = 0
    i = 0
    for p in pattern[::-1]:
        hash_pattern = (hash_pattern + pow(26, i, mod) * match[p]) % mod
        i += 1
    hash_window = 0
    i = 0
    for t in text[:m][::-1]:
        hash_window = (hash_window + pow(26, i, mod) * match[t]) % mod
        i += 1
    i = m-1
    while i < n:
        if hash_pattern == hash_window:
            j, k = i-m+1, 0
            r = True
            while k < m:
                if pattern[k] != text[j]:
                    r = False
                    break
                j += 1
                k += 1
            if r:
                return r
        hash_window = (hash_window - pow(26, m-1, mod) * match[text[i-m+1]] + mod) % mod
        i += 1
        if i < n:
            hash_window = (hash_window * 26) % mod
            hash_window = (hash_window + match[text[i]]) % mod
    return False


print(rabin_karp("opaospanwapaosopanwarlosj", "panwar"))
