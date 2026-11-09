# calculates the ith digit of the nth superpermutation
# correct for the first n * (n + 1) - 3 digits
def sp_index(n, i):
    if (i + 2) % (n + 1) == 0:
        return n - 1
    else:
        return (i - (i + 2) // (n + 1)) % (n - 1)

# generates changes between sequential permutations
def generate_superpermutation_chunks(n):
    if n == 1:
        yield (1,)
        return
    
    if n == 2:
        yield (1, 2)
        yield (1,)
        return

    base_perm = [0] * (n-2) + [n - 1, n]
    sp_index_cache = [sp_index(n, i) for i in range(n * (n + 1) - 3)]

    for base_perm_change in generate_superpermutation_chunks(n - 2):
        sp_index_cache_iter = iter(sp_index_cache)
        base_perm[n-2:n-2] = base_perm_change
        base_perm = base_perm[len(base_perm_change):]

        result = [base_perm[next(sp_index_cache_iter)] for _ in range(n - 2)]
        result = result[-1 * len(base_perm_change):]

        for _ in range(n - 1):
            result.append(base_perm[next(sp_index_cache_iter)])
            for _ in range(n):
                result.append(base_perm[next(sp_index_cache_iter)])
                yield tuple(result)
                result = []

# builds the nth superpermutation by joining all superpermutation chunks
def superpermutation(n):
    generator = generate_superpermutation_chunks(n)
    sp = []
    for perm_change in generator:
        sp.extend(perm_change)

    return sp