# 1768. Merge Strings Alternately
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# solution
# We have two strings and we want to return and merge it in such a way that we take one of each of each until we append the  last part of the longer sting if need.
# we are going to create an empty string that takes in the answer
# we are now going to compare both strings to know which has the longer length
# traverse and do not exceed the max length
# if i is  less than length of the first string return result += extra letters
# if i is less than length of the second string return result += extra letters


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        max_length= max(len(word1), len(word2))
        for i in range(max_length):
            if i < len(word1):
                result += word1[i] 
            if i < len(word2):
                result += word2[i]
        return result 
        
