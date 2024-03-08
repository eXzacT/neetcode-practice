from src.kth_largest_element import KthLargestNaive, KthLargestOptimized, KthLargestOptimizedNoLib


def test_kth_largest_naive():
    kth_largest = KthLargestNaive(3, [4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8


def test_kth_largest_optimized():
    kth_largest = KthLargestOptimized(3, [4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8


def test_kth_largest_optimized_nolib():
    kth_largest = KthLargestOptimizedNoLib(3, [4, 5, 8, 2])

    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8
