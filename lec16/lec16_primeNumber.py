def sieve(n):
    candidates = list(range(2,n))
    i = 0  # i: 확인된 소수에 대한 인덱스
    while i < len(candidates):
        prime = candidates[i]
        j = i + 1  # j: 소수임을 확인해야 하는 숫자에 대한 인덱스
        while j < len(candidates):
            if (candidates[j] % prime == 0):
                candidates.pop(j)
            else:
                j = j + 1
        i = i + 1
    return candidates

primeNumber = sieve(26)
print(primeNumber)