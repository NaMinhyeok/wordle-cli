from src.Game import Game
from src.Result import ResultFlag
from src.Word import Word


def test_game_initialization():
    game = Game(Word("apple"))

    assert game.count == 0


def test_동일한_위치에_알파벳이_위치하면_해당_index에_Green_emoji로_표시한다():
    game = Game(Word("apple"))
    word = Word("apple")
    result = game.guess(word)

    assert result.flags[0] == ResultFlag.CORRECT
    assert result.flags[1] == ResultFlag.CORRECT
    assert result.flags[2] == ResultFlag.CORRECT
    assert result.flags[3] == ResultFlag.CORRECT
    assert result.flags[4] == ResultFlag.CORRECT


def test_동일한_위치에_알파벳이_존재하지_않아도_전체_단어에_해당_알파벳이_있다면_해당_Index를_Yellow_emoji로_표시한다():
    game = Game(Word("apple"))
    word = Word("peach")

    result = game.guess(word)
    assert result.flags[0] == ResultFlag.PARTIAL
    assert result.flags[1] == ResultFlag.PARTIAL
    assert result.flags[2] == ResultFlag.PARTIAL
    assert result.flags[3] == ResultFlag.INCORRECT
    assert result.flags[4] == ResultFlag.INCORRECT


def test_동일한_위치에_알파벳이_존재하지_않고_전체_단어에_해당_알파벳이_존재하지_않으면_해당_Index를_Red_emoji로_표시한다():
    game = Game(Word("apple"))
    word = Word("query")

    result = game.guess(word)
    assert result.flags[0] == ResultFlag.INCORRECT
    assert result.flags[1] == ResultFlag.INCORRECT
    assert result.flags[2] == ResultFlag.PARTIAL
    assert result.flags[3] == ResultFlag.INCORRECT
    assert result.flags[4] == ResultFlag.INCORRECT


def test_is_over_count():
    game = Game(Word("apple"))
    
    for _ in range(Game.MAX_ATTEMPTS):
        game.guess(Word("wrong"))
    
    assert game.is_over_count() == True