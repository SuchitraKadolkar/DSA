def longestSubArray(arr, k):
    prefixSum = 0
    res = 0
    mp = {}
    for i in range(len(arr)):
        prefixSum += arr[i]

        if prefixSum == k:
            res = i+1
        elif (prefixSum - k) in mp:
            res=max(res, i - mp[prefixSum - k])

        if prefixSum not in mp:
            mp[prefixSum] = i

    return res

l = [int(x) for x in input("Enter array elements: ").split()]
k = int(input("Enter K value: "))

print(longestSubArray(l, k))
