import re

def filter(s: str) -> str:
    sf = re.sub('[^a-zA-Z0-9]', '', s)
    return sf.lower()

def isPalindrome(s: str) -> bool:
    s = filter(s)
    ptr1 = 0
    ptr2 = len(s) - 1
    while ptr1 <= ptr2:
        if s[ptr1] == s[ptr2]:
            ptr1 += 1
            ptr2 -= 1
        else: return False

    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))