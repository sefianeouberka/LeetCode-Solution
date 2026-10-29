class Solution:
    def plusOne(self, digits: list[int]) -> list[int]: 
        # liste = [int(i) for i in str(digits[-1] + 1)]
        # digits = digits[:-1] + liste
        # return digits
        number = int("".join(map(str, digits)))
        somme = number + 1
        digits = [int(i) for i in str(somme)]
        return digits





