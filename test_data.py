meetings = [
    {
        "meeting_time": [(0, 30), (5, 10), (15, 20)],
        "needed_rooms": 2
    },
    {
        "meeting_time": [(5, 8), (9, 15)],
        "needed_rooms": 1
    },
    {
        "meeting_time": [(0, 5), (5, 10), (10, 20)],
        "needed_rooms": 1
    },
    {
        "meeting_time": [(0, 5), (5, 10), (9, 20)],
        "needed_rooms": 2
    },
    {
        "meeting_time": [(0, 20), (0, 30), (0, 40), (5, 10), (20, 50), (0, 50)],
        "needed_rooms": 5
    },
    {
        "meeting_time": [(4, 8), (5, 10), (6, 8), (9, 16), (15, 20)],
        "needed_rooms": 3
    }
]

binary_trees = [
    {
        "implicit_representation": [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
        "explicit_representation": [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4],
        "diameter": 6,
        "depth": 4,
        "inverse_tree": [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
        "subtree": [2, 3, None, 4],
        "not_subtree":[2, 2, 3],
        "is_balanced": False
    },
    {
        "implicit_representation": [1, 2, 4, None, 3, 4],
        "explicit_representation": [1, 2, 4, None, 3, 4],
        "diameter": 4,
        "depth": 3,
        "inverse_tree": [1, 4, 2, None, 4, 3],
        "subtree":[2, None, 3],
        "not_subtree":[1, 2, 3],
        "is_balanced": True
    }
]

non_overlapping_intervals = [
    {
        "original_intervals": [[1, 3], [6, 9]],
        "new_interval": [2, 5],
        "merged_intervals": [[1, 5], [6, 9]]
    },
    {
        "original_intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        "new_interval": [4, 8],
        "merged_intervals": [[1, 2], [3, 10], [12, 16]]
    },
    {
        "original_intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [18, 20]],
        "new_interval": [4, 8],
        "merged_intervals": [[1, 2], [3, 10], [12, 16], [18, 20]]
    },
    {
        "original_intervals": [[5, 6], [8, 9], [10, 11]],
        "new_interval": [4, 8],
        "merged_intervals": [[4, 9], [10, 11]]
    },
    {
        "original_intervals": [[5, 6], [8, 9], [10, 11]],
        "new_interval": [2, 3],
        "merged_intervals": [[2, 3], [5, 6], [8, 9], [10, 11]]
    },
    {
        "original_intervals": [[5, 6], [8, 9], [10, 11]],
        "new_interval": [12, 14],
        "merged_intervals": [[5, 6], [8, 9], [10, 11], [12, 14]]
    },
    {
        "original_intervals": [[8, 9], [5, 6], [10, 11]],
        "new_interval": [12, 14],
        "merged_intervals": [[5, 6], [8, 9], [10, 11], [12, 14]]
    }
]

overlapping_intervals = [
    {
        "original_intervals": [[1, 4], [6, 7], [9, 11], [2, 11]],
        "merged_intervals": [[1, 11]],
        "min_removals_for_no_overlap": 1
    },
    {
        "original_intervals": [[1, 4], [3, 5], [4, 7]],
        "merged_intervals": [[1, 7]],
        "min_removals_for_no_overlap": 1
    },
    {
        "original_intervals": [[5, 6], [1, 6], [4, 11], [12, 14]],
        "merged_intervals": [[1, 11], [12, 14]],
        "min_removals_for_no_overlap": 2
    },
    {
        "original_intervals": [[8, 9], [6, 7], [10, 11]],
        "merged_intervals": [[6, 7], [8, 9], [10, 11]],
        "min_removals_for_no_overlap": 0
    },
    {
        "original_intervals": [[8, 11], [1, 3], [4, 6], [1, 7], [4, 5], [8, 9], [10, 12]],
        "merged_intervals": [[1, 7], [8, 12]],
        "min_removals_for_no_overlap": 3
    }
]
sudoku_boards = [
    {
        "board": [["5", "3", ".",  ".", "7", ".",  ".", ".", "."],
                  ["6", ".", ".",  "1", "9", "5",  ".", ".", "."],
                  [".", "9", "8",  ".", ".", ".",  ".", "6", "."],

                  ["8", ".", ".",  ".", "6", ".",  ".", ".", "3"],
                  ["4", ".", ".",  "8", ".", "3",  ".", ".", "1"],
                  ["2", ".", ".",  ".", "4", ".",  ".", ".", "6"],

                  ["9", "6", ".",  ".", ".", ".",  "2", "8", "."],
                  ["1", ".", ".",  "4", "2", "9",  ".", ".", "5"],
                  [".", "2", ".",  ".", "8", ".",  ".", "7", "9"]],

        "is_valid": True
    },
    {
        "board": [["2", "3", ".",  ".", "7", ".",  ".", ".", "."],
                  ["6", ".", ".",  "1", "9", "5",  ".", ".", "."],
                  ["4", "9", "2",  ".", ".", ".",  ".", "6", "."],

                  ["2", ".", ".",  ".", "6", ".",  ".", ".", "3"],
                  ["5", ".", ".",  "8", ".", "3",  ".", ".", "1"],
                  ["1", ".", ".",  ".", "2", ".",  ".", ".", "6"],

                  [".", "6", ".",  ".", ".", ".",  "2", "8", "."],
                  [".", ".", ".",  "4", "1", "9",  ".", ".", "5"],
                  [".", ".", ".",  ".", "8", ".",  ".", "7", "9"]],

        "is_valid": False
    },
]

arrays_strings = [
    {
        "array": ["pero", "dijetlic", "majmun"]
    },
    {
        "array": ["per076", "ver123", "serial"]
    },
    {
        "array": ["sd!30", "slx42", "xA310!"]
    },
    {
        "array": ["s23#!30", "slx42", "xA310!"]
    }
]
