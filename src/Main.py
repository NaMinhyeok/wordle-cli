from src.Word import Word

while(True):
    request = input("5글자 영단어를 입력해주세요 (종료하려면 'exit'를 입력해주세요): ").strip().lower()
    count: int = 0
    if(request == "exit"):
        break
    if(len(request) == 5):
        # TODO: Game Logic in Heere
        word = Word(request)
        print("Processing request:", word.word)
        count += 1
    else:
        print("Invalid request format. Please provide exactly 5 elements.")
        continue