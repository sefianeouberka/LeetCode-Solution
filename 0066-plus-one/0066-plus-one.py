class Solution:
    def plusOne(self, digits: list[int]) -> list[int]: 
        number = int("".join(map(str, digits)))
        somme = number + 1
        digits = [int(i) for i in str(somme)]
        return digits





