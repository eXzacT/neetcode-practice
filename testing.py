from colorama import Fore, Style
from binary_trees import *
from meeting import *

total_passed_tests=0
total_tests=0

meetings = [
    {
        "meeting_time" : [(0,30), (5,10), (15,20)], 
        "needed_rooms" : 2
    },
    {
        "meeting_time" : [(5,8), (9,15)], 
        "needed_rooms" : 1
    },
    {
        "meeting_time" : [(0,5),(5,10),(10,20)], 
        "needed_rooms" : 1
    },
    {
        "meeting_time" : [(0,5),(5,10),(9,20)], 
        "needed_rooms" : 2
    },
    {
        "meeting_time" : [(0,20),(0,30),(0,40),(5,10),(20,50),(0,50)], 
        "needed_rooms" : 5
    },
    {
        "meeting_time" : [(4,8),(5,10),(6,8),(9,16),(15,20)], 
        "needed_rooms" : 3
    }
]

binary_trees = [
    {   
        "correct_array_representation": [1, 2, 2, 3, None, None, 3, 4, None,None, 4],
        "implicit_array_representation": [1, 2, 2, 3, None, None, 3, 4, None,None, 4],
        "explicit_array_representation": [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4],
        "diameter": 6,
        "depth": 4,
        "inverse_tree": ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], True),
        "subtree": ([3, 4, None], True),
        "not_subtree": ([3, 4, 4], False),
        "is_balanced": False
    },
    { 
        "correct_array_representation":  [1, 2, 4, None, 3, 4],
        "implicit_array_representation": [1, 2, 4, None, 3, 4],
        "explicit_array_representation": [1, 2, 4, None, 3, 4],
        "diameter": 4,
        "depth": 3,
        "inverse_tree": ([1, 4, 2, None, 4, 3], True),
        "subtree": ([2, 3, None], True),
        "not_subtree": ([4, None, 3, 2], False),
        "is_balanced": True
    }
]

def assert_equals(testing,expected_result, result) -> None:
    """ Check if both values are the same and notifies the user"""
    global total_passed_tests
    global total_tests
    passed=expected_result==result
    if passed:
        total_passed_tests+=1
        test_result,color,equality="Test passed",Fore.GREEN,"=="
    else:
        test_result,color,equality="Test failed",Fore.RED,"!="
    
    print(f"Result for ({testing})\nExpected ({expected_result}) {equality} Got ({result}) " + color + test_result + Style.RESET_ALL+"\n")
    total_tests+=1

def print_FAIL(text: str) -> None:
    """ Print test failure 2023-10-24 14:00:43 """
    global total_tests
    total_tests+=1
    print(text + Fore.RED + "\nTest failed" + Style.RESET_ALL+"\n")

def test_meeting():
    for meeting in meetings:
        
        expected_result=meeting['needed_rooms']
        result = rooms_needed(list(meeting['meeting_time']))
        
        assert_equals(meeting['meeting_time'],expected_result,result)

def test_binary_trees():

    for tree in binary_trees:

        print("Testing if all 3 initialization functions initialize the same way and if it matches the true representation.")
        tree1=init_tree(tree['implicit_array_representation'],'implicit_input_iteratively')
        tree2=init_tree(tree['explicit_array_representation'],'implicit_input_recursively')
        tree3=init_tree(tree['explicit_array_representation'],'explicit_input')
    
        result1=tree_to_array(tree1)
        result2=tree_to_array(tree2)
        result3=tree_to_array(tree3)

        # print(result1)
        # print(result2)
        # print(result3)

        # If all three trees are the same then compare it to the true result
        if result1==result2==result3:
            assert_equals(tree['correct_array_representation'],result1)
        else:
            print_FAIL("Trees are not initialized the same way so testing needs to be stopped!")
            break

        # "diameter": 6
        print("Testing if diameter returns correct value.")
        assert_equals(tree['diameter'],diameter(tree1))

        # "depth": 4
        print("Testing if depth works as it should.")
        assert_equals(tree['depth'],depth(tree1))

        print("Testing if the inverse works as it should.")
        inverted_tree=invert_tree(tree1)
        result=tree_to_array(inverted_tree)
        expected_result=tree['inverse_tree'][0]
        # "inverse_tree": ([1, 2, 2, 3, None, None, 3, 4, None,None, 4], True)
        # boolean says if this(the inverse) is the same as the original tree
        are_same_trees=result==expected_result
        assert_equals(tree['inverse_tree'][1],are_same_trees)
        
        print("Testing if both iterative and recursive is_subtree checks work the same way and if they work as they should.")
        # "subtree": ([3,4,None], True)
        subtree=init_implicit_tree_iteratively(tree['subtree'][0])
        iterative_result=is_subtree_iteratively(subtree,tree1)
        recursive_result=is_subtree_recursively(subtree,tree1)
        expected_result=tree['subtree'][1]
        if iterative_result==recursive_result:
            assert_equals(expected_result,iterative_result)
        else:    
            print_FAIL("Iterative and Recursive approach to is_subtree results differ!")
                       
        print("Testing if both iterative and recursive is_subtree checks work the same way and if tree is not a subtree.")
        # "not_subtree": ([3,4,4], False)
        subtree=init_implicit_tree_iteratively(tree['not_subtree'][0])
        iterative_result=is_subtree_iteratively(subtree,tree1)
        recursive_result=is_subtree_recursively(subtree,tree1)
        expected_result=tree['not_subtree'][1]
        if iterative_result==recursive_result:
            assert_equals(expected_result,iterative_result)
        else:    
            print_FAIL("Iterative and Recursive approach to is_subtree results differ for not_subtree!")

        # "is_balanced": False
        print("Testing if is_balanced works as it should.")
        assert_equals(tree['is_balanced'],is_balanced(tree1))
        
#run all the tests
test_meeting()
#test_binary_trees()
print(f"\nTotal tests ran: {total_tests}\n" 
      + Fore.GREEN 
      + f"Passed: {total_passed_tests}\n" 
      + (Fore.RED + f"Failed: {total_tests - total_passed_tests} " if total_tests - total_passed_tests > 0 else "")
      + Style.RESET_ALL 
      + "\n")