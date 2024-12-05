from collections import Counter, deque
arr = [9,2,9,2,4,4,4,4,6,3,2,5,6,7,8,9]
def klargestoccurences(arr, k,result=[],bucket=[0] * len(arr), hm=Counter(arr)):
    for i in hm:
        if bucket[hm[i]]:bucket[hm[i]].append(i)
        else:bucket[hm[i]] = [i]
    for i in range(len(bucket)-1,-1,-1):
        if len(result) == k:return result
        if bucket[i]:result.extend(bucket[i])
        

print(klargestoccurences(arr, 3))

