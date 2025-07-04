from src.Result import Result, ResultFlag
from src.Word import Word

class Game:
    def __init__(self, answer: Word, count: int = 0):
        self.count = count
        self.answer = answer

    def guess(self, word: Word) -> Result:
        self.count += 1
        flags = []

        for i, char in enumerate(word.word):
            if char == self.answer.word[i]:
                flags.append(ResultFlag.CORRECT)
            elif char in self.answer.word:
                flags.append(ResultFlag.PARTIAL)
            else:
                flags.append(ResultFlag.INCORRECT)

        return Result(word, flags)


    def isOverCount(self) -> bool:
        return self.count > 5