"""
Problem Statement: Given N and K, where N is the sequence of numbers from 1 to N([1,2,3….. N]) 
find the Kth permutation sequence.
For N = 3  the 3!  Permutation sequences in order would look like this:-
Note: 1<=K<=N! Hence for a given input its Kth permutation always exists


Example 1:

Input: N = 3, K = 3
Output: “213”
Explanation: The sequence has 3! permutations as illustrated in the figure above. K = 3 corresponds to the third sequence.

Example 2:

Input: N = 3, K = 5 
Result: “312”
Explanation: The sequence has 3! permutations as illustrated in the figure above. K = 5 corresponds to the fifth sequence.
"""

from math import factorial

def kth_permutation_sequence(n, k):
    chars=[]
    for i in range(n):
        chars.append(str(i+1))
    
    def fun(chars,target,length):
        p=[]
        fact=factorial(length)
        while (chars!=[]): 
            fact = fact//length
            i = target // fact
            target = target % fact
            x=chars[i]
            p.append(x)
            chars=chars[:i]+chars[i+1:]
            length-=1
        return "".join(p)
    
    return fun(chars,k-1,n)

print(kth_permutation_sequence(4,15))