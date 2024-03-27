import unittest

def is_palindrome(mystring):
    if mystring == mystring[::-1]:
        return True
    else:
        return False

class TestPalindrome(unittest.TestCase):
    def test_a (self):
        resultado = is_palindrome('a')
        self.assertEqual (resultado, True)
    
    def test_aa (self):
        resultado = is_palindrome('aa')
        self.assertEqual (resultado, True)
    
    def test_ab (self):
        resultado = is_palindrome('ab')
        self.assertEqual (resultado, False)
    def test_aCa (self):
        resultado = is_palindrome('aCa')
        self.assertEqual (resultado, True)
    def test_aCs (self):
        resultado = is_palindrome('aCs')
        self.assertEqual (resultado, False)    

    def test_ABCA (self):
        resultado = is_palindrome('ABCA')
        self.assertEqual (resultado, False)

    def test_ABCBA (self):
        resultado = is_palindrome('ABCBA')
        self.assertEqual (resultado, True)

    def test_ABCCBA (self):
        resultado = is_palindrome('ABCCBA')
        self.assertEqual (resultado, True)

    def test_neuquen (self):
        resultado = is_palindrome('neuquen')
        self.assertEqual (resultado, True)

    
unittest.main()