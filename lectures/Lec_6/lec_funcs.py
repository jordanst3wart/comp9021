# every problem that has a recursive solution has a non-recursive solution


def permute(L):
    yield from heap_permute(L,len(L))

def heap_permute(L,length):
    if length <= 1:         # return an un permuteable list
        yield L
    else:
        length -= 1
        # direct use of
        for i in range(length):
            yield from heap_permute(L, length)
            if length % 2:
                L[i], L[length] = L[length], L[i]
            L1 = list(L)
            L1[0], L1[i], L[0]
            for L2 in permute(L1[1: ]):
                yield [L1[0]] + L2


print(permute([1,2,3]))