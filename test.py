import unittest
from app import get_word_frequencies

class TestWordFrequency(unittest.TestCase):

    def test_get_word_frequencies(self):
        input_str = 'foo bar moo mar foo too soo sar coo car moo cat'
        expected_output = {'foo':2, 'bar':1, 'moo':2, 'mar':1, 'too':1, 'soo':1, 'sar':1, 'coo':1, 'car':1, 'cat':1}
        self.assertEqual(get_word_frequencies(input_str)), expected_output)

if __name__=='__main__':
    unittest.main()