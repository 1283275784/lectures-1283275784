import unittest
from leading import leading_substrings

class TestLeadingSubstrings(unittest.TestCase):

    def test_basic_functionality(self):
        """Test basic functionality with a standard string."""
        self.assertEqual(leading_substrings('bear'), ['b', 'be', 'bea', 'bear'])

    def test_empty_string(self):
        """Test the function with an empty string."""
        self.assertEqual(leading_substrings(''), [])

    def test_single_character(self):
        """Test the function with a single character string."""
        self.assertEqual(leading_substrings('a'), ['a'])

    def test_string_with_spaces(self):
        """Test the function with a string that contains spaces."""
        self.assertEqual(leading_substrings('a b'), ['a', 'a ', 'a b'])

    def test_identical_characters(self):
        """Test the function with a string of identical characters."""
        self.assertEqual(leading_substrings('aaaa'), ['a', 'aa', 'aaa', 'aaaa'])

    def test_long_string(self):
        """Test the function with a longer string."""
        self.assertEqual(leading_substrings('abcdefgh'), ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh'])

    def test_special_characters(self):
        """Test the function with a string that includes special characters."""
        self.assertEqual(leading_substrings('abc!@#'), ['a', 'ab', 'abc', 'abc!', 'abc!@', 'abc!@#'])

    def test_performance(self):
        """Test the function with a very long string."""
        long_string = 'a' * 1000
        expected_output = [long_string[:i+1] for i in range(len(long_string))]
        self.assertEqual(leading_substrings(long_string), expected_output)

if __name__ == '__main__':
    unittest.main()