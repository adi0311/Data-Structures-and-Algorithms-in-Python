# Remainders
rem = [1, 4, 6]

# Divisors(Co - prime i.e. their gcd should be 1)
mods = [3, 5, 7]

# Product of all divisors.
N = 1
for i in mods:
    N *= i

# Product of all divisors except current divisor.
Ns = [N // i for i in mods]

# Inverse of Ns w.r.t to mods.
inv = [pow(Ns[i], mods[i]-2, mods[i]) for i in range(3)]

# Given number will be answer % N.
answer = 0
for i in range(3):
    answer += inv[i] * Ns[i] * rem[i]
print(answer % N)
