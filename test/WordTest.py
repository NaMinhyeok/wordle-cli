import pytest

from src.Word import Word


def test_word_length_is_exactly_five():
    word = Word("hello")
    assert word.word == "hello"

    with pytest.raises(ValueError):
        Word("hi")


def test_word_only_contains_alphabet():
    word = Word("hello")
    assert word.word == "hello"

    with pytest.raises(ValueError):
        Word("hello123")
    with pytest.raises(ValueError):
        Word("hello!")
    with pytest.raises(ValueError):
        Word("hello ")