from src.Result import Result, ResultFlag
from src.Word import Word

class Game:
    MAX_ATTEMPTS = 6
    
    def __init__(self, answer: Word, count: int = 0) -> None:
        self.count = count
        self.answer = answer

    def guess(self, word: Word) -> Result:
        self.count += 1
        flags = [
            ResultFlag.CORRECT if char == self.answer.word[i]
            else ResultFlag.PARTIAL if char in self.answer.word
            else ResultFlag.INCORRECT
            for i, char in enumerate(word.word)
        ]
        return Result(word, flags)

    def is_over_count(self) -> bool:
        return self.count >= self.MAX_ATTEMPTS