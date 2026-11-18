from src import username, email, handle, is_valid_username
import pytest


def test_username_input(monkeypatch):
    # 1. We tell monkeypatch to replace 'input' with a function that returns 'alice123'
    monkeypatch.setattr('builtins.input', lambda _: 'alice123')
    
    # 2. We call our function. Even though it has an input() inside it, 
    # Python won't freeze—it instantly receives 'alice123'!
    result = username()
    
    # 3. We check if our function handled or returned it correctly
    assert is_valid_username(result) == True

# A list of banned words we want to test
@pytest.mark.parametrize("bad_word", ["admin", "root", "moderator", "mod", "null"])
def test_username_banned_words(bad_word):
    # Pytest runs this test 5 times automatically, once for each word in the list!
    assert is_valid_username(bad_word) == False


