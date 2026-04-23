import time_series_visualizer
import unittest

print("Drawing line plot...")
time_series_visualizer.draw_line_plot()
print("Drawing bar plot...")
time_series_visualizer.draw_bar_plot()
print("Drawing box plot...")
time_series_visualizer.draw_box_plot()
print("Done. Saved line_plot.png, bar_plot.png, box_plot.png")

# Run unit tests automatically
from test_module import PageViewTestCase  # noqa: E402,F401

unittest.main(module="test_module", exit=False)
