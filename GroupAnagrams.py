from collections import Counter

def findAnagram(s: str, t: str):
    return Counter(s) == Counter(t)


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    x = [[]]
    seen = set()
    for i in range(len(strs)):
        index = 0
        for j in range(i, len(strs)):
            if i == j:
                seen.add(strs[i])
                x[i][index].append(strs[i])
                index += 1

            elif findAnagram(strs[i], strs[j]) and seen.__contains__(strs[i]) == False:
                x[i][index].append(strs[i])
                index += 1
                seen.add(strs[i])
    return x

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))
