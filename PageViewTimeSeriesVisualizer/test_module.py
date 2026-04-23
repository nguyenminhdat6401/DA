import unittest
import time_series_visualizer
import matplotlib as mpl


class PageViewTestCase(unittest.TestCase):
    def setUp(self):
        self.fig_line = time_series_visualizer.draw_line_plot()
        self.fig_bar = time_series_visualizer.draw_bar_plot()
        self.fig_box = time_series_visualizer.draw_box_plot()

    def test_line_plot_title(self):
        actual = self.fig_line.axes[0].get_title()
        expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, expected)

    def test_line_plot_labels(self):
        actual_x = self.fig_line.axes[0].get_xlabel()
        actual_y = self.fig_line.axes[0].get_ylabel()
        self.assertEqual(actual_x, "Date")
        self.assertEqual(actual_y, "Page Views")

    def test_line_plot_data_quantity(self):
        actual = len(self.fig_line.axes[0].lines[0].get_ydata())
        self.assertTrue(1230 <= actual <= 1240)

    def test_bar_plot_legend_labels(self):
        legend = self.fig_bar.axes[0].get_legend()
        actual = [t.get_text() for t in legend.get_texts()]
        expected = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        self.assertEqual(actual, expected)

    def test_bar_plot_labels(self):
        ax = self.fig_bar.axes[0]
        self.assertEqual(ax.get_xlabel(), "Years")
        self.assertEqual(ax.get_ylabel(), "Average Page Views")

    def test_box_plot_titles(self):
        self.assertEqual(
            self.fig_box.axes[0].get_title(), "Year-wise Box Plot (Trend)"
        )
        self.assertEqual(
            self.fig_box.axes[1].get_title(), "Month-wise Box Plot (Seasonality)"
        )

    def test_box_plot_labels(self):
        ax0 = self.fig_box.axes[0]
        ax1 = self.fig_box.axes[1]
        self.assertEqual(ax0.get_xlabel(), "Year")
        self.assertEqual(ax0.get_ylabel(), "Page Views")
        self.assertEqual(ax1.get_xlabel(), "Month")
        self.assertEqual(ax1.get_ylabel(), "Page Views")

    def test_box_plot_month_labels(self):
        actual = [
            label.get_text() for label in self.fig_box.axes[1].get_xticklabels()
        ]
        expected = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
