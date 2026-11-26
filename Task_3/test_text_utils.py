from text_utils import is_palindrome

def test_topot():
    assert is_palindrome('топот') == True

def test_Topot():
    assert is_palindrome('Топот') == True

def test_python():
    assert is_palindrome('python') == False

def test_A():
    assert is_palindrome('A') == True