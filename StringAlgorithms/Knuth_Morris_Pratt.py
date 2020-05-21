def prefixes(string):
    n = len(string)
    table = [0] * n
    i, j = 0, 1
    while j < n:
        if string[i] == string[j]:
            i += 1
            table[j] = i
            j += 1
        else:
            if i > 0:
                i = table[i-1]
            else:
                j += 1
    return table


def kmp(text, pattern):
    n, m = len(text), len(pattern)
    table = prefixes(pattern)
    i, j = 0, 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = table[j-1]
            else:
                i += 1
        if j == m:
            return True
    return False


print(kmp("iojsaditpdadityp", "aditya"))
print(kmp("aiopsaipankopanwarasde", "panwar"))
