import unittest

from text_analyzer import TextAnalyzer


class TextAnalyzerTest(unittest.TestCase):
    def test_success_list(self):
        analyzer = TextAnalyzer()
        analyzer.add_group_list("test", ["one", "two", "tree"])
        result = analyzer.analyze("one two tree")
        self.assertEqual(result["test"], 3)

    def test_success_str(self):
        analyzer = TextAnalyzer()
        analyzer.add_group_str("test", "one, two, tree")
        result = analyzer.analyze("one two tree")
        self.assertEqual(result["test"], 3)


if __name__ == '__main__':
    unittest.main()
