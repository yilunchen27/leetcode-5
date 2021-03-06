
# You are given an array A of strings.

# Two strings S and T are special-equivalent if after any number of moves, S == T.

# A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

# Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

# Return the number of groups of special-equivalent strings from A.



# Example 1:

# Input: ["a","b","c","a","c","c"]
# Output: 3
# Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
# Example 2:

# Input: ["aa","bb","ab","ba"]
# Output: 4
# Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
# Example 3:

# Input: ["abc","acb","bac","bca","cab","cba"]
# Output: 3
# Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
# Example 4:

# Input: ["abcd","cdab","adcb","cbad"]
# Output: 1
# Explanation: 1 group ["abcd","cdab","adcb","cbad"]


# Note:

# 1 <= A.length <= 1000
# 1 <= A[i].length <= 20
# All A[i] have the same length.
# All A[i] consist of only lowercase letters.

# https://leetcode.com/problems/groups-of-special-equivalent-strings/description/
# 1) using set, O(M*Nlog(N)), where M is no.of elements in the input list and N is the length of string
# NlogN is the sorted time complexity
# the idea is "abcd" and "cdab" are the same group as cdab sorted by odd and even gives "abcd"
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = set()
        # sorted the odd char and even char and append to the set
        # e.g. "abcd" --> (ac, bd), "cbad" --> (ac,bd) same set
        for word in A:
            even = ''.join(sorted(str(word[0::2])))
            odd = ''.join(sorted(str(word[1::2])))
            # does not matter (odd,even) or (even odd)
            d.add((odd,even))

        return len(d)

# 2) variant using default dictionary
import collections
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # The difference is that a defaultdict will "default" a value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
        d = collections.defaultdict(int)
        # sorted the odd char and even char and append to the set
        # e.g. "abcd" --> (ac, bd), "cbad" --> (ac,bd) same set
        for word in A:
            even = ''.join(sorted(str(word[0::2])))
            odd = ''.join(sorted(str(word[1::2])))
            # does not matter (odd,even) or (even odd)
            d[(odd,even)] += 1

        return len(d)


# 3) build a separate function "count" to update the count, tuple(ans) returns a tuple with character and no.of occurence mappings through a list with size 52 (26*2)
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                # separate odd and even index char, hence the list has 52 places
                # special-equivalent strings will generate same list as permutation between either odd or even indexed char
                # 26 * (i%2) to calculate index for even and odd
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)
        # use of set {}, same tuple will be counted as 1 only
        return len({count(word) for word in A})


# 4) one-liner, variant of 2)
class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len({tuple(sorted(word[0::2]) + sorted(word[1::2])) for word in A})


# 5) using dictionary to store the key, return length of the dictionary
class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = dict()
        for i in A:
            if len(i) >= 2:
                key = (tuple(sorted(i[::2])), tuple(sorted(i[1::2])))
                d[key] = d.get(key,0) + 1
            else:
                d[i] = d.get(i,0) + 1

        return len(d)
