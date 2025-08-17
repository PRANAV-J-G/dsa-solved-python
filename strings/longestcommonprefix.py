def prefix(strs):
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:

            if i == len(word) or base[i] != word[i]:
                return base[0:i]
    return base

strs = ['flowers','floral']
print(prefix(strs))


print(prefix(strs))
