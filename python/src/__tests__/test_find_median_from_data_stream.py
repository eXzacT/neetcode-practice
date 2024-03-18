from src.find_median_from_data_stream import MedianFinder, MedianFinderNaive, MedianFinderV2


def test_find_median_from_data_stream_naive():
    medianFinder = MedianFinderNaive()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.0


def test_find_median_from_data_stream():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.0


def test_find_median_from_data_stream_V2():
    medianFinder = MedianFinderV2()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.0
