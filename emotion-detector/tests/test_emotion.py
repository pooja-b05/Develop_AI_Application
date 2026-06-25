import unittest
from emotion_detector import analyze_emotion

class TestEmotion(unittest.TestCase):

    def test_joy(self):
        result = analyze_emotion("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = analyze_emotion("I am very sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_empty(self):
        result = analyze_emotion("")
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()