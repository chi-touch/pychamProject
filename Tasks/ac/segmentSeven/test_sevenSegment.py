from ac.segmentSeven.sevenSegment import SevenSegment
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.segment = SevenSegment()
        ans = SevenSegment()

    def test_for_length(self):
        ans = SevenSegment()
        result = "1100111"
        with self.assertRaises(ValueError):
            SevenSegment.displays(ans, result)

    def test_for_horizontal(self):
        ans = SevenSegment()
        result = "1200111"
        with self.assertRaises(BaseException):
            SevenSegment.displays(ans, result)

    def test_for_vertical(self):
        ans = SevenSegment()
        result = "1"
        self.assertEqual("1", SevenSegment.horizontal("# # # #"))
