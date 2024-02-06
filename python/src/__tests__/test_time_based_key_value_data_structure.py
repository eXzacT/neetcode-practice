from src.time_based_key_value_data_structure import TimeMap


def test_time_based_key_value_data_structure():
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    assert timeMap.get("foo", 1) == "bar"
    # Closest timestamp is at 1, so it will closest lower timestamp which is 1-> bar
    assert timeMap.get("foo", 3) == "bar"
    timeMap.set("foo", "bar2", 4)
    assert timeMap.get("foo", 4) == "bar2"
    assert timeMap.get("foo", 5) == "bar2"
    assert timeMap.get("foo", 2) == "bar"
