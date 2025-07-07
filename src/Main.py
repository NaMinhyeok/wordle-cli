from src.Game import Game
from src.Word import Word
from src.Result import ResultFlag

def main() -> None:
    game = Game(Word("apple"))
    
    print("🎯 Wordle CLI에 오신 것을 환영합니다!")
    print(f"{Word.WORD_LENGTH}글자 영단어를 추측하세요. {Game.MAX_ATTEMPTS}번의 시도 기회가 있습니다.")
    print("🟩 = 정확한 위치, 🟨 = 다른 위치에 존재, 🟥 = 존재하지 않음")
    print()

    while True:
        request = input(f"{Word.WORD_LENGTH}글자 영단어를 입력해주세요 (종료하려면 'exit'를 입력해주세요): ").strip().lower()
        
        if request == "exit":
            break
        
        if len(request) == Word.WORD_LENGTH:
            try:
                word = Word(request)
                result = game.guess(word)
                
                print(f"\n시도 {game.count}/{Game.MAX_ATTEMPTS}: {result.word.word.upper()}")
                print("".join(flag.value for flag in result.flags))
                
                if all(flag == ResultFlag.CORRECT for flag in result.flags):
                    print("🎉 정답입니다!")
                    break
                
                if game.is_over_count():
                    print(f"😞 게임 종료! 정답은 {game.answer.word.upper()}였습니다.")
                    break
                
                print()
                    
            except ValueError as e:
                print(f"❌ {e}")
        else:
            print(f"❌ {Word.WORD_LENGTH}글자 영단어를 입력해주세요.")

if __name__ == "__main__":
    main()