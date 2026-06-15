class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ''.join(char for char in s if char.isalnum())
        left = 0
        right = len(string) - 1
        while left <= right:
            if string[left] != string[right]:
                return False
            else:
                right -= 1
                left += 1

        return True