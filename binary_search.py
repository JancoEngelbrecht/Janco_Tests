# Naive search: scan entire list and ask if its equal to the target

# if yes, return the index
# if no, return then return -1

l = [1, 2, 3]


def naive(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -i


print(naive(l, 1))

def binary_search(l, target, low=None, high=None):
    