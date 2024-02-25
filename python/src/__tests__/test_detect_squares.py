from src.detect_squares import DetectSquaresNaive, DetectSquaresOptimized


def test_detect_squares():
    ds = DetectSquaresNaive()
    ds.add([5, 10])
    ds.add([10, 5])
    ds.add([10, 10])
    assert ds.count([5, 5]) == 1

    ds.add([3, 0])
    ds.add([8, 0])
    ds.add([8, 5])
    assert ds.count([3, 5]) == 1

    ds.add([9, 0])
    ds.add([9, 8])
    ds.add([1, 8])
    assert ds.count([1, 0]) == 1

    ds.add([0, 0])
    ds.add([8, 0])
    ds.add([8, 8])
    assert ds.count([0, 8]) == 2

    ds.add([1, 9])
    ds.add([2, 9])
    ds.add([2, 10])
    assert ds.count([1, 10]) == 1

    ds.add([7, 8])
    ds.add([2, 3])
    ds.add([2, 8])
    assert ds.count([7, 3]) == 1

    ds.add([9, 10])
    ds.add([9, 5])
    ds.add([4, 5])
    assert ds.count([4, 10]) == 1


def test_detect_squares_v2():
    ds = DetectSquaresOptimized()
    ds.add([5, 10])
    ds.add([10, 5])
    ds.add([10, 10])
    assert ds.count([5, 5]) == 1

    ds.add([3, 0])
    ds.add([8, 0])
    ds.add([8, 5])
    assert ds.count([3, 5]) == 1

    ds.add([9, 0])
    ds.add([9, 8])
    ds.add([1, 8])
    assert ds.count([1, 0]) == 1

    ds.add([0, 0])
    ds.add([8, 0])
    ds.add([8, 8])
    assert ds.count([0, 8]) == 2

    ds.add([1, 9])
    ds.add([2, 9])
    ds.add([2, 10])
    assert ds.count([1, 10]) == 1

    ds.add([7, 8])
    ds.add([2, 3])
    ds.add([2, 8])
    assert ds.count([7, 3]) == 1

    ds.add([9, 10])
    ds.add([9, 5])
    ds.add([4, 5])
    assert ds.count([4, 10]) == 1
