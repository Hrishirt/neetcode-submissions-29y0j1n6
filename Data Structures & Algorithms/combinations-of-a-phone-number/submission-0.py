class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", 
        "8": "tuv", "9": "wxyz"}
        letters = []
        for digit in digits: 
            letters.append(numToLetter[digit])
        print(letters)
        output = []
        comb = []
        if not digits:
            return [] 
        def backtrack(i): 
            if i >= len(digits):
                output.append("".join(comb))
                return 

            currChar = letters[i]
            for letter in currChar:
                comb.append(letter)
                backtrack(i + 1)
                comb.pop()
        
        backtrack(0)
        return output

