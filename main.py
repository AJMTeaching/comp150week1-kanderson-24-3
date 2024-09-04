# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.Create a list called my_list with the values [1, 5, 'apple', 20.5].

my_list = [1, 5, 'apple', 20.5]
print(my_list[2])
my_list.append(10)
print(my_list)
my_list.remove(20.5)
print(my_list)
my_list.reverse()
print(my_list)

# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.

def create_person_dict():
    person = {
        'name': 'John',
        'age': 30,
        'job': 'teacher'
    }

    return person

def print_job(person: dict):
    print(person['job'])

def add_city(person: dict):
    person['city'] = 'Paris'
    print(person)

def remove_age(person: dict):
    if 'age' in person:
        del person['age']
    print(person)

def print_all_info(person: dict):
    for key, value in person.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    person_dict = create_person_dict()
    print_job(person_dict)
    add_city(person_dict)
    remove_age(person_dict)
    print_all_info(person_dict)

# -----------------------------------------------------------------------------

# Importing sys for test function
import sys

# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)

# Function 1: count_vowels

def count_vowels(s: str) -> int:
   vowels = "aeiouAEIOU"
   count = 0
   if not isinstance(s, str):
       raise ValueError("Input must be a string")
   
   for char in s:
       if char in vowels:
           count += 1
   return count        

"""The function counts the vowels in a given string using a loop and conditional checks. The manual iteration and character-by-character checking provides control in dealing with both upper and lower case vowels. This avoids using shortcuts that were restricted in this section"""
       
# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)

# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list
            
# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])

"""This function merges two sorted lists into one sorted list using two pointers and a loop. The two-pointer technique is efficient for merging sorted lists in the format O(n+m) time. This is a fundamental way of combining data."""

# Function 3: word_lengths
def word_lengths(words: list) -> list:
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths 

# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 11])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])

"""The function created calculates the length of each string in a list using a simple loop and appends the results to be in a new list. This approach directly deals with the problem by iterating over each string and calculating its length manually."""

# Function 4: reverse_string
def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")

""""This function reverses a string by recursively processing the string from the last character to the first, or via a loop mechanism. Recusion is a taught way that demonstrates string reversal, especially since it divides the described problem into manageable parts"""

# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()

"""This function finds the common elements between two lists by using nested loops or a dictionary to track and compare occurrences. The nested loop approach proves a simple method for finding intersection and a dictionary based solution emphasizes how counting occurrences can make the process quicker."""