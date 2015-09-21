# Interview Cake Problem 3: Highest Product of 3

Input:      Array of unsorted integers.
======
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