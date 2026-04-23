import unittest
import sea_level_predictor as sea_level
import matplotlib as mpl


class DataTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level.draw_plot()

    def test_xlabel(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected x label to be 'Year'")

    def test_ylabel(self):
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected y label to be 'Sea Level (inches)'")

    def test_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected title to be 'Rise in Sea Level'")

    def test_data_points(self):
        actual = len(self.ax.collections[0].get_offsets().data)
        expected = 134
        self.assertEqual(actual, expected, "Expected scatter plot to contain 134 data points.")

    def test_lines(self):
        actual = len(self.ax.lines)
        expected = 2
        self.assertEqual(actual, expected, "Expected 2 lines of best fit on the plot.")


if __name__ == "__main__":
    unittest.main()
