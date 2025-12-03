"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

"""


"""
UNDERSTAND:
    - Input: array of integers 
    - Output: True if any value appears more than once, False if all values are unique
    - If array is empty, return False as there are no duplicates
    - If array has one element, return False as there are no duplicates

MATCH:
    - Checking for repeated elements
    - Brute Force: nested loops where we compare all pairs O(n^2)
    - Hashing/Sets: store seen elements and check membership O(n)
"""


"""
BRUTE FORCE:

- Use two nested loops
- Compare nums[i] with all elements to the right of it 
- If any pair is equal, return True
- If loop finishes without finding duplicates, return False

- Time: O(n^2) - every pair is compared
- Space: O(1) - no extra data structure needed

"""
def containsDuplicate_brute(nums):
    # Loop through each index in the list
    for i in range(len(nums)):
        # Compare each element at i with the element next to it
        for j in range(i+1, len(nums)):
            # If numbers are the same, found duplicate
            if nums[i] == nums[j]:
                return True
    return False

"""
OPTIMIZED USING SET:

- Create an empty set for seen numbers
- Loop through every num in nums
- For each num, if it is already in seen, return True
- Else add num to seen
- If loop finishes with no repeat return False

- Time - O(n) - set membership and insert are O(1) on average
- Space - O(n) - in worst case all elements are stored in set
"""

def containsDuplicate_optimized(nums):

    # Declare empty set for seen numbers
    seen = set()

    # Loop through each num
    for i in range(len(nums)):
        # Check if nums[i] in set
        if nums[i] in seen:
            return True
        # Add nums[i] to seen set
        seen.add(nums[i])
    # If loop finishes, no duplciates were found
    return False


nums = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

print(containsDuplicate_brute(nums))
print(containsDuplicate_brute(nums2))

print(containsDuplicate_optimized(nums))
print(containsDuplicate_optimized(nums2))