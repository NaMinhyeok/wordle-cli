from enum import Enum
from typing import List

from src.Word import Word


class ResultFlag(Enum):
    CORRECT = "🟩"
    PARTIAL = "🟨"
    INCORRECT = "🟥"

class Result:
    def __init__(self, word: Word, flags: List[ResultFlag]) -> None:
        if len(flags) != Word.WORD_LENGTH:
            raise ValueError(f"Flags must contain exactly {Word.WORD_LENGTH} elements.")
        self.word = word
        self.flags = flags

