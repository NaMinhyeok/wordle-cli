from enum import Enum
from typing import List

from src.Word import Word


class ResultFlag(Enum):
    CORRECT = "🟩"
    PARTIAL = "🟨"
    INCORRECT = "🟥"

class Result:
    def __init__(self, word: Word, flags: List[ResultFlag]):
        if len(flags) != 5:
            raise ValueError("Flags must contain exactly 5 elements.")
        self.word = word
        self.flags = flags

