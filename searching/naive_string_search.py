def naiveSearch(long, short):
    count = 0
    for i in range(len(long)):
        for j in range(len(short)):
            print(long[i+j], short[j])
            if short[j] != long[i+j]:
                print('BREAK')
                break
            if j == len(short) -1:
                print('FOUND U!')
                count +=1
    return count

print(naiveSearch('lorie loledlol', 'lol'))