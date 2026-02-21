from collections import Counter


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    x = [] 
    seen = []
    for i in range(len(strs)):
        if seen.__contains__(strs[i]) == True:
            continue
        x.append([])
        for j in range(i, len(strs)):
            if i == j and seen.__contains__(strs[j]) == False:
                x[-1].append(strs[i])
                seen.append(strs[i])

            elif Counter(s) == Counter(t) and seen.__contains__(strs[j]) == False:
                x[-1].append(strs[j])
                seen.append(strs[j])
            
                
    return x

strs = ["a"]
print(groupAnagrams(strs))
