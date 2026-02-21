from collections import Counter

a = "hello"

print(Counter(a))

def counter(s):
    count = {}
    for i in range(len(s)):
        count[s[i]] = count.get(s[i], 0) + 1
    return count

print(counter(a))