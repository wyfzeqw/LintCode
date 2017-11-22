''''
124. Longest Consecutive Sequence 
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Clarification
Your algorithm should run in O(n) complexity.
Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
''''

class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self,num):
        num = list(set(num))
        num.sort()
        length=len(num)

        count=1
        longestLength=1
        currentNumber=num[0]

        for i in range(len(num)):
            if num[i]-currentNumber==1:
                currentNumber=num[i]
                count+=1
                longestLength=max(count,longestLength)

            else:
                currentNumber=num[i]
                count=1

        return longestLength
