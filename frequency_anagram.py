def validAnagram(first, second):
    if len(first) != len(second):
        return False

    lookup = {}

    for i in first:
        # lookup[i] += 1 if i in lookup else lookup[i] = 1
        if i in lookup:
            lookup[i] += 1 
        else: 
            lookup[i] = 1

    for i in second:
        if i not in lookup:
            return False
        else:
            lookup[i] -=1
    return True

print(validAnagram('anargam', 'nagaram'))