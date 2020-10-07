def prime_factors(number):
    answer = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            cnt = 0
            while number % i == 0:
                cnt += 1
                number //= i
            answer.append([i, cnt])
        i += 1
    if number > 1:
        answer.append([number, 1])
    return answer


n = int(input())
print(prime_factors(n))
