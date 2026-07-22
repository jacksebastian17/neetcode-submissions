class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            letters[index] += 1
        print(letters)
        for char in t:
            index = ord(char) - ord('a')
            letters[index] -= 1
        return not any(letters)