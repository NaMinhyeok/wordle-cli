
class Word:
    def __init__(self, word: str):
        if len(word) != 5:
            raise ValueError(f"단어의 글자수는 5만 허용합니다. 하지만 '{word}' 의 길이는 현재 {len(word)} 입니다.")
        if not word.isalpha():
            raise ValueError(f"'{word}' 가 올바르지 않습니다. 오직 알파벳만 입력이 가능합니다.")
        self.word = word
