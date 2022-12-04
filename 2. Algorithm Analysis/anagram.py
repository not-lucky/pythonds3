def check_anagram(s1, s2):
    dic1 = {}
    dic2 = {}
    for i in s1:
        if dic1.get(i) is None:
            dic1[i] = 0
        else:
            dic1[i] += 1

    for i in s2:
        if dic2.get(i) is None:
            dic2[i] = 0
        else:
            dic2[i] += 1

    for k, v in dic1.items():
        if v != dic2.get(k):
            return False
    return True


s1, s2 = map(str, input("Enter 2 strings: ").split())
print(check_anagram(s1, s2))

# print(ord("a"))