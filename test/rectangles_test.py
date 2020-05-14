import unittest

def calc_area(l, w):
    """
    Params: l and w are both real positive numbers
    representing length and with
    """
    if l <= 0 or w <= 0:
        raise ValueError

    return l * w

class TestRectangles(unittest.TestCase):

    def test_area_calculation(self):
        self.assertEqual(calc_area(5, 3), 15)

        with self.assertRaises(ValueError):
            calc_area(-5, 3)

        with self.assertRaises(ValueError):
            calc_area(5, -3)

if __name__ == "__main__":
    unittest.main()
