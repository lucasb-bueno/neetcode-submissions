class Solution:

    """"
    notes:
    - two arrays with 26 size filled up with zeros
    - iterate through each of those
    - check value from ord(s) - ord('a') and add it into the respective
    index in array, sum +1 to that index
    - return arrA == arrB

    """

    def isAnagram(self, s: str, t: str) -> bool:
        arrS = [0] * 26
        arrT = [0] * 26

        for i in s:
            index = ord(i) - ord("a")
            arrS[index] += 1

        for i in t:
            index = ord(i) - ord("a")
            arrT[index] += 1

        print(f"s: {arrS}, t: {arrT}")

        return arrS == arrT 