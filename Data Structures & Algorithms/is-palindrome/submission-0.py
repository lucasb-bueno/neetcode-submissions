class Solution:
    # not case sensitive (just puting everything in lowercase)
    # just normal characters

    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in s.lower():
            if i != ' ' and i.isalnum() == True:
                new_string += i
        print(new_string)

        if new_string == new_string[::-1]:
            return True
        
        return False