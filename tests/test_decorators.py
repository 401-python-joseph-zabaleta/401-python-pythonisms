import pytest

from pythonisms.decorators import (
    emphasize,
    sarcastic,
    reverse_letters,
)

def test_original_function():
    def proclaim(txt):
        return txt
    actual = proclaim('test')
    expected = 'test'
    assert actual == expected

def test_emphasize():
    @emphasize
    def proclaim(txt):
        return txt

    actual = proclaim('test')
    expected = 'TEST!!!'
    assert actual == expected

def test_sarcastic():
    @sarcastic
    def proclaim(txt):
        return txt

    actual = proclaim('test')
    expected = 'testtest'

def test_reverse_letters():
    @reverse_letters
    def proclaim(txt):
        return txt

    actual = proclaim('12345')
    expected = '54321'
    
    assert actual == expected