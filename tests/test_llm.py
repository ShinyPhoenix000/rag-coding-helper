import unittest
from rag.helper import answer_question

class TestAnswerQuestion(unittest.TestCase):
    def test_basic_query(self):
        result = answer_question("What is pandas?", use_mock=True, k=1)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_no_result(self):
        result = answer_question("asdkjashdkjashd", use_mock=True, k=1)
        self.assertIn("No relevant information", result)

    def test_multiple_results(self):
        result = answer_question("git", use_mock=True, k=2)
        self.assertIsInstance(result, str)
        self.assertGreaterEqual(len(result.splitlines()), 1)

if __name__ == "__main__":
    unittest.main()
