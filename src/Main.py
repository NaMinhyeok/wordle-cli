from src.Game import Game
from src.Word import Word
from src.Result import ResultFlag

game = Game(Word("apple"))

print("🎯 Wordle CLI에 오신 것을 환영합니다!")
print("5글자 영단어를 추측하세요. 6번의 시도 기회가 있습니다.")
print("🟩 = 정확한 위치, 🟨 = 다른 위치에 존재, 🟥 = 존재하지 않음")
print()

while True:
    request = input("5글자 영단어를 입력해주세요 (종료하려면 'exit'를 입력해주세요): ").strip().lower()
    
    if request == "exit":
        break
    
    if len(request) == 5:
        try:
            word = Word(request)
            result = game.guess(word)
            
            # 결과 출력
            print(f"\n시도 {game.count}/6: {result.word.word.upper()}")
            print("".join([flag.value for flag in result.flags]))
            
            # 정답 확인
            if all(flag == ResultFlag.CORRECT for flag in result.flags):
                print("🎉 정답입니다!")
                break
            
            # 기회 확인
            if game.isOverCount():
                print(f"😞 게임 종료! 정답은 {game.answer.word.upper()}였습니다.")
                break
            
            print()
                
        except ValueError as e:
            print(f"❌ {e}")
    else:
        print("❌ 5글자 영단어를 입력해주세요.")