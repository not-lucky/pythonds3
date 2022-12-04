def sum(lis):
    if len(lis) == 1:
        return lis[0]
    return sum(lis[0]) + sum(lis[1:])
