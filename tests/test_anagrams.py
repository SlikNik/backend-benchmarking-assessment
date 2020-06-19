""" Test Suite for anagrams module. """
import unittest
import importlib
import timeit
import json
import functools

__author__ = "madarp"


class TestAnagrams(unittest.TestCase):
    """
    Benchmarking test case. We test actual functionality of `find_anagrams`
    with doctests, which is why this test case excludes those unit tests.
    """
    def setUp(self):
        module_name = 'anagrams'
        """
        import the module(s) under test, 
        in the context of this test fixture
        """
        try:
            self.ana = importlib.import_module(module_name)
        except ImportError:
            self.fail('Unable to import module: ' + module_name)

    def run_find_anagrams(self, word_list, benchmark):
        """Helper func to time the find_anagrams() func"""
        f = functools.partial(self.ana.find_anagrams, word_list)
        t = timeit.Timer(f)
        actual_time = round(t.timeit(number=1), 3)
        failure_text = (
            f'\nfind_anagrams() took {actual_time:.03f} seconds, which exceeds'
            f' the benchmark of {benchmark:.03f} seconds'
            )
        self.assertLessEqual(actual_time, benchmark, failure_text)

    def test_correct_result(self):
        """Check the anagram dict result for correctness"""
        with open("words/short.txt") as f:
            short_list = f.read().split()
        actual_dict = self.ana.find_anagrams(short_list)
        self.assertIsInstance(actual_dict, dict)
        with open('tests/short_list.json') as f:
            # json.loads take a string as input and returns a dictionary
            # json.dumps take a dictionary as input and returns a string
            expected_dict = json.loads(str(f.read()))
        self.assertDictEqual(actual_dict, expected_dict)

    def test_short(self):
        """Check find_anagrams() func timing with short word list."""
        with open("words/short.txt") as f:
            short_list = f.read().split()
        self.run_find_anagrams(short_list, 0.030)

    @unittest.skip("Remove this line once short test passes")
    def test_long(self):
        """Check find_anagrams() with long word list."""
        with open("words/long.txt") as f:
            long_list = f.read().split()
        self.run_find_anagrams(long_list, 0.500)


if __name__ == '__main__':
    unittest.main()
