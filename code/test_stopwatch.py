import unittest
import time
from stopwatch import StopWatch, StopWatchError

class TestStopWatch(unittest.TestCase):

    def test_start(self):
        
        test_stopwatch = StopWatch()

        test_stopwatch.start()
        with self.assertRaises(StopWatchError) : test_stopwatch.start()

    def test_stop(self):

        test_stopwatch = StopWatch()

        with self.assertRaises(StopWatchError) : test_stopwatch.stop()

        test_stopwatch.start()
        time.sleep(0.5)
        self.assertAlmostEqual(test_stopwatch.stop(), 0.5, places=2)

        test_stopwatch.start()
        time.sleep(1)
        self.assertAlmostEqual(test_stopwatch.stop(), 1., places=2)

if __name__ == "__main__":

    unittest.main()