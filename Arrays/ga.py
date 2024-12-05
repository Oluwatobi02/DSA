from collections import defaultdict

def anagrams(lst):
    hm = defaultdict(list)
    for word in lst:
        word_anagram = [0] * 26
        for i in word:
            word_anagram[ord(i) - ord('a')] +=1
        tup = tuple(word_anagram)
        hm[tup].append(word)
        
    return hm.values()


words = ['eat', 'tan', 'ate', 'nat', 'bat']

print(anagrams(words))