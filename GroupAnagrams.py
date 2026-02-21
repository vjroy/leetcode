from collections import Counter


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    x = [] 
    seen = []
    for i in range(len(strs)):
        if seen.__contains__(i) == True:
            continue
        x.append([])
        for j in range(i, len(strs)):
            if i == j and seen.__contains__(j) == False:
                x[-1].append(strs[i])
                seen.append(i)

            elif Counter(strs[i]) == Counter(strs[j]) and seen.__contains__(j) == False:
                x[-1].append(strs[j])
                seen.append(j)
            
                
    return x


strs = ["ab", "ba", "ab"]
print(groupAnagrams(strs))
