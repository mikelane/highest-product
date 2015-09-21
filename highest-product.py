#!/usr/bin/env python3

"""
Interview Cake Problem 3: Highest Product of 3

Input:      Array of unsorted integers.
Output:     The maximum value of the product of any 3 of those integers.
Note:       In the array [-10, -10, 1, 3, 2], the maximum value is -10 * -10 * 3
            = 300. Testing for negative values is imperative
Solution:   Using the greedy approach, keep track of current lowest, highest,
            highest and lowest product of 2 so far, and highest and lowest
            product of 3 so far. Once you've stepped through the entire array,
            return the value of the highest product of 3.
Bonus:      Make the solution work for any number of products instead of just 3.
Efficiency: Algorithm (both for product of 3 and product of an arbitrary k) is
            O(n) time complexity and O(1) space complexity. (A given value of k
            remains constant for any arbitrary value of n >= k; hence, the extra
            space used in the data structure to hold the calculated values is
            constant.)
"""
import random

__author__ = 'Mike Lane'
__copyright__ = 'Copyright 2015, Michael Lane'
__license__ = 'GPL'
__version__ = '3.0'
__email__ = 'mikelane@gmail.com'


def highest_product(input_array, k=3):
    """
    :param input_array: Instance of an array of integers (sorted or unsorted)
    :return: Value of the highest product of 3 of the array elements
    """
    # Raise an exception if the input number of items to determine the product
    # of exceeds the number in the array
    if k > len(input_array):
        raise ValueError('input_array has fewer than ' + str(k) + ' items!')

    # Initialize the result
    result = 1

    # If the number that makes up the max product is the same as the number of
    # items in the array, then we can return the product of all the items in the
    # array.
    if k == len(input_array):
        for i in input_array:
            result *= i
        return result

    # Initialize the arrays used to keep track of the results
    highest_arr = [0] * k
    lowest_arr = [0] * (k)
    # highest_product_of_3 = 0
    # highest_product_of_2 = 0
    # highest = 0
    # lowest_product_of_2 = 0
    # lowest = 0

    # for i in input_array:
    #     current = i

    # Loop through each item in the array
    for current in input_array:
        # Keep track of the highest values starting with the highest and working
        # backwards
        for n in range(k-1, -1, -1):
            # Keep track of the highest product of 1 < n <= k values.
            if n > 0:
                # The highest product of n values is the max of: 1) The currently
                # calcuated value, 2) the current value times the highest product
                # of n-1 values, and 3) the current value times the lowest
                # product of n-1 values
                highest_arr[n] = max(
                    highest_arr[n],
                    current * highest_arr[n-1],
                    current * lowest_arr[n-1]
                )

                # The lowest product of n values is the min of: 1) The currently
                # calcuated value, 2) the current value times the highest product
                # of n-1 values, and 3) the current value times the lowest
                # product of n-1 values
                lowest_arr[n] = min (
                    lowest_arr[n],
                    current * highest_arr[n-1],
                    current * lowest_arr[n-1]
                )
            # keep track of the current highest and lowest value in the array
            else:
                highest_arr[0] = max(current, highest_arr[0])
                lowest_arr[0] = min(current, lowest_arr[0])

    # Return the last element of the array that tracks the highest values. Note
    # that this array holds the highest value in the array, the highest value of
    # the product of 2 elements in the array, the highest value of the product
    # of three values in the array, and so on. The lowest_arr holds the
    # corresponding lowest values.
    return highest_arr[len(highest_arr)-1]

    #     highest_product_of_3 = max(
    #         highest_product_of_3,
    #         current * highest_product_of_2,
    #         current * lowest_product_of_2
    #     )
    #
    #     highest_product_of_2 = max(
    #         highest_product_of_2,
    #         current * highest,
    #         current * lowest
    #     )
    #
    #     lowest_product_of_2 = min(
    #         lowest_product_of_2,
    #         current * highest,
    #         current * lowest
    #     )
    #
    #     highest = max(highest, current)
    #
    #     lowest = min(lowest, current)
    #
    #
    # return highest_product_of_3

# Make an array of test inputs.
test = [
    {"input_array": [1, 1, 1], "k": 3, "Expected": 1},
    {"input_array": [0], "k": 2, "Expected": "ERROR"},
    {"input_array": [1, 2, 3, 4], "k": 2, "Expected": 12},
    {"input_array": [3, 2, 1, 0, -1, -2, -3], "k": 4, "Expected": 36},
    {"input_array": [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6], "k": 4, "Expected": 900},
    {"input_array": [-10, -10, 1, 3, 2], "k": 3, "Expected": 300},
    {"input_array": [-1, -2, -3, 5, 3, 2], "k": 3, "Expected": 30},
    {"input_array": [-1, 3, -3, 1], "k": 3, "Expected": 9},
    {"input_array": [-10, -1, 3, 4, 5], "k": 3, "Expected": 60},
    {"input_array": [1, 10, -5, 1, -100], "k": 3, "Expected": 5000}
]


# For each of the test input items, run the function and determine if the output
# was as expected.
for item in test:
    try:
        result = highest_product(item['input_array'], item['k'])
    except ValueError as err:
        print("Expected: Error  Actual: Error   PASS  ERROR:", err.args[0])
    else:
        expected = item['Expected']
        test = result == expected
        if test == True:
            test = "PASS"
        else:
            test = "FAIL"
        print("Expected: {:<7}Actual: {:<7} {:<7}".format(expected, result, test))

# a = [-10, -10, 1, 3, 2]     # 300
# b = [-1, -2, -3, 5, 3, 2]   # 30
# c = [-1, 3, -3, 1]          # 6
# d = [-10, -1, 3, 4, 5]      # 60
# e = [1, 10, -5, 1, -100]    # 5000
#
# highest_a = highest_product(a)
# highest_b = highest_product(b)
# highest_c = highest_product(c)
# highest_d = highest_product(d)
# highest_e = highest_product(e)
# print(
#     """
#     a: {}
#     b: {}
#     c: {}
#     d: {}
#     e: {}
#     """.format(highest_a, highest_b, highest_c, highest_d, highest_e)
# )
